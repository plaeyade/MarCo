"""Convierte la salida AGREGADA de HEVESY (resumen_tablero.json) en los CSV reales del tablero.

Uso:  python3 -I tools/real_inventario.py <ruta>/resumen_tablero.json

Escribe dashboard/data/real_inventario.csv y dashboard/data/real_inventario_calidad.csv.
El JSON de entrada vive fuera del repositorio (PC del propietario); sólo trae vocabulario
cerrado, conteos y códigos de referente R-###. Este script NO lee expedientes.

Regla k >= 5: ninguna celda con 1-4 pacientes se escribe sola. Las celdas chicas se suman en
«otros/<5» dentro de su sede; si esa suma sigue < 5, se suman con las de otras sedes en una
fila sede = «otros/<5». Ver dashboard/data/SUPUESTOS_SINTETICOS.md («Datos reales»).
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dashboard", "data")
K = 5
OTROS = "otros/<5"
SEDE = {"merida": "MID", "villahermosa_sede1_gamma": "VHSA1", "oaxaca": "OAX",
        "desconocida": "desconocida", "ambigua": "ambigua"}
TIPO = {"osea": "gammagrafia_osea"}  # el resto del vocabulario de HEVESY coincide con el del tablero
COLS = ["sede", "anio", "mes", "tipo_estudio", "pacientes", "estudios", "referente_codigo", "especialidad_referente"]
INICIO_REGISTRO = "2023-07"  # antes: meses con 1-4 estudios, registro incompleto

d = json.load(open(sys.argv[1], encoding="utf-8"))
assert d["esquema"] == "hevesy/resumen-tablero@1", d["esquema"]
assert d["omitidas_por_privacidad"] == 0
assert set(d["sedes"]) <= set(SEDE), d["sedes"].keys()
tipo = lambda t: TIPO.get(t, t)
filas = []


def fila(sede, anio="", mes="", tipo_estudio="todos", pacientes="", estudios="", ref="", esp=""):
    filas.append(dict(zip(COLS, [sede, anio, mes, tipo_estudio, pacientes, estudios, ref, esp])))


def con_k(celdas):
    """celdas: lista de (sede, clave, n). Devuelve (visibles, otros_por_sede, residuo_global)."""
    vis, chicas = [], {}
    for s, c, n in celdas:
        if n >= K:
            vis.append((s, c, n))
        else:
            chicas[s] = chicas.get(s, 0) + n
    otros = {s: n for s, n in chicas.items() if n >= K}
    residuo = sum(n for s, n in chicas.items() if n < K)
    return vis, otros, residuo


# 1. Red y sedes: pacientes totales
fila("todas", pacientes=d["pacientes_total"])
for s, v in d["sedes"].items():
    assert v["pacientes"] >= K
    fila(SEDE[s], pacientes=v["pacientes"])

# 2. Red por tipo (pacientes con >= 1 estudio del tipo; estudios = paciente x tipo x mes)
for t, n in d["pacientes_por_tipo_estudio"].items():
    fila("todas", tipo_estudio=tipo(t), pacientes=n, estudios=d["estudios_por_tipo"][t])

# 3. Red por subtipo (tipo/subtipo)
vis, otros, residuo = con_k([("todas", tipo(k.split("/")[0]) + "/" + k.split("/")[1], n) for k, n in d["pacientes_por_subtipo"].items()])
if 0 < otros.get("todas", 0) + residuo < K:
    # Pocas celdas chicas (p. ej. renal/dtpa = 1): se suman a la celda visible más grande de su mismo tipo,
    # que pasa a llamarse «<tipo>/<subtipo>+otros/<5». Así ninguna celda de 1-4 queda sola.
    chicas = [(c, n) for c, n in ((tipo(k.split("/")[0]) + "/" + k.split("/")[1], n) for k, n in d["pacientes_por_subtipo"].items()) if n < K]
    for c, n in chicas:
        t = c.split("/")[0]
        i = max((j for j, v in enumerate(vis) if v[1].split("/")[0] == t), key=lambda j: vis[j][2])
        vis[i] = ("todas", vis[i][1].split("+")[0] + "+" + OTROS, vis[i][2] + n)
    otros, residuo = {}, 0
for _, c, n in vis:
    fila("todas", tipo_estudio=c, pacientes=n)
if otros.get("todas", 0) + residuo:
    assert otros.get("todas", 0) + residuo >= K
    fila("todas", tipo_estudio="subtipo/" + OTROS, pacientes=otros.get("todas", 0) + residuo)

# 4. Sede x tipo (pacientes)
vis, otros, residuo = con_k([(SEDE[s], tipo(t), n) for s, ts in d["sede_por_tipo"].items() for t, n in ts.items()])
for s, c, n in vis:
    fila(s, tipo_estudio=c, pacientes=n)
for s, n in otros.items():
    fila(s, tipo_estudio=OTROS, pacientes=n)
if residuo:
    assert residuo >= K
    fila(OTROS, tipo_estudio=OTROS, pacientes=residuo)

# 5. Sede x año del primer estudio (pacientes nuevos)
vis, otros, residuo = con_k([(SEDE[s], a, n) for s, an in d["sede_por_anio"].items() for a, n in an.items()])
for s, a, n in vis:
    fila(s, anio=a, pacientes=n)
for s, n in otros.items():
    fila(s, anio=OTROS, pacientes=n)
if residuo:
    assert residuo >= K
    fila(OTROS, anio=OTROS, pacientes=residuo)

# 6. Red por mes: estudios del mes y pacientes nuevos (primer estudio en el mes)
meses = sorted(set(d["estudios_por_mes"]) | set(d["pacientes_por_mes_primer_estudio"]))
pre_e = sum(d["estudios_por_mes"].get(m, 0) for m in meses if m < INICIO_REGISTRO)
pre_p = sum(d["pacientes_por_mes_primer_estudio"].get(m, 0) for m in meses if m < INICIO_REGISTRO)
assert pre_p >= K
fila("todas", anio="<" + INICIO_REGISTRO, pacientes=pre_p, estudios=pre_e)
for m in meses:
    if m < INICIO_REGISTRO:
        continue
    p, e = d["pacientes_por_mes_primer_estudio"].get(m, 0), d["estudios_por_mes"].get(m, 0)
    assert p >= K and e >= K, m
    fila("todas", anio=m[:4], mes=int(m[5:]), pacientes=p, estudios=e)

# 7. Referentes por código (k >= 5) y por especialidad
refs = d["referentes"]
for r in sorted(refs, key=lambda r: (-r["pacientes"], r["codigo"])):
    if r["pacientes"] >= K:
        fila("todas", pacientes=r["pacientes"], ref=r["codigo"], esp=r["especialidad"])
chicos = [r for r in refs if r["pacientes"] < K]
fila("todas", pacientes=sum(r["pacientes"] for r in chicos), ref=OTROS, esp="varias")
por_esp = {}
for r in refs:
    por_esp[r["especialidad"]] = por_esp.get(r["especialidad"], 0) + r["pacientes"]
vis, otros, residuo = con_k([("todas", e, n) for e, n in por_esp.items()])
for _, e, n in sorted(vis, key=lambda x: -x[2]):
    fila("todas", pacientes=n, ref="todos", esp=e)
if otros.get("todas", 0) + residuo:
    fila("todas", pacientes=otros.get("todas", 0) + residuo, ref="todos", esp=OTROS)

for f in filas:
    assert f["pacientes"] == "" or int(f["pacientes"]) >= K, f
with open(os.path.join(OUT, "real_inventario.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, COLS, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)

# Calidad y limitaciones del corte
o, est = d["ocr"], d["referentes_estado"]
ocr_txt = o.get("pdf_texto_ocr", 0)  # desde el corte 16-11-2026: escaneos leídos con OCR local
pdf = o["pdf_con_texto"] + ocr_txt + o["pdf_sin_ocr"]
desc = d["sedes"]["desconocida"]["pacientes"]
ff = d["fuente_fecha"]
cal = [
    ("fecha_corrida", "Fecha del corte del inventario", d["fecha_corrida"], "fecha", ""),
    ("pacientes_total", "Carpetas de paciente", d["pacientes_total"], "pacientes", ""),
    ("sede_desconocida", "Pacientes sin señal de sede", desc, "pacientes", "Ni el texto ni la ruta indican sede"),
    ("sede_desconocida_pct", "Pacientes sin señal de sede", round(desc / d["pacientes_total"] * 100, 1), "%", ""),
    ("sede_ambigua", "Pacientes con señales de varias sedes", d["sedes"]["ambigua"]["pacientes"], "pacientes", ""),
    ("sede_por_texto", "Sede detectada por el texto del informe", d["fuente_sede"]["texto"], "pacientes", ""),
    ("sede_por_ruta", "Sede detectada por la ruta de la carpeta", d["fuente_sede"]["ruta"], "pacientes", ""),
    ("pdf_sin_ocr", "PDF sin texto extraíble (escaneos sin OCR)", o["pdf_sin_ocr"], "archivos", "Pueden subestimar tipos y referentes"),
    ("pdf_con_texto", "PDF con capa de texto", o["pdf_con_texto"], "archivos", ""),
    ("pdf_texto_ocr", "Escaneos leídos con OCR local", ocr_txt, "archivos", "OCR en la PC del propietario; puede tener errores de lectura"),
    ("pdf_sin_ocr_pct", "PDF sin texto extraíble", round(o["pdf_sin_ocr"] / pdf * 100, 1), "% de los PDF", ""),
    ("ref_con_referente", "Pacientes con referente detectado", est["con_referente"], "pacientes", ""),
    ("ref_no_detectado", "Pacientes con texto pero sin referente detectado", est["no_detectado"], "pacientes", ""),
    ("ref_sin_ocr", "Pacientes cuyo referente no se pudo leer (sin OCR)", est["sin_ocr"], "pacientes", ""),
    ("ref_sin_documentos", "Pacientes sin documentos legibles", est["sin_documentos"], "pacientes", ""),
    ("ref_codigos", "Códigos de referente distintos", len(refs), "referentes", ""),
    ("ref_codigos_k5", "Referentes con 5 o más pacientes (se muestran)", sum(1 for r in refs if r["pacientes"] >= K), "referentes", ""),
    ("ref_codigos_otros", "Referentes con menos de 5 pacientes (en «otros/<5»)", len(chicos), "referentes", ""),
    ("ref_firmantes_no_excluidos", "Firmantes propios de la unidad excluidos de referentes", "no", "estado",
     "Falta aplicar firmantes_sugeridos.txt: los códigos más frecuentes pueden ser médicos de la unidad"),
    ("esp_no_detectada_pct", "Pacientes referidos cuyo referente no tiene especialidad detectada",
     round(por_esp.get("no_detectada", 0) / sum(por_esp.values()) * 100, 1), "%", ""),
    ("fecha_por_archivo_pct", "Estudios fechados por la fecha del archivo (no del informe)",
     round(ff["fecha_archivo"] / sum(ff.values()) * 100, 1), "%", "La fecha de archivo puede ser la de copia o edición"),
    ("meses_registro_incompleto", "Meses anteriores a 2023-07 con 1 a 4 estudios (registro incompleto)",
     sum(1 for m in d["estudios_por_mes"] if m < INICIO_REGISTRO), "meses", "Sumados en una fila «<2023-07»"),
    ("mes_parcial", "Mes en curso al corte (parcial)", max(d["estudios_por_mes"]), "mes", "Hasta el día del corte"),
]
with open(os.path.join(OUT, "real_inventario_calidad.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(["indicador_id", "indicador", "valor", "unidad", "nota"])
    w.writerows(cal)
print(len(filas), "filas;", len(cal), "indicadores de calidad")
