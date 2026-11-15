# Contratos

MarCo **consume** contratos definidos en el repositorio `gamma-contracts`; no los define.

| Contrato | Estado | Uso en MarCo |
|---|---|---|
| `gamma/referencia@2` | Propuesta en `gamma-contracts` (PR #1, ADR-0002), por aprobar con revisión independiente | Agregados de referencias por sede/referente/campaña para el tablero. Sedes `MID`, `VHSA1`, `VHSA2`, `OAX`, `TOL`, `COL` |
| `gamma/referencia@1` | Borrador obsoleto, nunca registrado | Sólo lectura de borradores: `VSA` → `VHSA1`, `CINO` → `VHSA2`, canal `telefono` → `llamada_telefonica` (`migrar_referencia_1_a_2()` de `gamma-contracts`) |

`schemas/gamma.referencia@2.schema.json` es una **copia de lectura idéntica byte a byte** de `contracts/gamma/referencia@2.schema.json` de `gamma-contracts`, para las pruebas locales; `schemas/gamma.referencia.v1.json` conserva el borrador del plan base (§ 5.5), obsoleto. La fuente de verdad es `gamma-contracts`; al aprobarse, sustituir la copia por un submódulo o paquete versionado.

Campos prohibidos en el evento (lo verifican las pruebas): diagnóstico, CIE, resultados, imágenes, notas clínicas, nombre, CURP.
