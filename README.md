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

El tablero «MarCo Tablero» (artifact Data, https://claude.ai/artifact/Rr3smpN4rNWtNsHGrCCTAK) lee los CSV de `dashboard/data/`: presupuestos del plan y datos públicos con fuente (INEGI, GLOBOCAN, congresos) como cifras reales; plantillas vacías de desempeño por plaza y canal; y archivos `ejemplo_*.csv` con cifras **de ejemplo, no reales**, que sólo se muestran al activar «Ver ejemplo». Las fuentes futuras están en `dashboard/conectores.json`.
Hasta conectar APIs, todas las métricas de desempeño quedan vacías.

## Documentos relacionados

- Plan base: `plan_gamma_marketing.md` (línea Marketing & Communication).
- Documento maestro GAMMA, Anexo V.
