"""Genera los datos SINTÉTICOS (no reales) del tablero MarCo.

Uso:  python3 tools/sinteticos.py            (escribe dashboard/data/sintetico_*.csv)

Semilla fija (SEMILLA) para que cada corrida produzca exactamente los mismos archivos.
Supuestos documentados en dashboard/data/SUPUESTOS_SINTETICOS.md. Nada de lo que escribe
este script es un dato real: no proviene de expedientes, CRM, agenda ni plataformas.
No genera nombres de pacientes ni de médicos: los referentes son códigos R-001, R-002…
"""
import csv
import os
import random

SEMILLA = 20261115
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dashboard", "data")
rng = random.Random(SEMILLA)

MESES = [f"{a}-{m:02d}" for a in (2025, 2026) for m in range(1, 13)][:22]  # 2025-01 … 2026-10
TIPOS = ["gammagrafia_osea", "tiroidea", "renal", "rastreo_i131", "terapia_i131", "lu177",
         "perfusion_miocardica", "paratiroides", "otras"]

# Sedes sin actividad antes de su apertura (decisión del propietario, 15-nov-2026): no generan filas.
# VHSA2 (Villahermosa sede 2, en el CINO con el aliado estratégico) abre a fines de 2027; TOL y COL, próxima apertura.
PROXIMA_APERTURA = {"VHSA2": "fines 2027", "TOL": "por definir", "COL": "por definir"}

# Estudios al mes en la base (enero 2025, ya en régimen) por sede operando y tipo. Lu-177 y PET-CT no se
# ofrecen en ninguna sede operando, así que no aparecen en la muestra.
BASE = {
    "MID":   {"gammagrafia_osea": 110, "tiroidea": 45, "renal": 40, "rastreo_i131": 14, "terapia_i131": 10, "lu177": 0, "perfusion_miocardica": 45, "paratiroides": 12, "otras": 25},
    "VHSA1": {"gammagrafia_osea": 85, "tiroidea": 40, "renal": 30, "rastreo_i131": 12, "terapia_i131": 9, "lu177": 0, "perfusion_miocardica": 30, "paratiroides": 10, "otras": 18},
    "OAX":   {"gammagrafia_osea": 70, "tiroidea": 35, "renal": 25, "rastreo_i131": 10, "terapia_i131": 8, "lu177": 0, "perfusion_miocardica": 18, "paratiroides": 8, "otras": 15},
}
CRECIMIENTO = {"MID": 0.012, "VHSA1": 0.010, "OAX": 0.009}  # mensual compuesto
ESTACIONAL = {1: 0.95, 4: 0.92, 7: 0.95, 12: 0.88}  # enero, Semana Santa, vacaciones, diciembre
TARIFA = {"gammagrafia_osea": 5200, "tiroidea": 3800, "renal": 4500, "rastreo_i131": 7500, "terapia_i131": 42000,
          "lu177": 145000, "perfusion_miocardica": 9500, "paratiroides": 5500, "otras": 4500}
SIN_REFERENTE = {"otras": 0.25}  # fracción de pacientes sin referente registrado; resto 0.12

ESPECIALIDADES = {
    "gammagrafia_osea": ["Oncología médica", "Cirugía oncológica", "Urología", "Ortopedia", "Medicina interna"],
    "tiroidea": ["Endocrinología", "Medicina interna", "Cirugía oncológica", "Medicina familiar"],
    "renal": ["Urología", "Nefrología", "Pediatría"],
    "rastreo_i131": ["Endocrinología", "Cirugía oncológica"],
    "terapia_i131": ["Endocrinología", "Cirugía oncológica"],
    "lu177": ["Oncología médica", "Urología"],
    "perfusion_miocardica": ["Cardiología", "Medicina interna"],
    "paratiroides": ["Endocrinología", "Cirugía oncológica"],
    "otras": ["Oncología médica", "Medicina interna", "Hematología", "Neurología", "Medicina familiar"],
}
PESO_ESP = {"Oncología médica": 9, "Cirugía oncológica": 6, "Endocrinología": 9, "Urología": 7, "Cardiología": 6,
            "Nefrología": 3, "Medicina interna": 10, "Ortopedia": 4, "Pediatría": 3, "Medicina familiar": 6,
            "Hematología": 2, "Neurología": 2}
POOL = {"MID": 70, "VHSA1": 55, "OAX": 45}  # referentes propios por sede
assert not set(BASE) & set(PROXIMA_APERTURA), "una sede de próxima apertura no tiene actividad"


