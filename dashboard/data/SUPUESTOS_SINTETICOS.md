# Datos SINTÉTICOS del tablero MarCo — supuestos

> **SINTÉTICO — no real.** Ninguna cifra de los archivos `sintetico_*.csv` proviene de expedientes, agenda, CRM, plataformas de anuncios ni encuestas. Sirven para ver cómo se leerá el tablero con datos y para dimensionar el plan. **No se citan ni se usan en piezas, informes externos ni decisiones de inversión.**

Instrucción del propietario (15-nov-2026): poblar todas las métricas de desempeño con datos sintéticos rotulados y preparar el esquema de los datos reales del inventario de expedientes (HEVESY). Es la excepción **oficial** a la regla «nada inventado» de `AGENTS.md` § 4 (propietario, 15-11-2026): aplica sólo a estos archivos, siempre con la etiqueta «SINTÉTICO — no real», con semilla y supuestos documentados aquí, sin mezclarse con datos reales sin insignia de origen, y nunca a `kpis.csv`, `presupuesto_canal.csv`, `sedes.csv` ni a las plantillas reales, que siguen vacías.

## Cómo se generan

- Script: `tools/sinteticos.py`, **semilla fija 20261115** (`random.Random`). Correrlo de nuevo produce archivos idénticos.
- Periodo: enero 2025 a octubre 2026 (22 meses; octubre es el último mes cerrado).
- Sedes con datos sintéticos: sólo las operando, MID, VHSA1 y OAX. Villahermosa sede 2 en el CINO (VHSA2, **próxima apertura, fines de 2027**), Toluca (TOL) y Colima (COL) son «próxima apertura»: **sin filas**, porque una sede no tiene actividad antes de abrir (`PROXIMA_APERTURA` en el script; una aserción impide generar filas para ellas).
- Sin nombres de pacientes ni de médicos. Los referentes son códigos `R-001…`; cada código tiene una especialidad.

## Supuestos por métrica

| Métrica | Supuesto |
|---|---|
| Estudios por sede y tipo | **Calibrados a la escala real** del inventario de expedientes (corte 15-11-2026, `real_inventario.csv`). Promedio de estudios/mes en enero–octubre 2026: Oaxaca 41, Villahermosa sede 1 22, Mérida 9 (red ≈ 72; real ≈ 65–75, ene–oct 75.5), repartido como los pacientes nuevos 2026 con sede conocida (OAX > VHSA1 > MID). Crecimiento compuesto mensual resuelto para que el promedio ene–oct 2026 ÷ promedio 2025 sea el real anualizado: OAX +32 %, VHSA1 +180 %, MID +25 %. Estacionalidad: enero −5 %, abril −8 %, julio −5 %, diciembre −12 %. Ruido normal σ = 5 % sobre el total mensual de la sede. |
| Mezcla de estudios | Por sede, gammagrafía / yodo-131 como en los pacientes reales: OAX 67/33, VHSA1 58/42, MID 50/50. Dentro de cada familia, la mezcla real de la red: ósea 54 %, tiroidea 29 %, renal 9 %, paratiroides 4 %, otras 3 %, perfusión 1 %; rastreo I-131 64 %, terapia I-131 36 %. Reparto por mayor residuo con arrastre entre meses (los conteos son chicos). **Sin Lu-177 ni PET-CT**: sólo se ofrecerán en VHSA2, que aún no abre. |
| VHSA2 (CINO) | Próxima apertura (fines de 2027): sin actividad sintética en el periodo. La versión anterior le daba actividad desde 2025 por error; se regeneró el 15-11-2026. |
| Pacientes | Estudios ÷ U(1.00, 1.08): algunos pacientes tienen más de un estudio en el mes. |
| Referencias | 20 % de pacientes sin referente registrado (30 % en «otras»); el resto se reparte entre referentes de especialidades afines al estudio con pesos tipo Zipf, 1 / (rango + 3)^0.8. Pools: OAX 70, VHSA1 40, MID 25 referentes (real: 439 códigos en 1 703 pacientes). |
| Conversión de referencia | Normal(79 %, 4 pp), acotada a 65–92 %. Referencias recibidas = referidos atendidos ÷ conversión. |
| Ingresos (plantilla) | Estudios × tarifa supuesta (MXN): ósea 5,200; tiroidea 3,800; renal 4,500; perfusión 9,500; paratiroides 5,500; rastreo I-131 7,500; terapia I-131 42,000; Lu-177 145,000 por ciclo (sin uso mientras VHSA2 no abra); otras 4,500. Ruido σ = 3 %. **No son tarifas de GAMMA.** Con la escala real: ≈ 0.75 M MXN/mes en la red en 2026; terapias I-131 ≈ 10/mes (36 % del yodo-131). |
| Canales | Gasto mensual dentro del rango del plan (`presupuesto_canal.csv`): Google ≈ 32 k, Meta ≈ 17 k, LinkedIn ≈ 11 k (desde abr-2025), YouTube ≈ 6.5 k (desde feb-2025), TikTok ≈ 3 k (piloto desde mar-2026), WhatsApp Business ≈ 3 k (herramienta); +0.8 % mensual. CPM y CTR sin cambio (Google 440 / 4.5 %, Meta 42 / 1.1 %, TikTok 15 / 0.7 %, LinkedIn 210 / 0.6 %, YouTube 26 / 0.3 %). **Conversión recalibrada a la escala real**: un estudio requiere orden médica, así que lead/clic Google 2.5 %, LinkedIn 2 %, Meta 0.8 %, YouTube 0.6 %, TikTok 0.3 %; cita/lead 8–12 %; paciente/cita 40–60 %. Resultado: los canales atribuyen ≈ 15–20 pacientes/mes, ≈ 1/3 de los ≈ 40–50 pacientes nuevos/mes reales; CPA ≈ 7 000 MXN. |
| WhatsApp | Sólo logística. «Impresiones» = mensajes entregados; «clics» = conversaciones iniciadas (≈ 60/mes en ene-2025, +3 % mensual); «leads» = solicitudes de agenda (37 % de conversaciones). |
| Embudo | Suma de canales del último mes: impresiones → clics → leads → citas → estudios (pacientes atribuidos). |
| CPL / CPA | Se calculan en el tablero: CPL = gasto ÷ leads; CPA (costo por paciente) = gasto ÷ pacientes atribuidos. |
| Reseñas, NPS y SEO | Reseñas Google proporcionales al volumen real: OAX ≈ 130–150, VHSA1 ≈ 60–90, MID ≈ 35–65; calificación 4.4–4.9; NPS pacientes 60–76; NPS referentes 48–64; posición media SEO 2.4–7.0; top-3 local si la posición < 4.5. Tráfico orgánico 1 500–3 000 sesiones/mes. |
| Congresos | Sólo congresos concluidos del calendario (ANCAM, SMeO y SMNE 2026): contactos, referentes nuevos (7–12 % de contactos), referencias atribuidas (0.5–1.2 por referente nuevo, acorde con ≈ 40–50 pacientes nuevos/mes en la red) y costo total (asistencia/stand). |
| KPIs | Valor sintético del último mes para los KPIs de desempeño. Cumplimiento COFEPRIS e incidentes de privacidad **no** tienen valor sintético: sólo se muestran con dato real. |

