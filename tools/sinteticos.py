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

# Calibración a la escala REAL del inventario de expedientes (HEVESY, corte 15-11-2026; dashboard/data/real_inventario.csv):
# la red hace ≈ 65–75 estudios/mes en 2026 (enero a octubre: 75.5/mes), con OAX > VHSA1 > MID. Objetivo sintético:
# promedio de estudios/mes en enero–octubre 2026 por sede (≈ 72 en la red, repartido como los pacientes nuevos 2026 con
# sede conocida: OAX 57 %, VHSA1 31 %, MID 12 %) y crecimiento 2025→2026 del promedio mensual (real anualizado:
# OAX +31.9 %, VHSA1 +181.5 %, MID +24.5 %). Lu-177 y PET-CT no se ofrecen en ninguna sede operando.
OBJETIVO_2026 = {"OAX": 41.0, "VHSA1": 22.0, "MID": 9.0}   # estudios/mes, promedio enero–octubre 2026
CRECE_25_26 = {"OAX": 0.32, "VHSA1": 1.80, "MID": 0.25}    # promedio mensual ene–oct 2026 ÷ promedio 2025 − 1
# Mezcla por sede (pacientes reales con ≥ 1 estudio de cada familia): gammagrafía / yodo-131.
GAMMA_PCT = {"OAX": 0.67, "VHSA1": 0.58, "MID": 0.50}
# Dentro de cada familia, la mezcla real de la red (estudios): gammagrafía 1 166 = ósea 630, tiroidea 337, renal 104,
# paratiroides 49, otras 34, perfusión 12; yodo-131 950 = rastreo 606, terapia 344.
MEZCLA_GAMMA = {"gammagrafia_osea": 630, "tiroidea": 337, "renal": 104, "paratiroides": 49, "otras": 34, "perfusion_miocardica": 12}
MEZCLA_YODO = {"rastreo_i131": 606, "terapia_i131": 344}
ESTACIONAL = {1: 0.95, 4: 0.92, 7: 0.95, 12: 0.88}  # enero, Semana Santa, vacaciones, diciembre


def tasa_mensual(g):
    """Tasa mensual compuesta r tal que el promedio ene–oct 2026 ÷ promedio 2025 = 1 + g (sin estacionalidad)."""
    lo, hi = 0.0, 0.5
    for _ in range(80):
        r = (lo + hi) / 2
        a25 = sum((1 + r) ** k for k in range(12)) / 12
        a26 = sum((1 + r) ** k for k in range(12, 22)) / 10
        lo, hi = (r, hi) if a26 / a25 < 1 + g else (lo, r)
    return r


CRECIMIENTO = {s: tasa_mensual(g) for s, g in CRECE_25_26.items()}  # mensual compuesto
NIVEL = {s: OBJETIVO_2026[s] / (sum((1 + CRECIMIENTO[s]) ** k for k in range(12, 22)) / 10) for s in OBJETIVO_2026}
BASE = {s: {**{t: GAMMA_PCT[s] * n / sum(MEZCLA_GAMMA.values()) for t, n in MEZCLA_GAMMA.items()},
            **{t: (1 - GAMMA_PCT[s]) * n / sum(MEZCLA_YODO.values()) for t, n in MEZCLA_YODO.items()}, "lu177": 0}
        for s in OBJETIVO_2026}  # fracción de los estudios de la sede por tipo
TARIFA = {"gammagrafia_osea": 5200, "tiroidea": 3800, "renal": 4500, "rastreo_i131": 7500, "terapia_i131": 42000,
          "lu177": 145000, "perfusion_miocardica": 9500, "paratiroides": 5500, "otras": 4500}
