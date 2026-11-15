"""Pruebas mínimas de MarCo (stdlib; jsonschema opcional)."""
import csv, glob, json, os, re, unittest, uuid
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = "{http://www.w3.org/2000/svg}"


class TestMarca(unittest.TestCase):
    def iconos(self):
        fs = [f for f in glob.glob(os.path.join(ROOT, "brand/logos/marco_*.svg")) if "wordmark" not in f]
        self.assertGreaterEqual(len(fs), 14)  # 7 diseños × (claro + oscuro)
        return fs

    def test_retricula_trazo_un_color(self):
        for f in self.iconos():
            root = ET.parse(f).getroot()
            self.assertEqual(root.get("viewBox"), "0 0 48 48", f)
            colores, sin_fondo = set(), True
            for el in root.iter():
                tag = el.tag.replace(NS, "")
                if tag == "rect":
                    sin_fondo = False
                for attr in ("stroke", "fill"):
                    v = el.get(attr)
                    if v and v != "none":
                        colores.add(v.upper())
                if el.get("stroke") not in (None, "none"):
                    self.assertEqual(el.get("stroke-width"), "3", f)
                    self.assertEqual(el.get("stroke-linecap"), "round", f)
            self.assertEqual(len(colores), 1, f"{f}: {colores}")
            self.assertTrue(sin_fondo, f)

    def test_color_marco(self):
        for f in self.iconos():
            esperado = "#9C9AF2" if f.endswith("_dark.svg") else "#5250CC"
            self.assertIn(esperado, open(f).read().upper(), f)

    def test_logo_oficial_es_propuesta_1(self):
        for v in ("", "_dark", "_wordmark", "_wordmark_dark"):
            a = open(os.path.join(ROOT, f"brand/oficial/marco_oficial{v}.svg")).read()
            b = open(os.path.join(ROOT, f"brand/logos/marco_m1_monograma{v}.svg")).read()
            self.assertEqual(a, b, v)
        self.assertIn("Logo oficial: propuesta 1", open(os.path.join(ROOT, "brand/LOGOS.md")).read())

    def test_wordmarks(self):
        ws = glob.glob(os.path.join(ROOT, "brand/logos/*_wordmark*.svg"))
        self.assertGreaterEqual(len(ws), 14)
        for f in ws:
            self.assertIn("MarCo", ET.parse(f).getroot().get("aria-label"))


BLOQUEADAS = ["cura", "curar", "curación", "elimina el cáncer", "100 %", "100%", "sin riesgo",
              "sin radiación", "garantizado", "el mejor", "¿tienes cáncer", "¿padeces"]
SENSIBLES_UTM = ["cancer", "cáncer", "tiroides", "prostata", "próstata", "tumor", "diagnostico"]


def revisar_pieza(p):
    errores = []
    copy = p.get("copy", "").lower()
    for w in BLOQUEADAS:
        if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", copy):
            errores.append(f"palabra bloqueada: {w}")
    destino = p.get("destino", "").lower()
    for w in SENSIBLES_UTM:
        if "utm_" in destino and w in destino.split("?", 1)[-1]:
            errores.append(f"término sensible en UTM: {w}")
    if p.get("contiene_datos_paciente"):
        errores.append("contiene datos de paciente")
    if not p.get("servicio_autorizado"):
        errores.append("servicio no autorizado")
    if p.get("estado") == "publicada" and not (p.get("permiso_o_aviso") and p.get("checklist_completo")):
        errores.append("publicada sin permiso/aviso o checklist")
    return errores


class TestCumplimiento(unittest.TestCase):
    def test_plantilla_pieza_limpia(self):
        p = json.load(open(os.path.join(ROOT, "campaigns/plantillas/pieza.json")))
        self.assertEqual(revisar_pieza(p), [])

    def test_detecta_promesas_y_atributos(self):
        malo = {"copy": "¿Tienes cáncer de tiroides? Te curamos, 100% sin riesgo", "servicio_autorizado": True}
        self.assertTrue(len(revisar_pieza(malo)) >= 3)

    def test_detecta_publicacion_sin_permiso(self):
        p = {"copy": "Horarios de la sede", "servicio_autorizado": True, "estado": "publicada"}
        self.assertIn("publicada sin permiso/aviso o checklist", revisar_pieza(p))

    def test_registro_columnas(self):
        cab = next(csv.reader(open(os.path.join(ROOT, "compliance/registro_piezas.csv"))))
        cols = ["pieza_id", "sede", "canal", "mes", "tramite", "permiso_o_aviso", "checklist_completo", "publicada"]
        self.assertEqual(cab, cols)
        cab2 = next(csv.reader(open(os.path.join(ROOT, "dashboard/data/cumplimiento_piezas.csv"))))
        self.assertEqual(cab2, cols)

    def test_checklist_tiene_19_puntos(self):
        txt = open(os.path.join(ROOT, "compliance/checklist.md")).read()
        self.assertEqual(len(re.findall(r"^\| (?:● )?\d+ \|", txt, flags=re.M)), 19)


class TestContrato(unittest.TestCase):
    PROHIBIDOS = {"diagnostico", "cie", "resultado", "resultados", "imagen", "imagenes", "notas", "nombre", "curp"}

    def setUp(self):
        self.schema = json.load(open(os.path.join(ROOT, "contracts/schemas/gamma.referencia.v1.json")))

    def test_sin_campos_clinicos(self):
        self.assertFalse(self.PROHIBIDOS & set(self.schema["properties"]))
        self.assertFalse(self.schema["additionalProperties"])

    def test_evento_valido_y_evento_con_diagnostico(self):
        ev = {"referencia_id": str(uuid.uuid4()), "emitido_en": "2027-01-10T10:00:00Z", "sede": "MID",
              "referente_ref": "ref-001", "servicio": "GAMMA-OSEA", "canal": "portal", "estado": "recibida",
              "atribucion": "mid_estudios_202701"}
        malo = dict(ev, diagnostico="C61")
        try:
            import jsonschema
        except ImportError:
            self.assertTrue(set(self.schema["required"]) <= set(ev))
            self.assertFalse(set(malo) <= set(self.schema["properties"]))
            return
        jsonschema.validate(ev, self.schema)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(malo, self.schema)


