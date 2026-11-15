# Contratos

MarCo **consume** contratos definidos en el repositorio `gamma-contracts`; no los define.

| Contrato | Estado | Uso en MarCo |
|---|---|---|
| `gamma/referencia@1` | Borrador, por aprobar mediante ADR en `gamma-contracts` | Agregados de referencias por sede/referente/campaña para el tablero |

`schemas/gamma.referencia.v1.json` es una **copia de lectura** del borrador publicado en el plan base (§ 5.5) para las pruebas locales. La fuente de verdad es `gamma-contracts`; al aprobarse, sustituir esta copia por un submódulo o paquete versionado.

Campos prohibidos en el evento (lo verifican las pruebas): diagnóstico, CIE, resultados, imágenes, notas clínicas, nombre, CURP.
