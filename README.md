# MarCo — GAMMA Marketing & Communication

Repositorio privado de la línea **MarCo** del universo GAMMA (red de medicina nuclear en el sureste de México y CINO con ciclotrón).
Contiene la marca, las plantillas de campaña, el circuito de cumplimiento COFEPRIS/LFPDPPP y el esquema del tablero de métricas.

> Convenciones: **†** = dato no verificado en fuente primaria. No se nombran personas. No se publican cifras de desempeño inventadas.
>
> **Datos sintéticos.** Los archivos `dashboard/data/sintetico_*.csv` son **SINTÉTICOS — no reales**. Los genera
> `tools/sinteticos.py` (semilla fija 20261115) y van rotulados en el tablero. No se citan en piezas, informes externos ni
> decisiones (excepción oficial del 15-11-2026, [AGENTS.md](AGENTS.md) §4).

## Estructura

| Carpeta | Contenido |
|---|---|
| `brand/` | **Logo oficial: propuesta 1** en `brand/oficial/` (monograma M+C con arco de emisión). Logos SVG (48 × 48, trazo 3, un color #5250CC, fondo transparente), variantes oscuras (#9C9AF2), wordmarks horizontales y lámina comparativa |
| `campaigns/` | Plantillas de brief, ficha de pieza (JSON) y convención de UTM |
| `compliance/` | Lista de verificación por pieza (COFEPRIS + plataformas) y registro de piezas |
| `dashboard/` | Esquema de métricas (`metricas.schema.json`), conectores previstos (`conectores.json`), página del tablero (`tablero_index.html`) y `data/`: datos del plan y públicos con fuente, sintéticos rotulados y plantillas reales vacías |
| `contracts/` | Copia de lectura de `gamma/referencia@2` de `gamma-contracts` (y del borrador `@1`, obsoleto) |
| `docs/` | Plan de publicidad multicanal; `congresos_2026_2027.md`; `legal/` (registro de marca IMPI y aviso COFEPRIS 02-002-A) |
| `tools/` | `logos.py` (SVG de las propuestas), `sheet.py` (lámina comparativa) y `sinteticos.py` (CSV sintéticos con semilla fija) |
| `tests/` | `test_marco.py`: 21 pruebas (marca, cumplimiento, contrato, tablero, sintéticos) |

## Instalación y uso

Sólo requiere Python ≥ 3.11 de la biblioteca estándar (sin dependencias). Para el PNG de la lámina hace falta
`rsvg-convert` (librsvg).

```bash
python3 -m unittest discover -s tests -v       # pruebas
python3 tools/logos.py brand/logos              # regenera los SVG y brand/logos/titles.json (intermedio, no versionado)
python3 tools/sheet.py brand/logos brand/lamina_logos_marco.svg && rsvg-convert brand/lamina_logos_marco.svg -o brand/lamina_logos_marco.png
python3 tools/sinteticos.py                     # regenera dashboard/data/sintetico_*.csv
```

Los tres generadores son deterministas: con el repositorio limpio, volver a correrlos no deja diferencias en git.

## Marca

Logo oficial: **propuesta 1**. Guía de uso: [brand/GUIA_MARCA.md](brand/GUIA_MARCA.md). Registro ante el IMPI: [docs/legal/registro_marca_impi.md](docs/legal/registro_marca_impi.md).

## Tablero

El tablero «MarCo Tablero» (artifact Data, https://claude.ai/artifact/Rr3smpN4rNWtNsHGrCCTAK) lee los CSV de `dashboard/data/`:

- **Reales con fuente:** presupuestos del plan y datos públicos (INEGI 2020, mortalidad INEGI 2024, GLOBOCAN, congresos, IMPI).
- **SINTÉTICOS — no reales:** `sintetico_*.csv`, generados por `tools/sinteticos.py` con semilla fija 20261115; supuestos en `dashboard/data/SUPUESTOS_SINTETICOS.md`. Se rotulan «SINTÉTICO — no real» en cada pestaña y en el pie. No se citan ni se usan para decidir.
- **Reales por llegar:** `real_inventario.csv` (inventario de expedientes HEVESY, agregado y sin nombres; hoy vacío). Cuando tenga filas de una sede, el tablero muestra para esa sede pacientes, estudios por tipo y referencias como «REAL — inventario expedientes». Las plantillas `plazas_mensual.csv`, `canales.csv`, `embudo.csv` y `resenas_seo.csv` siguen vacías hasta conectar sus fuentes (`dashboard/conectores.json`).

Plazas operando: MID, VHSA1 (Villahermosa sede 1), OAX. Próxima apertura: VHSA2 (Villahermosa sede 2 en el CINO, fines de 2027), TOL y COL. Las sedes de próxima apertura no tienen actividad en el tablero, ni siquiera sintética.

## Estado y siguiente fase

- **Hecho:** marca oficial (propuesta 1), estrategia de registro ante el IMPI documentada, plantillas de campaña, circuito de
  cumplimiento COFEPRIS/LFPDPPP, plan de publicidad multicanal, calendario de congresos, tablero con datos del plan,
  públicos con fuente y sintéticos rotulados, y copia de lectura de `gamma/referencia@2`.
- **Siguiente:** conectar las fuentes reales de `dashboard/conectores.json` (`real_inventario.csv` desde HEVESY,
  agregado y con k ≥ 5, y después canales, embudo, plazas y reseñas). Cuando `gamma/referencia@2` pase a `estable` en
  gamma-contracts, sustituir la copia de `contracts/schemas/` por un paquete versionado.

## Documentos relacionados

- [docs/plan_publicidad_multicanal.md](docs/plan_publicidad_multicanal.md): plan de publicidad multicanal.
- [docs/congresos_2026_2027.md](docs/congresos_2026_2027.md): congresos 2026–2027.
- [docs/legal/registro_marca_impi.md](docs/legal/registro_marca_impi.md) y [docs/legal/aviso_cofepris_02-002-A.md](docs/legal/aviso_cofepris_02-002-A.md).
- [compliance/checklist.md](compliance/checklist.md), [contracts/README.md](contracts/README.md) y [AGENTS.md](AGENTS.md) (reglas obligatorias).
- Fuera de este repositorio: el plan base `plan_gamma_marketing.md` (línea Marketing & Communication) y el documento
  maestro GAMMA, Anexo V.

## Licencia

Repositorio privado sin licencia publicada: todos los derechos reservados. La marca MarCo y sus logos son de uso
exclusivo de GAMMA.