SIN_REFERENTE = {"otras": 0.30}  # fracción de pacientes sin referente registrado; resto 0.20

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
POOL = {"MID": 25, "VHSA1": 40, "OAX": 70}  # referentes propios por sede (real: 439 códigos en 1 703 pacientes)
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
tipos_sede = [t for t in TIPOS if t != "lu177"]
arrastre = {s: [0.0] * len(tipos_sede) for s in BASE}
for sede, base in BASE.items():
    for i, mes in enumerate(MESES):
        m = int(mes[5:])
        total = NIVEL[sede] * (1 + CRECIMIENTO[sede]) ** i * ESTACIONAL.get(m, 1.0) * rng.gauss(1, 0.05)
        total = max(1, round(total))
        # reparto por mayor residuo con arrastre entre meses: la mezcla acumulada sigue a BASE aunque los conteos sean chicos
        cuota = [arrastre[sede][j] + total * base[t] for j, t in enumerate(tipos_sede)]
        cuenta = [int(q) for q in cuota]
        for j in sorted(range(len(cuota)), key=lambda j: (cuota[j] - cuenta[j], rng.random()), reverse=True)[:total - sum(cuenta)]:
            cuenta[j] += 1
        arrastre[sede] = [q - c for q, c in zip(cuota, cuenta)]
        for tipo, est in zip(tipos_sede, cuenta):
            if not est:
                continue
            pac = max(1, min(est, round(est / rng.uniform(1.0, 1.08))))
            sin = round(pac * SIN_REFERENTE.get(tipo, 0.20))
            elig = [r for r in referentes[sede] if r[1] in ESPECIALIDADES[tipo]]
            reparto = multinomial(pac - sin, [r[2] for r in elig])
            filas = [[sede, mes[:4], str(m), tipo, p, p, r[0], r[1]] for r, p in zip(elig, reparto) if p]
            if sin:
                filas.append([sede, mes[:4], str(m), tipo, sin, sin, "", ""])
            # estudios proporcionales a pacientes, conservando el total
            for k in range(est - sum(f[5] for f in filas)):
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
    # Conversiones bajas: un estudio de medicina nuclear requiere orden médica, así que la pauta atrae sobre todo
    # consultas; calibrado para que los canales atribuyan ≈ 1/3 de los ≈ 40–50 pacientes nuevos/mes de la red real.
    "Meta (Facebook/Instagram)": (17000, 42, 0.011, 0.008, 0.12, 0.60, 0.42, "2025-01"),
    "Google (Search/PMax)": (32000, 440, 0.045, 0.025, 0.12, 0.60, 0.45, "2025-01"),
    "TikTok": (3000, 15, 0.007, 0.003, 0.08, 0.50, 0.55, "2026-03"),
    "LinkedIn": (11000, 210, 0.006, 0.020, 0.10, 0.40, 0.50, "2025-04"),
    "YouTube": (6500, 26, 0.003, 0.006, 0.10, 0.50, 0.48, "2025-02"),
    "WhatsApp Business": (3000, None, None, 0.37, 0.30, 0.70, None, "2025-01"),
}
can = []
for i, mes in enumerate(MESES):
    m = int(mes[5:])
    for canal, (g, cpm, ctr, lc, cl, pc, ap, ini) in CANAL.items():
        if mes < ini:
            continue
        gasto = int(round(g * (1 + 0.008 * i) * rng.gauss(1, 0.06), -1))
        if canal == "WhatsApp Business":
            conversaciones = round(60 * (1 + 0.03 * i) * ESTACIONAL.get(m, 1) * rng.gauss(1, 0.07))
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
RES = {"MID": ("GAMMA Mérida", 45, 4.7), "VHSA1": ("GAMMA Villahermosa sede 1", 70, 4.6),
       "OAX": ("GAMMA Oaxaca", 130, 4.5)}
res = []
for sede, (nombre, n, cal) in RES.items():
    pos = round(rng.uniform(2.4, 7.0), 1)
    res.append({"sede": sede, "nombre": nombre, "resenas_google": n + rng.randint(-10, 20),
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
                 "referencias_atribuidas": round(nuevos * rng.uniform(0.5, 1.2)),
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
    "trafico_organico": f"{rng.randint(1500, 3000)} sesiones (red, {ult})",
    "seo_localpack": f"{sum(r['local_pack_top3'] == 'Sí' for r in res)} de {len(res)} sedes operando",
    "costo_paciente": f"{round(pauta / max(1, sum(r['pacientes'] for r in can_u if r['canal'] != 'WhatsApp Business')))} MXN",
    "inversion_vs_presupuesto": f"{round(pauta / 1000)} k MXN/mes",
    "convenios_aseguradoras": str(rng.randint(3, 6)),
}
w("sintetico_kpis.csv", ["kpi_id", "valor_sintetico"], [[k, v] for k, v in kp.items()])

print(f"inventario: {len(inv)} filas · plazas: {len(plazas)} · canales: {len(can)} · semilla {SEMILLA}")