## Datos reales del inventario de expedientes (HEVESY)

**Primer corte: 15-11-2026** (`REAL — inventario expedientes 15-11-2026`). HEVESY corrió en la PC del propietario y entregó sólo un resumen agregado (`resumen_tablero.json`, esquema `hevesy/resumen-tablero@1`: vocabulario cerrado, conteos y códigos `R-###`; sin nombres, CURP, folios, fechas de nacimiento ni texto libre; verificado antes de usarlo). `tools/real_inventario.py <ruta>/resumen_tablero.json` escribe:

- `real_inventario.csv` — mismo encabezado que `sintetico_inventario.csv`, pero el corte **no trae el cruce completo** sede × mes × tipo × referente. Por eso el archivo contiene tablas marginales, distinguibles por qué columnas están llenas:

| Tabla | `sede` | `anio` | `mes` | `tipo_estudio` | `referente_codigo` | `pacientes` / `estudios` |
|---|---|---|---|---|---|---|
| Total red / por sede | `todas` / sede | — | — | `todos` | — | pacientes |
| Red × tipo | `todas` | — | — | tipo | — | pacientes con ≥ 1 estudio del tipo / estudios (paciente × tipo × mes) |
| Red × subtipo | `todas` | — | — | `tipo/subtipo` | — | pacientes |
| Sede × tipo | sede | — | — | tipo | — | pacientes |
| Sede × año | sede | aaaa | — | `todos` | — | pacientes nuevos (año del primer estudio) |
| Red × mes | `todas` | aaaa (o `<2023-07`) | 1–12 | `todos` | — | pacientes nuevos / estudios |
| Referentes | `todas` | — | — | `todos` | `R-###` u `otros/<5` | pacientes |
| Especialidades | `todas` | — | — | `todos` | `todos` | pacientes (suma por especialidad) |

- Sedes: `merida` → `MID`, `villahermosa_sede1_gamma` → `VHSA1`, `oaxaca` → `OAX`; `desconocida` y `ambigua` se conservan. Tipo `osea` → `gammagrafia_osea`.
- **k ≥ 5**: ninguna celda con 1–4 pacientes se escribe sola. Se suman en `otros/<5` dentro de su sede; si esa suma sigue < 5, en una fila `sede = otros/<5`. Referentes con < 5 pacientes van en `R` = `otros/<5` (416 de 439 códigos). La prueba `test_inventario_real_esquema` exige `pacientes ≥ 5` en cada fila.
- Meses anteriores a 2023-07 (1–4 estudios cada uno): **registro incompleto**, sumados en una fila `anio = <2023-07`.
- `real_inventario_calidad.csv` — limitaciones del corte: 645 de 1 703 pacientes (37.9 %) con sede «desconocida»; 5 121 PDF sin texto (sin OCR, 51 % de los PDF), que pueden subestimar tipos y referentes; 70 % de los estudios fechados por la fecha del archivo; noviembre de 2026 parcial.

En el tablero: la pestaña «Estudios y referencias» y las cifras de estudios y pacientes del resumen son REAL; «Plazas» (sede × mes), terapias por mes, conversión e ingresos siguen SINTÉTICO — no real, porque el corte no los trae. Una fila real sólo sustituye al sintético de su sede si tiene grano completo (sede operando, año, mes y tipo). Desde el 15-11-2026 los sintéticos están **recalibrados a esa escala real** (≈ 72 estudios/mes en la red en 2026, mezcla y crecimiento por sede); siguen siendo SINTÉTICO — no real y no sustituyen al dato.

Nota: el contrato `gamma/referencia@2` (`contracts/schemas/`, PR #1 de `gamma-contracts`) usa los mismos códigos de sede que el tablero; el borrador `@1` usaba VSA y CINO, alias obsoletos de VHSA1 y VHSA2.