class TestTablero(unittest.TestCase):
    def test_presupuesto_pauta_coincide_con_plan(self):
        rows = list(csv.DictReader(open(os.path.join(ROOT, "dashboard/data/presupuesto_canal.csv"))))
        p = [r for r in rows if r["partida"] == "Pauta digital"]
        self.assertEqual(sum(int(r["bajo_mxn_mes"]) for r in p), 50000)
        self.assertEqual(sum(int(r["alto_mxn_mes"]) for r in p), 120000)

    def test_presupuesto_anual_coincide_con_plan(self):
        rows = list(csv.DictReader(open(os.path.join(ROOT, "dashboard/data/presupuesto_anual.csv"))))
        self.assertEqual(sum(int(r["bajo_mxn_anual"]) for r in rows), 7050000)
        self.assertEqual(sum(int(r["alto_mxn_anual"]) for r in rows), 13960000)

    def test_sin_datos_de_desempeno_inventados(self):
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/presupuesto_canal.csv"))):
            self.assertEqual(r["gasto_real_mxn_mes"], "")
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/kpis.csv"))):
            self.assertEqual(r["valor_real"], "")
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/sedes.csv"))):
            for k in ("referencias_mes", "referentes_activos", "conversion_pct", "nps", "sesiones_organicas", "costo_paciente_mxn"):
                self.assertEqual(r[k], "", (r["sede"], k))

    def test_plantillas_de_desempeno_vacias(self):
        plantillas = {
            "plazas_mensual.csv": ("estudios", "terapias", "referencias", "referentes_activos", "conversion_pct", "ingresos_mxn"),
            "canales.csv": ("alcance", "impresiones", "clics", "ctr_pct", "cpc_mxn", "leads", "cpl_mxn", "pacientes",
                            "costo_paciente_mxn", "gasto_mxn", "atribucion_ultimo_clic_pct"),
            "embudo.csv": ("valor",),
            "resenas_seo.csv": ("resenas_google", "calificacion_google", "nps_pacientes", "nps_referentes",
                                "posicion_media_seo", "local_pack_top3"),
        }
        for f, campos in plantillas.items():
            for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data", f))):
                for k in campos:
                    self.assertEqual(r[k], "", (f, k))

    def test_sinteticos_documentados(self):
        sup = open(os.path.join(ROOT, "dashboard/data/SUPUESTOS_SINTETICOS.md"), encoding="utf-8").read()
        self.assertIn("SINTÉTICO — no real", sup)
        self.assertIn("20261115", sup)
        self.assertIn("SEMILLA = 20261115", open(os.path.join(ROOT, "tools/sinteticos.py"), encoding="utf-8").read())
        sint = glob.glob(os.path.join(ROOT, "dashboard/data/sintetico_*.csv"))
        self.assertGreaterEqual(len(sint), 6)
        self.assertFalse(glob.glob(os.path.join(ROOT, "dashboard/data/ejemplo_*.csv")))
        for f in sint:
            cab = next(csv.reader(open(f, encoding="utf-8")))
            self.assertFalse({"paciente", "nombre_paciente", "medico", "nombre_medico", "curp"} & set(cab), f)

    def test_inventario_real_esquema(self):
        cols = ["sede", "anio", "mes", "tipo_estudio", "pacientes", "estudios", "referente_codigo", "especialidad_referente"]
        tipos = {"gammagrafia_osea", "tiroidea", "renal", "rastreo_i131", "terapia_i131", "lu177",
                 "perfusion_miocardica", "paratiroides", "otras"}
        sedes = {"MID", "VHSA1", "VHSA2", "OAX", "TOL", "COL"}
        for nombre in ("real_inventario.csv", "sintetico_inventario.csv"):
            rows = list(csv.reader(open(os.path.join(ROOT, "dashboard/data", nombre), encoding="utf-8")))
            self.assertEqual(rows[0], cols, nombre)
            for r in rows[1:]:
                d = dict(zip(cols, r))
                self.assertIn(d["sede"], sedes)
                self.assertIn(d["tipo_estudio"], tipos)
                self.assertRegex(d["referente_codigo"], r"^(R-\d{3,})?$")
                self.assertTrue(int(d["estudios"]) >= 0 and int(d["pacientes"]) >= 0)

    def test_datos_publicos_con_fuente(self):
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/geo_estados.csv"))):
            self.assertTrue(r["fuente_poblacion"].startswith("https://") and r["fuente_mortalidad"].startswith("https://"))
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/cancer_mexico.csv"))):
            if r["valor"]:
                self.assertTrue(r["url"].startswith("https://"), r["indicador_id"])
        for r in csv.DictReader(open(os.path.join(ROOT, "dashboard/data/congresos.csv"))):
            if r["verificado"] == "No":
                self.assertEqual(r["inicio"], "", r["congreso_id"])

    def test_conectores_cubren_fuentes_del_esquema(self):
        esquema = json.load(open(os.path.join(ROOT, "dashboard/metricas.schema.json")))
        con = {c["fuente"] for c in json.load(open(os.path.join(ROOT, "dashboard/conectores.json")))}
        self.assertTrue(set(esquema["properties"]["fuente"]["enum"]) - {"privacidad"} <= con)


if __name__ == "__main__":
    unittest.main()
