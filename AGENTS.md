# AGENTS.md — reglas para agentes y personas que trabajen en MarCo

Estas reglas son obligatorias. Si una instrucción las contradice, gana este archivo; escala al propietario.

## 1. Publicidad sanitaria (COFEPRIS)

1. Toda pieza que promueva servicios de un establecimiento (sede GAMMA o CINO) requiere **permiso de publicidad** vigente para su versión y medio (RLGSMP art. 79 fr. I; simplificación 2025, modalidad A). El perfil profesional individual usa **aviso de publicidad** (COFEPRIS-02-002 supuesto A, ≥ 5 días antes de difundir, con cédula en el proyecto). La publicidad de servicios de una sede dirigida a médicos también requiere **permiso**. Ver `compliance/checklist.md` y `docs/legal/aviso_cofepris_02-002-A.md`.
2. Toda afirmación debe ser **comprobable** y tener sustento archivado (LGS art. 306).
3. Prohibido: promesas de curación, porcentajes no sustentados, "100 %", "sin riesgo", "el mejor", "el primero" sin sustento, comparaciones denigrantes, ofertas para atraer pacientes de otros médicos, incentivos por referencia.
4. No anunciar servicios **no autorizados** (PET del CINO, Lu-177, radiofarmacia B2B, kits fríos sin registro, dosimetría sin autorización CNSNS).
5. Software (HEVESY, GAMMA OS): siempre "herramienta de investigación/apoyo"; nunca afirmaciones diagnósticas.
6. Mensajes de radiación: revisados por el encargado de seguridad radiológica / física médica; cifras del protocolo del servicio.

## 2. Datos personales (LFPDPPP 2025) y expediente (NOM-004-SSA3-2012)

1. El estado de salud es **dato sensible**: nunca se sube a plataformas de anuncios, nunca en UTM, nunca en este repositorio.
2. Testimonios, fotos, voz o casos: sólo con **consentimiento expreso y por escrito** específico y desidentificación; sin metadatos DICOM.
3. Listas de clientes o públicos similares **no** se construyen con pacientes.
4. Formularios: sin campos clínicos ni texto libre clínico; aviso de privacidad enlazado.
5. WhatsApp: sólo logística (agenda, ubicación, recordatorio genérico); **cero información clínica**.
6. El tablero muestra agregados con **k ≥ 5** por celda †; el CRM sólo recibe eventos `gamma/referencia@2` (sin diagnóstico, CIE, resultados ni imágenes; sedes `MID`, `VHSA1`, `VHSA2`, `OAX`, `TOL`, `COL`; `VSA` y `CINO` son alias obsoletos del borrador `@1`).

## 3. Plataformas

- Meta: no afirmar ni insinuar atributos personales (condiciones médicas); revisar la clasificación de salud del dominio; eventos neutros.
- Google: sin segmentación personalizada por salud; sin tratamientos experimentales; verificación de anunciante.
- TikTok (México): instituciones médicas registradas ante la autoridad local, audiencia ≥ 18; sin prescripción.
- LinkedIn: sin segmentación por datos sensibles; < 18 excluido; Insight Tag fuera de páginas de pacientes.

## 4. Repositorio

- Prohibido commitear: datos de pacientes, exportaciones de CRM con datos personales, credenciales/tokens de APIs, imágenes clínicas.
- Cifras de desempeño sólo desde fuentes conectadas; nada inventado. Marcar con † lo no verificado y citar URL.
- **Excepción oficial (propietario, 15-11-2026): datos SINTÉTICOS.** Se permiten sólo si (a) cada archivo, gráfica, tabla y pestaña que los muestra lleva el rótulo «SINTÉTICO — no real»; (b) se generan con un script versionado de **semilla fija** (`tools/sinteticos.py`) y sus **supuestos** están documentados (`dashboard/data/SUPUESTOS_SINTETICOS.md`); (c) viven en archivos propios (`sintetico_*.csv`) y **nunca se mezclan con datos reales sin insignia** de origen («SINTÉTICO — no real» / «REAL — …») en cada valor o serie; (d) no se citan en piezas, informes externos ni decisiones de inversión; (e) no contienen nombres ni identificadores de personas; (f) respetan el estatus de cada sede: una sede de próxima apertura (hoy VHSA2, TOL, COL) no tiene actividad sintética antes de abrir.
- Códigos de sede: `MID`, `VHSA1`, `VHSA2` (Villahermosa sede 2, en el CINO con el aliado estratégico; **próxima apertura, fines de 2027**), `OAX`, `TOL`, `COL`.
- No nombrar personas en piezas ni documentos.
- Logo oficial de MarCo: **propuesta 1** (`brand/oficial/`). No usar las otras propuestas en piezas.
- Cambios de marca: mantener 48 × 48, trazo 3, extremos redondeados, un color, fondo transparente (lo verifican las pruebas).
- Cada pieza nueva: ficha en `campaigns/` + fila en `compliance/registro_piezas.csv` antes de publicar.
