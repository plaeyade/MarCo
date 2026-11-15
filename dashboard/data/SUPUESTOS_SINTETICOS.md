# Datos SINTÉTICOS del tablero MarCo — supuestos

> **SINTÉTICO — no real.** Ninguna cifra de los archivos `sintetico_*.csv` proviene de expedientes, agenda, CRM, plataformas de anuncios ni encuestas. Sirven para ver cómo se leerá el tablero con datos y para dimensionar el plan. **No se citan ni se usan en piezas, informes externos ni decisiones de inversión.**

Instrucción del propietario (15-nov-2026): poblar todas las métricas de desempeño con datos sintéticos rotulados y preparar el esquema de los datos reales del inventario de expedientes (HEVESY). Es una excepción acotada a la regla «nada inventado» de `AGENTS.md` § 4: aplica sólo a estos archivos, siempre con la etiqueta «SINTÉTICO — no real», y nunca a `kpis.csv`, `presupuesto_canal.csv`, `sedes.csv` ni a las plantillas reales, que siguen vacías.

## Cómo se generan

- Script: `tools/sinteticos.py`, **semilla fija 20261115** (`random.Random`). Correrlo de nuevo produce archivos idénticos.
- Periodo: enero 2025 a octubre 2026 (22 meses; octubre es el último mes cerrado).
- Sedes con datos sintéticos: MID, VHSA1, VHSA2, OAX. Toluca (TOL) y Colima (COL) son «próxima apertura»: sin filas.
- Sin nombres de pacientes ni de médicos. Los referentes son códigos `R-001…`; cada código tiene una especialidad.

## Supuestos por métrica

| Métrica | Supuesto |
|---|---|
| Estudios por sede y tipo | Base mensual (ene-2025) en régimen: Mérida ≈ 300, Villahermosa sede 1 ≈ 235, Villahermosa sede 2 (CINO) ≈ 240, Oaxaca ≈ 190. Capacidad de una gammacámara ≈ 10–15 estudios/día. Crecimiento compuesto 0.9–1.5 % mensual. Estacionalidad: enero −5 %, abril −8 % (Semana Santa), julio −5 %, diciembre −12 %. Ruido normal σ = 8 %. |
| Mezcla de estudios | Gammagrafía ósea es el estudio más frecuente; luego tiroidea, renal y perfusión miocárdica; paratiroides, rastreo I-131 y terapia I-131 son menores. **Lu-177 sólo en VHSA2** (≈ 7 ciclos/mes). En VHSA2 «otras» incluye PET-CT (≈ 120/mes en base): el vocabulario del inventario no tiene un tipo PET. |
| VHSA2 (CINO) | Rampa de maduración: 50 % de su base en enero 2025 hasta 100 % en diciembre 2025. Comparte 25 referentes con VHSA1 (misma ciudad). |
| Pacientes | Estudios ÷ U(1.00, 1.08): algunos pacientes tienen más de un estudio en el mes. |
| Referencias | 12 % de pacientes sin referente registrado (25 % en «otras»); el resto se reparte entre referentes de especialidades afines al estudio con pesos tipo Zipf, 1 / (rango + 3)^0.8. Pools: MID 70, VHSA1 55, VHSA2 20 + 25 compartidos, OAX 45 referentes. |
| Conversión de referencia | Normal(79 %, 4 pp), acotada a 65–92 %. Referencias recibidas = referidos atendidos ÷ conversión. |
| Ingresos (plantilla) | Estudios × tarifa supuesta (MXN): ósea 5,200; tiroidea 3,800; renal 4,500; perfusión 9,500; paratiroides 5,500; rastreo I-131 7,500; terapia I-131 42,000; Lu-177 145,000 por ciclo; otras 4,500 (VHSA2: 17,500 por mezcla con PET-CT). Ruido σ = 3 %. **No son tarifas de GAMMA.** |
| Canales | Gasto mensual dentro del rango del plan (`presupuesto_canal.csv`): Google ≈ 32 k, Meta ≈ 17 k, LinkedIn ≈ 11 k (desde abr-2025), YouTube ≈ 6.5 k (desde feb-2025), TikTok ≈ 3 k (piloto desde mar-2026), WhatsApp Business ≈ 3 k (herramienta); +0.8 % mensual. CPM: Meta 42, Google 440 (búsqueda), TikTok 15, LinkedIn 210, YouTube 26 MXN. CTR: Google 4.5 %, Meta 1.1 %, TikTok 0.7 %, LinkedIn 0.6 %, YouTube 0.3 %. Lead/clic: Google 9 %, LinkedIn 6 %, Meta 2.6 %, YouTube 2 %, TikTok 1 %. Cita/lead 22–38 %; paciente/cita 60–80 %. |
| WhatsApp | Sólo logística. «Impresiones» = mensajes entregados; «clics» = conversaciones iniciadas; «leads» = solicitudes de agenda (37 % de conversaciones). |
| Embudo | Suma de canales del último mes: impresiones → clics → leads → citas → estudios (pacientes atribuidos). |
| CPL / CPA | Se calculan en el tablero: CPL = gasto ÷ leads; CPA (costo por paciente) = gasto ÷ pacientes atribuidos. |
| Reseñas, NPS y SEO | Reseñas Google 90–440 por sede, calificación 4.4–4.9; NPS pacientes 60–76; NPS referentes 48–64; posición media SEO 2.4–7.0; top-3 local si la posición < 4.5. |
| Congresos | Sólo congresos concluidos del calendario (ANCAM, SMeO y SMNE 2026): contactos, referentes nuevos (7–12 % de contactos), referencias atribuidas (1.4–2.6 por referente nuevo) y costo total (asistencia/stand). |
| KPIs | Valor sintético del último mes para los KPIs de desempeño. Cumplimiento COFEPRIS e incidentes de privacidad **no** tienen valor sintético: sólo se muestran con dato real. |

## Datos reales del inventario de expedientes (HEVESY)

`real_inventario.csv` tiene el mismo esquema que `sintetico_inventario.csv` y hoy está **vacío** (sólo encabezado):

| Columna | Contenido |
|---|---|
| `sede` | MID, VHSA1, VHSA2, OAX, TOL, COL |
| `anio`, `mes` | Año (aaaa) y mes (1–12) del estudio |
| `tipo_estudio` | `gammagrafia_osea`, `tiroidea`, `renal`, `rastreo_i131`, `terapia_i131`, `lu177`, `perfusion_miocardica`, `paratiroides`, `otras` |
| `pacientes`, `estudios` | Conteos agregados de la celda |
| `referente_codigo` | `R-001…` (vacío si no hay referente). Tabla de correspondencia código ↔ médico **fuera** del repositorio y del tablero |
| `especialidad_referente` | Especialidad del referente (texto libre corto) |

Nunca: nombres, CURP, expediente, diagnóstico, CIE ni fechas de nacimiento. Cuando el archivo tenga filas de una sede, el tablero muestra para esa sede los valores de pacientes, estudios, terapias, tipo de estudio, referencias y referentes activos como **REAL — inventario expedientes**, y deja los sintéticos sólo para las sedes y métricas que el inventario no cubre (conversión, ingresos, canales, reseñas, congresos). Los referentes con menos de 5 pacientes en el periodo se agrupan (k ≥ 5).

Nota: el contrato `gamma/referencia@1` (`contracts/schemas/`) aún usa los códigos VSA y CINO; equivalen a VHSA1 y VHSA2.