def w(path, cols, rows):
    with open(os.path.join(OUT, path), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(cols)
        for r in rows:
            wr.writerow([r.get(c, "") if isinstance(r, dict) else r[i] for i, c in enumerate(cols)])


def multinomial(n, pesos):
    tot = sum(pesos)
    out = [0] * len(pesos)
    for _ in range(n):
        x = rng.random() * tot
        acc = 0
        for i, p in enumerate(pesos):
            acc += p
            if x <= acc:
                out[i] += 1
                break
    return out


# ---------- referentes (códigos, sin nombres) ----------
esp_nombres = list(PESO_ESP)
codigo = 0
referentes = {}  # sede -> list of (codigo, especialidad, peso)
for sede in BASE:
    lista = []
    for _ in range(POOL[sede]):
        codigo += 1
        esp = rng.choices(esp_nombres, weights=[PESO_ESP[e] for e in esp_nombres])[0]
        lista.append((f"R-{codigo:03d}", esp, 1 / ((rng.randint(1, POOL[sede]) + 3) ** 0.8)))
    referentes[sede] = lista

# ---------- inventario sintético (mismo esquema que real_inventario.csv) ----------
inv = []
for sede, base in BASE.items():
    for i, mes in enumerate(MESES):
        m = int(mes[5:])
        for tipo in TIPOS:
            b = base[tipo]
            if not b:
                continue
            est = b * (1 + CRECIMIENTO[sede]) ** i * ESTACIONAL.get(m, 1.0) * rng.gauss(1, 0.08)
            est = max(0, round(est))
            if not est:
                continue
            pac = max(1, min(est, round(est / rng.uniform(1.0, 1.08))))
            sin = round(pac * SIN_REFERENTE.get(tipo, 0.12))
            elig = [r for r in referentes[sede] if r[1] in ESPECIALIDADES[tipo]]
            reparto = multinomial(pac - sin, [r[2] for r in elig])
            asignado_est = 0
            filas = []
            for r, p in zip(elig, reparto):
                if p:
                    filas.append([sede, mes[:4], str(m), tipo, p, 0, r[0], r[1]])
            if sin:
                filas.append([sede, mes[:4], str(m), tipo, sin, 0, "", ""])
            # estudios proporcionales a pacientes, conservando el total
            for f in filas:
                f[5] = f[4]
                asignado_est += f[4]
            extra = est - asignado_est
            for k in range(extra):
                filas[k % len(filas)][5] += 1
            inv.extend(filas)
COLS_INV = ["sede", "anio", "mes", "tipo_estudio", "pacientes", "estudios", "referente_codigo", "especialidad_referente"]
w("sintetico_inventario.csv", COLS_INV, inv)

# ---------- conversión e ingresos por sede y mes ----------
plazas = []
for sede in BASE:
    for mes in MESES:
        filas = [r for r in inv if r[0] == sede and f"{r[1]}-{int(r[2]):02d}" == mes]
        refer = sum(r[4] for r in filas if r[6])
        conv = min(92.0, max(65.0, rng.gauss(79, 4)))
        ingresos = sum(r[5] * TARIFA[r[3]] for r in filas)
        plazas.append({"sede": sede, "mes": mes, "referencias_recibidas": round(refer / (conv / 100)),
                       "conversion_pct": round(conv, 1), "ingresos_mxn": int(round(ingresos * rng.gauss(1, 0.03), -3))})
w("sintetico_plazas_mensual.csv", ["sede", "mes", "referencias_recibidas", "conversion_pct", "ingresos_mxn"], plazas)

# ---------- canales (red completa) ----------
CANAL = {  # gasto base MXN/mes, CPM, CTR, lead/clic, cita/lead, paciente/cita, alcance/impresión, inicio
    "Meta (Facebook/Instagram)": (17000, 42, 0.011, 0.026, 0.30, 0.75, 0.42, "2025-01"),
    "Google (Search/PMax)": (32000, 440, 0.045, 0.090, 0.38, 0.80, 0.45, "2025-01"),
    "TikTok": (3000, 15, 0.007, 0.010, 0.22, 0.65, 0.55, "2026-03"),
    "LinkedIn": (11000, 210, 0.006, 0.060, 0.30, 0.60, 0.50, "2025-04"),
    "YouTube": (6500, 26, 0.003, 0.020, 0.25, 0.70, 0.48, "2025-02"),
    "WhatsApp Business": (3000, None, None, 0.37, 0.50, 0.80, None, "2025-01"),
}
can = []
for i, mes in enumerate(MESES):
    m = int(mes[5:])
    for canal, (g, cpm, ctr, lc, cl, pc, ap, ini) in CANAL.items():
        if mes < ini:
            continue
        gasto = int(round(g * (1 + 0.008 * i) * rng.gauss(1, 0.06), -1))
        if canal == "WhatsApp Business":
            conversaciones = round(1100 * (1 + 0.015 * i) * ESTACIONAL.get(m, 1) * rng.gauss(1, 0.07))
            alcance = round(conversaciones * 1.3)
            imp = round(conversaciones * 3.6)
            clics = conversaciones
        else:
            imp = round(gasto / cpm * 1000 * rng.gauss(1, 0.05))
            clics = round(imp * ctr * rng.gauss(1, 0.06))
            alcance = round(imp * ap)
        leads = round(clics * lc * ESTACIONAL.get(m, 1) * rng.gauss(1, 0.08))
        citas = round(leads * cl * rng.gauss(1, 0.06))
        pac = round(citas * pc * rng.gauss(1, 0.05))
        can.append({"mes": mes, "canal": canal, "alcance": alcance, "impresiones": imp, "clics": clics,
                    "gasto_mxn": gasto, "leads": leads, "citas": citas, "pacientes": pac})
w("sintetico_canales_mensual.csv", ["mes", "canal", "alcance", "impresiones", "clics", "gasto_mxn", "leads", "citas", "pacientes"], can)

# ---------- reseñas, NPS y SEO por sede ----------
RES = {"MID": ("GAMMA Mérida", 380, 4.7), "VHSA1": ("GAMMA Villahermosa sede 1", 260, 4.6),
       "OAX": ("GAMMA Oaxaca", 190, 4.5)}
res = []
for sede, (nombre, n, cal) in RES.items():
    pos = round(rng.uniform(2.4, 7.0), 1)
    res.append({"sede": sede, "nombre": nombre, "resenas_google": n + rng.randint(-20, 40),
                "calificacion_google": round(min(4.9, cal + rng.uniform(-0.1, 0.1)), 1),
                "nps_pacientes": rng.randint(60, 76), "nps_referentes": rng.randint(48, 64),
                "posicion_media_seo": pos, "local_pack_top3": "Sí" if pos < 4.5 else "No"})
w("sintetico_resenas_seo.csv", ["sede", "nombre", "resenas_google", "calificacion_google", "nps_pacientes",
                                "nps_referentes", "posicion_media_seo", "local_pack_top3"], res)

# ---------- resultados de congresos concluidos ----------
cong = []
for cid, base_c, costo in (("ANCAM-2026", 80, 60000), ("SMEO-2026", 140, 120000), ("SMNE-2026", 120, 110000)):
    contactos = round(base_c * rng.gauss(1, 0.1))
    nuevos = max(5, round(contactos * rng.uniform(0.07, 0.12)))
    cong.append({"congreso_id": cid, "contactos": contactos, "referentes_nuevos": nuevos,
                 "referencias_atribuidas": round(nuevos * rng.uniform(1.4, 2.6)),
                 "costo_mxn": int(round(costo * rng.gauss(1, 0.08), -3))})
w("sintetico_congresos.csv", ["congreso_id", "contactos", "referentes_nuevos", "referencias_atribuidas", "costo_mxn"], cong)

# ---------- KPIs (último mes, red completa) ----------
ult = MESES[-1]
inv_u = [r for r in inv if f"{r[1]}-{int(r[2]):02d}" == ult]
can_u = [r for r in can if r["mes"] == ult]
pauta = sum(r["gasto_mxn"] for r in can_u if r["canal"] != "WhatsApp Business")
kp = {
    "referencias_mes": f"{sum(r[4] for r in inv_u if r[6])} (red, {ult})",
    "referentes_activos": f"{len({r[6] for r in inv_u if r[6]})} (red, {ult})",
    "conversion": f"{round(sum(p['conversion_pct'] for p in plazas if p['mes'] == ult) / len(BASE), 1)} %",
    "sla_respuesta": f"{rng.randint(78, 90)} %",
    "nps_pacientes": str(round(sum(r["nps_pacientes"] for r in res) / len(res))),
    "nps_referentes": str(round(sum(r["nps_referentes"] for r in res) / len(res))),
    "trafico_organico": f"{rng.randint(8500, 12500)} sesiones (red, {ult})",
    "seo_localpack": f"{sum(r['local_pack_top3'] == 'Sí' for r in res)} de {len(res)} sedes operando",
    "costo_paciente": f"{round(pauta / max(1, sum(r['pacientes'] for r in can_u if r['canal'] != 'WhatsApp Business')))} MXN",
    "inversion_vs_presupuesto": f"{round(pauta / 1000)} k MXN/mes",
    "convenios_aseguradoras": str(rng.randint(3, 6)),
}
w("sintetico_kpis.csv", ["kpi_id", "valor_sintetico"], [[k, v] for k, v in kp.items()])

print(f"inventario: {len(inv)} filas · plazas: {len(plazas)} · canales: {len(can)} · semilla {SEMILLA}")
