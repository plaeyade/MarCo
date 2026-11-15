# MarCo — GAMMA Marketing & Communication

Repositorio privado de la línea **MarCo** del universo GAMMA (red de medicina nuclear en el sureste de México y CINO con ciclotrón).
Contiene la marca, las plantillas de campaña, el circuito de cumplimiento COFEPRIS/LFPDPPP y el esquema del tablero de métricas.

> Convenciones: **†** = dato no verificado en fuente primaria. No se nombran personas. No se publican cifras de desempeño inventadas.

## Estructura

| Carpeta | Contenido |
|---|---|
| `brand/` | **Logo oficial: propuesta 1** en `brand/oficial/` (monograma M+C con arco de emisión). Logos SVG (48 × 48, trazo 3, un color #5250CC, fondo transparente), variantes oscuras (#9C9AF2), wordmarks horizontales y lámina comparativa |
| `campaigns/` | Plantillas de brief, ficha de pieza (JSON) y convención de UTM |
| `compliance/` | Lista de verificación por pieza (COFEPRIS + plataformas) y registro de piezas |
| `dashboard/` | Esquema de métricas, conectores previstos y datos del plan (presupuestos y metas; sin datos reales) |
| `contracts/` | Referencia al contrato `gamma/referencia@1` de `gamma-contracts` (copia de lectura del borrador) |
| `docs/` | Plan de publicidad multicanal; `congresos_2026_2027.md`; `legal/` (registro de marca IMPI y aviso COFEPRIS 02-002-A) |
| `tools/` | Generadores de logos y lámina |
| `tests/` | Pruebas mínimas (marca, cumplimiento, contrato, tablero) |

## Uso

```bash
python3 -m unittest discover -s tests -v      # pruebas
python3 tools/logos.py brand/logos             # regenerar SVG
python3 tools/sheet.py brand/logos brand/lamina_logos_marco.svg && rsvg-convert brand/lamina_logos_marco.svg -o brand/lamina_logos_marco.png
```

## Marca

Logo oficial: **propuesta 1**. Guía de uso: `brand/GUIA_MARCA.md`. Registro ante el IMPI: `docs/legal/registro_marca_impi.md`.

## Tablero

El tablero «MarCo Tablero» (artifact Data, https://claude.ai/artifact/Rr3smpN4rNWtNsHGrCCTAK) lee los CSV de `dashboard/data/`:

- **Reales con fuente:** presupuestos del plan y datos públicos (INEGI 2020, mortalidad INEGI 2024, GLOBOCAN, congresos, IMPI).
- **SINTÉTICOS — no reales:** `sintetico_*.csv`, generados por `tools/sinteticos.py` con semilla fija 20261115; supuestos en `dashboard/data/SUPUESTOS_SINTETICOS.md`. Se rotulan «SINTÉTICO — no real» en cada pestaña y en el pie. No se citan ni se usan para decidir.
- **Reales por llegar:** `real_inventario.csv` (inventario de expedientes HEVESY, agregado y sin nombres; hoy vacío). Cuando tenga filas de una sede, el tablero muestra para esa sede pacientes, estudios por tipo y referencias como «REAL — inventario expedientes». Las plantillas `plazas_mensual.csv`, `canales.csv`, `embudo.csv` y `resenas_seo.csv` siguen vacías hasta conectar sus fuentes (`dashboard/conectores.json`).

Plazas: MID, VHSA1 (Villahermosa sede 1), VHSA2 (Villahermosa sede 2 en el CINO), OAX; próxima apertura TOL y COL.

## Documentos relacionados

- Plan base: `plan_gamma_marketing.md` (línea Marketing & Communication).
- Documento maestro GAMMA, Anexo V.
