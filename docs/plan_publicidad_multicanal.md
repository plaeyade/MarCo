# MarCo — Plan de publicidad multicanal (v1.1, 15-11-2026)

> Línea **MarCo** (Marketing & Communication) del universo GAMMA. Desarrolla el capítulo 4 y la partida de pauta (§ 5.2) del plan base `plan_gamma_marketing.md`.
> Convenciones: **†** = no verificado en fuente primaria o interpretación por validar con abogado regulatorio / la propia plataforma. Montos en **MXN al mes, IVA no incluido**; son **rangos de planeación**, no cotizaciones. No se nombran personas. **No hay cifras de desempeño**: todo resultado (CPC, CPL, conversiones, alcance) se medirá tras el lanzamiento; las columnas de metas sólo repiten las metas del plan base.

## Plazas (actualización 15-11-2026)

| Código | Plaza | Estatus | Servicios | Población 2020 (INEGI) |
|---|---|---|---|---|
| MID | GAMMA Mérida | Operando | Gammagrafía; yodo-131 | Municipio 995,129 · Yucatán 2,320,898 |
| VHSA1 | GAMMA Villahermosa sede 1 «GAMMA» | Operando | Gammagrafía; yodo-131 | Municipio Centro 683,607 · Tabasco 2,402,598 |
| VHSA2 | GAMMA Villahermosa sede 2, en el CINO con el aliado estratégico | **Próxima apertura (fines 2027)** | Previstos al abrir: PET-CT, ciclotrón, gammagrafía, yodo-131, lutecio-177 | (misma ciudad) |
| OAX | GAMMA Oaxaca | Operando | Gammagrafía; yodo-131 | Municipio 270,955 · Oaxaca 4,132,148 |
| TOL | GAMMA Toluca | Próxima apertura | Por definir | Municipio 910,608 ([DataMéxico](https://www.economia.gob.mx/datamexico/es/profile/geo/toluca)) · Estado de México 16,992,418 ([INEGI](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2021/EstSociodemo/ResultCenso2020_Nal.pdf)) |
| COL | GAMMA Colima | Próxima apertura | Por definir | Municipio 157,048 · Colima 731,391 ([INEGI, presentación de resultados Colima](https://www.inegi.org.mx/contenidos/programas/ccpv/2020/doc/cpv2020_pres_res_col.pdf)) |

VHSA2 (sede 2 en el CINO), Toluca y Colima: 0 % de pauta y ninguna actividad comercial hasta su apertura; Perfil de Empresa sólo con domicilio operativo. VHSA2 abre a **fines de 2027** (decisión del propietario, 15-11-2026); sus servicios (PET-CT, lutecio-177, etc.) se anuncian sólo al cumplir la puerta de la § 5 (licencias sanitaria y CNSNS vigentes y permiso de publicidad; AGENTS.md § 1.4). Hasta entonces, el 30 % local de Villahermosa va íntegro a la sede 1; tras la apertura se divide entre sede 1 y sede 2 †. Códigos de sede en todo el plan y en el contrato `gamma/referencia@2`: MID, VHSA1, VHSA2, OAX, TOL, COL. Mortalidad por tumores 2024 (tasa estandarizada, INEGI): Colima 84.5, Estado de México 70.0 por 100 mil.

---

## 0. Resumen

1. **El canal principal sigue siendo el médico referente.** La publicidad pagada apoya tres cosas: (a) que el paciente que ya tiene una orden encuentre la sede y sepa prepararse; (b) que el médico conozca el catálogo, los tiempos y la teranóstica; (c) que aseguradoras, hospitales y clientes B2B identifiquen a GAMMA. No se pauta para "crear" demanda de estudios en personas sanas.
2. **Presupuesto de pauta digital:** **50–120 mil MXN/mes** (la misma bolsa del plan base, 600 k–1.44 M/año) repartida así: Google (Search + Performance Max + Perfil de Empresa) 24–45 k; Meta 12–28 k; LinkedIn 8–20 k; YouTube 4–12 k; TikTok 0–6 k (piloto); Waze 2–5 k; pruebas 0–4 k. **Fuera de la bolsa de pauta**: WhatsApp Business (partida de herramientas) 2–4 k; medios tradicionales locales 0–15 k/mes de mantenimiento y una ola de lanzamiento del CINO de 150–450 k en total (partida de PR y lanzamiento del CINO).
3. **Ninguna pieza sale sin permiso o aviso de publicidad COFEPRIS** cuando aplique ([RLGSMP art. 79](https://mley.mx/Reg_LGS_MP/articulo/79/); [Acuerdo de simplificación 2025](https://sidof.segob.gob.mx/notas/docFuente/5756000)) y sin la lista de verificación de la § 9.
4. **El CINO no se anuncia como servicio disponible** (PET/CT, Lu-177, radiofarmacia) hasta tener licencia sanitaria, licencia CNSNS y, si aplica, CBPF. Antes de eso sólo hay comunicación institucional ("en construcción", empleo, ciencia).
5. **Medición sin datos de salud:** UTM en todo; píxel y API de conversiones sólo con consentimiento y sólo con eventos neutros; ningún evento de "estudio agendado" ni de página de padecimiento sale hacia Meta, Google, TikTok o LinkedIn; la atribución fina se hace dentro de GAMMA OS con el contrato `gamma/referencia@2` (códigos de sede MID, VHSA1, VHSA2, OAX, TOL, COL; `@1` usaba VSA y CINO, hoy alias obsoletos).

---

## 1. Públicos y objetivos por canal

| Público | Necesidad | Canales pagados | Objetivo de la pauta | KPI de seguimiento (del plan base § 5.4) |
|---|---|---|---|---|
| Paciente con orden médica / familiar | Encontrar la sede, saber cómo prepararse, agendar | Google Search, Perfil de Empresa, Waze, Meta (alcance local), WhatsApp (logística) | Llamadas, rutas, clics a "Agendar" | Acciones GBP, costo por paciente adquirido (canal digital), NPS |
| Público general de la ciudad | Saber que existe medicina nuclear local y que es segura | Meta, YouTube, TikTok (piloto), radio/prensa local | Alcance educativo, reproducciones completas | Alcance, visitas a guías educativas |
| Oncología, endocrinología, cardiología, urología, cirugía | Catálogo, tiempos, informe, interconsulta, teranóstica | LinkedIn, Google Search (términos profesionales), YouTube (webinars), correo | Registro a sesiones/webinars, descargas del catálogo, referencias | Referencias por médico, referentes activos |
| Aseguradoras (GMM), TPA, hospitales | Red, tabulador, preautorización, cumplimiento | LinkedIn, prensa especializada †, eventos | Reuniones agendadas | Convenios activos (+3) |
| Clientes B2B (dosimetría TLD, kits fríos) | Calidad documentada, entrega, soporte | LinkedIn, Google Search B2B, congresos | Solicitudes de cotización | Clientes de dosimetría (meta del plan: primeros 20 †) |
| Comunidad cercana al CINO | Tranquilidad sobre el ciclotrón, empleo | Prensa local, radio, Meta geolocalizado, reuniones vecinales | Comprensión y confianza | Menciones y sentimiento |
| Talento (técnicos, físicos, enfermería) | Empleo | LinkedIn, Meta | Postulaciones | Vacantes cubiertas † |

---

## 2. Marco de cumplimiento que aplica a todos los canales

### 2.1 Regulación mexicana

| Regla | Qué implica para la pauta | Fuente |
|---|---|---|
| Publicidad comprobable, orientadora y educativa | Cada afirmación (tiempos, "primero", "único", tecnología) con sustento archivado | [LGS art. 306](https://mley.mx/LGS/articulo/306/) |
| Permiso para publicidad de servicios de salud de establecimientos | Campañas de sedes y del CINO → **permiso de publicidad** (modalidad A tras la simplificación 2025), por versión y medio | [RLGSMP art. 79](https://mley.mx/Reg_LGS_MP/articulo/79/), [art. 80](https://mley.mx/Reg_LGS_MP/articulo/80/); [SIDOF](https://sidof.segob.gob.mx/notas/docFuente/5756000) |
| Aviso de publicidad para actividades profesionales (COFEPRIS-02-002, supuesto A; fusionado por acuerdo DOF 4-may-2026) | Perfil individual del médico nuclear; presentar ≥ 5 días antes de difundir; el proyecto debe señalar la cédula profesional/especialidad; gratuito † | [Manual COFEPRIS de aviso](https://www.gob.mx/cms/uploads/attachment/file/795383/Manual_Aviso_de_Publicidad.pdf) |
| No se autoriza publicidad de tratamientos sin eficacia comprobada o sin acreditar personal y recursos | Nada de "cura", porcentajes de éxito, ni servicios aún no autorizados | [RLGSMP art. 18](https://mley.mx/Reg_LGS_MP/articulo/18/) |
| Datos de salud = datos sensibles; consentimiento expreso y por escrito | Ninguna lista de pacientes se sube a plataformas; testimonios sólo con consentimiento específico | [LFPDPPP 2025](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf) |
| Confidencialidad del expediente | Sin imágenes clínicas identificables ni metadatos DICOM | [NOM-004-SSA3-2012, 5.5](https://www.gob.mx/cms/uploads/attachment/file/512094/NOM-004-SSA3-2012.pdf) |
| Prohibición de dicotomía y de ofertas para atraer pacientes de otros médicos | Sin descuentos "si vienes de parte de…", sin incentivos a referentes | [Código de conducta para el personal de salud, II.E.7](https://www.gob.mx/cms/uploads/attachment/file/242116/CODIGO_DE_CONDUCTA_PARA_EL_PERSONAL_DE_SALUD_2002.pdf) |

**Leyendas:** el permiso puede fijar leyendas obligatorias (p. ej., número de permiso, responsable sanitario) †. La plantilla de cada formato deja un espacio fijo para ellas; si el formato no lo permite (bumper de 6 s, Waze), la leyenda va en la página de destino † (validar con el despacho).

### 2.2 Reglas comunes de plataformas (resumen)

| Plataforma | Clasificación de "salud" | Segmentación por salud | Medición | Fuente |
|---|---|---|---|---|
| Meta | No es "categoría especial de anuncios" (ésas son crédito, empleo, vivienda y temas sociales/políticos †); sin embargo, desde enero de 2025 Meta clasifica a los anunciantes de **salud y bienestar** y limita eventos de embudo medio/bajo (configuración base, restricción media o completa) | Prohibido afirmar o insinuar atributos personales (incluidas condiciones médicas); audiencias y conversiones personalizadas no pueden basarse en salud | Optimización hacia eventos de clic (p. ej., "abrir formulario") en lugar de "envío"; parámetros de URL recortados | [Cardinal Digital Marketing](https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/); [ADM 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/); [Meta, atributos personales](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/) † (texto no legible en esta revisión) |
| Google Ads (Search, PMax, YouTube) | Política "Healthcare and medicines": certificación para farmacias en línea (en México con registro COFEPRIS), servicios de medicamentos de prescripción, fabricantes farmacéuticos, adicciones; **tratamientos especulativos/experimentales prohibidos**; la página no menciona clínicas ni imagen diagnóstica, por lo que no se identifica certificación obligatoria para GAMMA † | Publicidad personalizada: no se segmenta por condiciones de salud; desde el 29-05-2025 se excluye de la categoría el contenido dirigido a profesionales de la salud en su rol profesional | Etiqueta de Google y conversiones mejoradas sólo con consentimiento; no remarketing en páginas de estudios | [Healthcare and medicines](https://support.google.com/adspolicy/answer/176031?hl=en); [Experimental treatments](https://support.google.com/adspolicy/answer/15596627); [cambio mayo 2025](https://support.google.com/adspolicy/answer/16258024?hl=en) |
| TikTok | En México: "instituciones médicas" permitidas si están **registradas ante la autoridad local** y la pauta se limita a **≥ 18 años**; medicamentos de prescripción no permitidos; dispositivos médicos con aprobación local y ≥ 18; cirugía plástica como ejemplo no permitido | Sin segmentación por salud; TikTok pide no usar su tecnología de seguimiento para recolectar información de salud | Píxel sólo en páginas neutras | [TikTok, Healthcare and Pharmaceuticals](https://ads.tiktok.com/help/article/tiktok-ads-policy-healthcare-pharmaceuticals); [ADM 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/) |
| LinkedIn | "Medical devices and medical treatments" restringidos: sólo donde sean legales; no dirigir a < 18; LinkedIn "se reserva el derecho de restringir publicidad relacionada con cualquier asunto de salud"; prescripción sólo EE. UU./Canadá; farmacia y telesalud sólo EE. UU. | Prohibido segmentar con datos sensibles, incluidos datos de salud | Insight Tag no debe instalarse en páginas que recolecten o contengan datos sensibles | [LinkedIn Advertising Policies](https://members.linkedin.com/legal/ads-policy); [ADM 2026](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/) |
| WhatsApp Business | Vertical regulada; **no usar WhatsApp para telemedicina ni para enviar o solicitar información de salud**; opt-in previo | — | Sólo métricas de entrega/lectura de plantillas | [WhatsApp Business Messaging Policy](https://www.whatsappbusiness.com/en-gb/policy/) |
| Google Business Profile | Un perfil por ubicación; nombre real sin palabras clave; perfiles de médicos individuales con reglas propias | — | Llamadas, rutas, clics (agregados) | [Directrices GBP](https://support.google.com/business/answer/3038177?hl=en) |
| Waze Ads | Formatos: flechas, búsqueda, pantallas de "takeover" en alto y pines; la ayuda revisada no menciona restricciones de salud ni disponibilidad por país † | Sólo geografía/horario | Navegaciones y visitas estimadas | [Ayuda Waze Ads](https://support.google.com/wazelocal/answer/9227698?hl=en) |

**Regla de oro de MarCo para copys:** tercera persona o información del servicio, nunca preguntas que supongan un diagnóstico.

| No | Sí |
|---|---|
| "¿Te diagnosticaron cáncer de tiroides?" | "Tratamiento con yodo-131 en Oaxaca: qué es y cómo prepararse" |
| "Elimina tu cáncer con Lu-177" | (no se anuncia hasta autorización; después:) "Teranóstica con Lu-177: un comité evalúa con tu médico si es adecuada" |
| "100 % seguro, sin radiación" | "La dosis se explica antes del estudio y la supervisan especialistas en seguridad radiológica" |
| "El mejor PET del sureste" | "PET/CT en [sede], con informe estructurado" (sólo si se puede sustentar el tiempo prometido) |

---

## 3. Canales

### 3.1 Meta (Facebook e Instagram)

**Objetivo:** alcance educativo local y tráfico a guías de preparación; reclutamiento; comunidad del CINO. No es canal de conversión clínica.

| Elemento | Definición |
|---|---|
| Públicos | Geografía: radio de 15–40 km por sede †; edad ≥ 18 (≥ 25 para piezas de familia/cuidado †); intereses **genéricos** (salud y bienestar general, familia) o segmentación amplia ("Advantage+") sin intereses de padecimientos |
| Prohibido | Listas de clientes con pacientes; públicos similares derivados de pacientes; remarketing de visitantes de páginas de estudios/tratamientos; intereses de enfermedades específicas; copys en segunda persona sobre condiciones |
| Objetivos de campaña | Reconocimiento y alcance (educación); Tráfico (guías y sedes); Interacción (videos); Clientes potenciales **sólo** para empleo, B2B o registro a sesiones, con formularios sin campos clínicos |
| Formatos | Reels 9:16 de 15–45 s, carrusel "cómo prepararse", imagen única de sede, historias con sticker de enlace, video subtitulado |
| Clasificación Meta | Verificar en el Administrador de eventos la categoría asignada al dominio (base, media o completa) y apelar si es incorrecta |
| Moderación | Comentarios con diagnóstico: no confirmar ni ampliar; responder con canal privado genérico; sin consulta clínica en público |

**Ideas de creatividades (sin promesas de curación):**
1. "¿Qué es la medicina nuclear?" en 30 s con animación de trazo (iconografía del universo).
2. Carrusel "Gammagrafía ósea: 5 pasos el día de tu estudio" (llegar, inyección, espera, imagen, salida) †(duraciones del protocolo de cada sede).
3. Reel "Conoce la sede": recepción, sala de espera, equipo de trabajo con consentimiento laboral de imagen, sin pantallas con datos.
4. "Seguridad radiológica explicada" con un físico médico (sin nombre en pieza si así se decide), dosis comparadas con fondo natural según protocolo.
5. CINO pre-licencia: "Así avanza la obra", empleo, ciencia, sin anunciar servicios.

### 3.2 Google Ads (Search, Performance Max, YouTube) y Perfil de Empresa

**Objetivo:** capturar intención ya existente ("gammagrafía ósea Villahermosa") y llevarla a llamada, ruta o formulario de agenda sin datos clínicos.

| Campaña | Contenido | Segmentación permitida | Nota |
|---|---|---|---|
| Search — Estudios por ciudad | Grupos por estudio × sede: ósea, tiroidea, renograma, perfusión miocárdica, ganglio centinela, PET/CT (cuando exista), yodo-131 | Ubicación (ciudad + radio), idioma, horario; palabras clave de intención | Extensiones de llamada, ubicación (vinculada al Perfil de Empresa) y enlaces a guías |
| Search — Marca | "GAMMA medicina nuclear", nombre de sede, "CINO" (tras licencias) | Ubicación | Protege la marca frente a competidores |
| Search — Profesional | "referir paciente medicina nuclear Mérida", "dosimetría TLD", "kits fríos" (sólo tras registro) | Ubicación nacional para B2B | Contenido dirigido a profesionales en su rol (excluido de la categoría de salud sensible desde 2025) |
| Performance Max — Tiendas/locales † | Objetivo de visitas o llamadas por sede, con activos de marca | Ubicación; **sin** listas de clientes de pacientes ni señales de audiencia de salud | Excluir URLs de estudios y tratamientos como destinos de remarketing; revisar que los activos generados no impliquen atributos personales |
| YouTube (vía Google Ads) | Ver § 3.5 | Ubicación, edad ≥ 18, temas generales; sin remarketing de páginas de estudios | Lista de exclusión de contenido sensible |

**Certificación:** con la información revisada no aparece certificación obligatoria para servicios de diagnóstico por imagen; sí la hay para farmacias en línea (en México con registro COFEPRIS), medicamentos de prescripción, fabricantes farmacéuticos y adicciones ([Google](https://support.google.com/adspolicy/answer/176031?hl=en)). **Kits fríos y radiofármacos** pueden activar la política de medicamentos de prescripción o términos restringidos: anunciar sólo a profesionales, sin nombres de fármacos en anuncios, y consultar a Google antes †. Completar la **verificación de anunciante** de Google Ads (identidad de la empresa) antes de lanzar †.

**Perfil de Empresa por sede:**

| Perfil | Categoría principal † | Contenido | Condición |
|---|---|---|---|
| GAMMA Oaxaca | Centro de medicina nuclear / clínica de diagnóstico † | Horario, teléfono, fotos autorizadas, servicios autorizados, enlace a la página de la sede con UTM | Licencias vigentes |
| GAMMA Villahermosa | Ídem | Ídem | Ídem |
| GAMMA Mérida | Ídem | Ídem | Ídem |
| GAMMA Toluca | — | Sólo cuando la sede tenga domicilio operativo y atienda | Apertura |
| GAMMA Colima | — | Sólo cuando la sede tenga domicilio operativo y atienda | Apertura |
| CINO | Centro médico † | "Próximamente" no es un estado de GBP: crear el perfil sólo al abrir †(posible fecha de apertura en GBP; validar) | Licencias |

Respuestas a reseñas: agradecer sin confirmar que la persona es paciente ni mencionar su estudio †(práctica recomendada en salud; consistente con NOM-004 5.5).

### 3.3 TikTok

**Objetivo:** piloto educativo para público joven-adulto y familiares; posicionamiento de empleo. Prioridad baja.

| Elemento | Definición |
|---|---|
| Requisitos | Cuenta de anunciante con verificación de empresa †; registro ante la autoridad local (licencia sanitaria/aviso de funcionamiento) disponible para TikTok; audiencia **≥ 18 años** ([TikTok](https://ads.tiktok.com/help/article/tiktok-ads-policy-healthcare-pharmaceuticals)) |
| No | Medicamentos de prescripción (incluye radiofármacos) en anuncios; antes/después; telediagnóstico; testimonios de eficacia |
| Formatos | In-Feed 9:16 de 9–30 s, Spark Ads sobre publicaciones orgánicas propias |
| Medición | Píxel sólo en página de inicio y de empleo; nunca en estudios/tratamientos |
| Creatividades | "Un día en medicina nuclear" (equipo, sin pacientes); "Mitos y realidades de la radiación" con fuentes; "¿Qué estudias para trabajar aquí?" (física médica, radiofarmacia) |
| Criterio de salida | Si en 3 meses no hay comentarios/visitas a guías que justifiquen el costo †, se pausa y el monto pasa a Google |

### 3.4 LinkedIn (B2B, médicos, aseguradoras, dosimetría y kits)

**Objetivo:** que el médico especialista, el área de redes médicas de aseguradoras, los hospitales y los responsables de seguridad radiológica conozcan a GAMMA; registro a sesiones; cotizaciones B2B.

| Campaña | Público (segmentación profesional) | Formato | Llamada a la acción |
|---|---|---|---|
| Referentes por sede | Cargo/título: oncólogo, endocrinólogo, cardiólogo, urólogo, cirujano oncólogo; ubicación: estados de la sede ± 100 km | Sponsored Content (imagen o documento: catálogo de estudios con indicaciones), Event Ads (sesión académica) | Registrarse a la sesión; descargar catálogo |
| Webinars regionales | Mismo público + residentes | Event Ads, Video | Registrarse (formulario sin datos clínicos) |
| Aseguradoras e instituciones | Empresa: aseguradoras GMM, TPA, hospitales privados; funciones: redes médicas, compras, dirección médica | Message Ads/Conversation Ads † (cuidar frecuencia), Document Ads | Agendar reunión |
| GAMMA DOSIMETRÍA | Funciones: física médica, seguridad radiológica, radiología; sectores: hospitales, industria, odontología † | Document Ads (ficha técnica), Lead Gen Form | Solicitar cotización |
| Kits fríos | Radiofarmacia, medicina nuclear | Document Ads | Solicitar ficha técnica |
| Talento | Física médica, radiofarmacia, enfermería, TSU en imagen | Job posts patrocinados | Postular |

**Condiciones:** dosimetría sólo tras autorización CNSNS y desempeño validado; kits sólo tras registro sanitario (plan base § 4.10). No segmentar por datos de salud ([LinkedIn](https://members.linkedin.com/legal/ads-policy)). Insight Tag sólo en páginas B2B y de eventos, nunca en páginas de pacientes.

### 3.5 YouTube

**Objetivo:** biblioteca de videos educativos (orgánica) con impulso pagado puntual.

| Pieza | Duración | Uso | Pauta |
|---|---|---|---|
| "¿Qué es la medicina nuclear?" | 90–120 s | Web, WhatsApp, sesiones | In-Stream omitible en ciudades de sedes, ≥ 18 |
| Preparación por estudio (ósea, tiroidea, renograma, perfusión, PET) | 60–180 s | Enlace desde confirmación de cita y guías | Sin pauta (orgánico) o In-Feed por búsqueda |
| Seguridad tras yodo-131 | 2–3 min | Material para pacientes y familias, aprobado por el ESR | Sin pauta; acceso por enlace †(evitar "dirigirse" a pacientes con condición) |
| Webinars para médicos | 30–60 min | Educación continua | Bumper de 6 s / In-Feed con segmentación por temas profesionales † |
| CINO: "así se construye" | 60–90 s | Comunidad, prensa | In-Stream local |

Comentarios moderados; subtítulos en español y, en Oaxaca, versión en lengua indígena para piezas clave † (definir variante con la comunidad).

### 3.6 WhatsApp Business (sólo informativo, sin datos de salud)

| Uso permitido | Uso prohibido |
|---|---|
| Confirmación de cita con fecha, hora, sede y enlace a la guía genérica en la web | Resultados, informes, imágenes, diagnósticos, dosis |
| Ubicación, estacionamiento, horario | Preguntas sobre síntomas, medicamentos o padecimientos |
| Recordatorio genérico ("tienes una cita en GAMMA Mérida mañana a las 9:00") | Plantillas de marketing que mencionen padecimientos |
| Encuesta NPS sin preguntas clínicas | Telemedicina o interconsulta |
| Botón "hablar con recepción" | Envío de documentos clínicos |

Requisitos: opt-in previo por categoría (utilidad vs marketing), plantillas aprobadas, aviso de privacidad enlazado, guion de recepción que redirige cualquier pregunta clínica a llamada o portal seguro ([política](https://www.whatsappbusiness.com/en-gb/policy/)). **Anuncios "clic a WhatsApp"** desde Meta: sólo para logística de citas y con mensaje inicial neutro ("Quiero información de horarios").

### 3.7 Waze y presencia local

| Elemento | Uso | Condición |
|---|---|---|
| Pin de marca por sede | Visibilidad en el mapa en el radio de la sede | Dirección y horario idénticos al Perfil de Empresa |
| Búsqueda promocionada | Primer resultado al buscar "medicina nuclear" o el nombre de la sede | Copy informativo |
| Takeover (alto total) | Sólo para el CINO tras apertura y para campañas de marca en corredores hospitalarios † | Sin mensajes de salud alarmistas; legible en 3 s |
| Señalética y directorios | Directorios de hospitales aliados, señalética vial (permisos municipales †) | — |

Disponibilidad y precios de Waze Ads en México por verificar con la plataforma †.

### 3.8 Medios tradicionales locales y prensa

| Medio | Uso | Momento | Nota |
|---|---|---|---|
| Radio local (noticieros matutinos, programas de salud) | Entrevistas educativas (ganadas) y cápsulas pagadas de 20–30 s | Días mundiales (cáncer, tiroides, próstata), lanzamiento del CINO | Cápsulas pagadas = publicidad → permiso COFEPRIS por versión y medio |
| Prensa estatal impresa y digital | Notas de prensa (obra, licencias, inauguración), inserciones informativas | Hitos del CINO; apertura de Toluca | Kit de prensa con hoja de datos verificados |
| Revistas de colegios médicos y boletines hospitalarios | Anuncio institucional para médicos | Congresos estatales | **Permiso** de publicidad (servicios de establecimiento, aunque el público sea médico; ver `docs/legal/aviso_cofepris_02-002-A.md`) |
| Exterior (espectaculares, parabuses) | Sólo marca + ubicación del CINO | Lanzamiento, con licencias | Alto costo; únicamente si la ola de lanzamiento lo justifica |
| TV local | Entrevista en programa de salud (ganada) | Lanzamiento CINO | Vocería entrenada; sin pacientes identificables |

---

## 4. Presupuesto mensual por canal

**Base:** el plan base asigna **50–120 k MXN/mes** a pauta digital (600 k–1.44 M/año), 120–300 k/año a herramientas y 500 k–1.4 M al PR y lanzamiento del CINO. Aquí se reparte esa bolsa; no se suma dinero nuevo.

| Canal | Bajo (MXN/mes) | Alto (MXN/mes) | % de la bolsa (alto) | Partida del plan base |
|---|---:|---:|---:|---|
| Google Search + Performance Max + Perfil de Empresa | 24 000 | 45 000 | 37.5 % | Pauta digital |
| Meta (Facebook + Instagram) | 12 000 | 28 000 | 23.3 % | Pauta digital |
| LinkedIn | 8 000 | 20 000 | 16.7 % | Pauta digital |
| YouTube | 4 000 | 12 000 | 10.0 % | Pauta digital |
| TikTok (piloto) | 0 | 6 000 | 5.0 % | Pauta digital |
| Waze | 2 000 | 5 000 | 4.2 % | Pauta digital |
| Pruebas y reserva de pauta | 0 | 4 000 | 3.3 % | Pauta digital |
| **Subtotal pauta digital** | **50 000** | **120 000** | **100 %** | = plan base § 5.2 |
| WhatsApp Business (API, conversaciones) † | 2 000 | 4 000 | — | Herramientas |
| Medios tradicionales locales (mantenimiento) | 0 | 15 000 | — | PR / contingencia |
| Ola de lanzamiento del CINO (3 meses, total) | 150 000 | 450 000 | — | PR y lanzamiento del CINO |

**Reparto por sede (orientativo †):** OAX 30 %, Villahermosa 30 % (VHSA1 íntegro hasta la apertura de VHSA2; después VHSA1 y VHSA2), MID 40 % de la pauta local (Mérida tiene competencia PET directa y mayor costo por clic esperado †); TOL y COL 0 % hasta su apertura; VHSA2 (CINO) 0 % antes de su apertura (fines de 2027) y de cumplir la puerta de la § 5, y tras ella hasta 35 % de la bolsa durante 3 meses tomando monto de las tres sedes operando.

**Reglas de reasignación:** mensual, con el tablero; sólo se mueve dinero entre canales de la misma partida; cualquier canal sin piezas aprobadas en el mes queda en 0.

---

## 5. Calendario de lanzamiento

| Mes | OAX | VHSA1 | MID | TOL | VHSA2 (CINO) | Canales |
|---|---|---|---|---|---|---|
| Dic-2026 | Perfil de Empresa, permisos en trámite | Ídem | Ídem | — | Comunicación institucional (obra, empleo) | GBP, LinkedIn orgánico |
| Ene-2027 | Search de marca y estudios (al recibir permiso) | Ídem | Ídem | — | Ídem | Google, WhatsApp (plantillas) |
| Feb-2027 | Meta educativo | Meta educativo | Meta educativo | — | Ídem | Meta |
| Mar-2027 | LinkedIn referentes + sesión académica | Ídem | Ídem | Estudio de mercado | — | LinkedIn, YouTube |
| Abr–May 2027 | YouTube preparación; Waze | Ídem | Ídem | — | — | YouTube, Waze |
| Jun–Ago 2027 | Mantenimiento; piloto TikTok en 1 sede † | Mantenimiento | Mantenimiento | GBP si hay sede | Prensa de avance de obra; vecinos | TikTok, prensa |
| Sep–Nov 2027 | Mantenimiento | Mantenimiento | Mantenimiento | Apertura digital (si procede) | Preapertura: comunicación institucional; permiso de publicidad de la ola en trámite; sin anunciar servicios | Prensa, LinkedIn orgánico |
| Dic-2027 (apertura prevista †) | Mantenimiento | Mantenimiento | Mantenimiento | — | **Sólo con la puerta cumplida:** inauguración, ola de medios, Search/Meta/YouTube/Waze de VHSA2 | Todos |

**Puerta de VHSA2 · CINO (apertura prevista a fines de 2027; todas deben estar en "sí"):** fecha de apertura confirmada por el propietario; licencia sanitaria; licencia de operación CNSNS de la instalación y del ciclotrón; CBPF si se distribuirán radiofármacos; permiso de publicidad de la campaña; simulacro de crisis realizado; autorización del aliado estratégico (hospital anfitrión) y de proveedores para mencionarlos; estatus de VHSA2 cambiado a «Operando» en `dashboard/data/sedes.csv` y `geo_sedes.csv`. Antes de eso VHSA2 no tiene pauta, piezas de servicio ni actividad en el tablero (ni siquiera sintética).

---

## 6. Medición

| Pieza | Regla |
|---|---|
| UTM | `utm_source` (google, meta, tiktok, linkedin, youtube, waze, radio, prensa), `utm_medium` (cpc, paid_social, display, video, qr, referral), `utm_campaign` = `{sede}_{objetivo}_{aaaamm}` (p. ej., `mid_estudios_202701`), `utm_content` = id de pieza del registro de cumplimiento; **nunca** un padecimiento ni un estudio sensible en la UTM † |
| Analítica web (GA4 u otra) | IP anonimizada, banner de consentimiento con categorías, sin etiquetas de terceros en páginas de estudios/tratamientos (plan base § 4.2) |
| Píxel/API de conversiones | Sólo tras consentimiento; eventos neutros: `PageView` en inicio y sedes, `Contact` (clic a llamar), `FindLocation` (clic a ruta), `Lead` sólo en empleo/B2B/eventos; sin parámetros personalizados; sin eventos de "cita agendada" |
| Llamadas | Números de seguimiento por canal/sede †; grabación sólo con aviso; el registro no guarda motivo clínico |
| Formularios | Nombre, teléfono/correo, sede, estudio solicitado de una lista (sin diagnóstico ni texto libre clínico), casillas de consentimiento separadas |
| Atribución fina | Dentro de GAMMA OS: el campo `atribucion` del evento `gamma/referencia@2` guarda la campaña (UTM) sin datos personales; agregados con k ≥ 5 † |
| Periodicidad | Semanal (pauta), mensual (tablero MarCo), trimestral (reasignación) |
| Metas | Sólo las del plan base (§ 4.1); los objetivos por canal se fijan tras 90 días de línea base |

---

## 7. Creatividades: banco de ideas por objetivo

| Objetivo | Idea | Canal | Formato | Riesgo a vigilar |
|---|---|---|---|---|
| Encontrar la sede | "Medicina nuclear en Villahermosa: horarios y cómo llegar" | Search, Waze, GBP | Texto, pin | Coherencia con GBP |
| Preparación | "Antes de tu gammagrafía tiroidea: 4 cosas que tu médico te pedirá revisar" † | Meta, YouTube | Carrusel, video | No sustituir indicación médica |
| Seguridad | "Radiación: qué recibe tu cuerpo y cómo la cuidamos" | YouTube, Meta | Video con física médica | Cifras del protocolo, no de internet |
| Confianza | "Nuestro equipo" (técnicos, enfermería, recepción) | Instagram, TikTok | Reels | Consentimiento laboral de imagen |
| Referentes | "Informe estructurado: así se ve" (machote sin datos reales, Anexo U) | LinkedIn | Documento | Sin datos de pacientes |
| Referentes | "Sesión: cuándo pedir una PET" | LinkedIn, correo | Event Ads | Aval académico † |
| Aseguradoras | "Red regional y preautorización: qué ofrecemos" | LinkedIn | Document Ads | Sin precios públicos |
| B2B | "Dosimetría TLD: lectura, trazabilidad, reporte digital" | LinkedIn, Search | Ficha técnica | Sólo tras autorización |
| Comunidad CINO | "El ciclotrón: qué es y por qué es seguro para los vecinos" | Prensa, radio, Meta local | Infografía | Revisión del ESR; sin ubicación de fuentes |
| Lanzamiento CINO | "Diagnóstico molecular y tratamiento de precisión en [región]" | Todos | Kit completo | Sólo con licencias; sin "primero" sin sustento |

---

## 8. Roles y flujo de aprobación por pieza

1. **Brief** (MarCo) → 2. **Borrador** (agencia o contenido) → 3. **Revisión médica** (médico nuclear designado) → 4. **Revisión radiológica** si menciona radiación (ESR/física médica) → 5. **Revisión regulatoria y de privacidad** (despacho/oficial de privacidad) → 6. **Permiso o aviso COFEPRIS** cuando aplique → 7. **Checklist de plataforma** (§ 9) → 8. **Publicación** con id de pieza en `utm_content` → 9. **Registro** en el tablero (cumplimiento de piezas).

Tiempo de ciclo a planear: 5–20 días hábiles por trámite de permiso según la vía ([RLGSMP art. 80](https://mley.mx/Reg_LGS_MP/articulo/80/)); por eso las piezas de días mundiales se preparan con 6–8 semanas de anticipación †.

---

## 9. Lista de verificación COFEPRIS + plataforma por pieza

Cada pieza obtiene un id (`MC-{sede}-{canal}-{aaaamm}-{nn}`) y se registra con esta lista. Una sola respuesta "no" en los puntos marcados con ● bloquea la publicación.

| # | Verificación | Aplica a | Evidencia |
|---|---|---|---|
| ● 1 | Permiso de publicidad (establecimiento) o aviso (profesional) vigente para esta versión y medio, o dictamen de que no se requiere | Todas | Número / dictamen |
| ● 2 | Servicio anunciado autorizado y operando en esa sede (licencia sanitaria, CNSNS, CBPF si aplica) | Todas | Licencias |
| ● 3 | Sin promesas de curación, porcentajes no sustentados, "100 %", "sin riesgo", "el mejor" | Todas | Firma médica |
| ● 4 | Cada afirmación verificable tiene sustento archivado | Todas | Carpeta |
| ● 5 | Sin datos, imagen, voz o caso de pacientes, o con consentimiento expreso y escrito específico + desidentificación | Todas | Folio |
| 6 | Mensajes de radiación revisados por ESR/física médica | Las que mencionan radiación | Firma |
| ● 7 | **Meta:** sin afirmar o insinuar atributos personales; sin audiencias basadas en salud; categoría de dominio revisada | Meta | Captura |
| ● 8 | **Google:** sin segmentación personalizada por salud; sin tratamientos experimentales; sin nombres de fármacos de prescripción en anuncios a público general; verificación de anunciante completa | Google/YouTube | Captura |
| ● 9 | **TikTok:** audiencia ≥ 18; registro local disponible; sin prescripción; píxel fuera de páginas de salud | TikTok | Captura |
| ● 10 | **LinkedIn:** sin segmentación por datos sensibles; < 18 excluido; Insight Tag fuera de páginas de pacientes | LinkedIn | Captura |
| ● 11 | **WhatsApp:** opt-in registrado; plantilla aprobada; cero información clínica | WhatsApp | Id de plantilla |
| 12 | **Waze/GBP:** nombre, dirección y horario idénticos; sin palabras clave en el nombre | Waze, GBP | Captura |
| ● 13 | Página de destino con aviso de privacidad, formulario sin datos clínicos, sin píxeles de terceros en páginas de estudios | Digitales | URL |
| 14 | UTM correcta y sin términos de salud sensibles; `utm_content` = id de pieza | Digitales | URL |
| 15 | Leyendas exigidas por el permiso † e identificación del establecimiento | Todas | Captura |
| 16 | Sin comparaciones denigrantes ni ofertas para atraer pacientes de otros médicos | Todas | Firma |
| 17 | Si menciona software/IA (HEVESY, GAMMA OS): "herramienta de investigación/apoyo", sin afirmaciones diagnósticas | Las que aplique | Firma |
| 18 | Accesibilidad: subtítulos, contraste, lenguaje claro; lengua indígena cuando aplique † | Todas | Revisión |
| 19 | Para VHSA2 (CINO): puerta de lanzamiento (§ 5) cumplida; apertura prevista fines de 2027 | VHSA2 | Lista firmada |

---

## 10. Riesgos de la pauta

| Riesgo | Señal | Respuesta |
|---|---|---|
| Rechazo de anuncios o restricción de cuenta | Notificación de política | Revisar copy (atributos personales), apelar con evidencia; no crear cuentas nuevas para eludir |
| Clasificación restrictiva en Meta | Eventos bloqueados en Administrador de eventos | Optimizar por clic/alcance; medir dentro de GAMMA OS |
| Costo por clic alto en Mérida por competencia | Presupuesto agotado temprano | Concentrar en marca + estudios donde GAMMA tenga diferencial; reforzar GBP orgánico |
| Comentario con diagnóstico propio en un anuncio | Comentario público | Protocolo de moderación (plan base § 4.5) |
| Pieza del CINO publicada antes de licencias | Detección interna o de prensa | Retirar, aclarar, registrar incidente (plan base § 6) |
| Uso de WhatsApp para información clínica | Auditoría mensual | Capacitación, plantillas cerradas, incidente de privacidad |

---

## 11. Decisiones que se piden al propietario

1. Aprobar el reparto de la bolsa de pauta (§ 4) y el reparto por sede.
2. Aprobar el piloto de TikTok o dejarlo en 0.
3. Contratar el despacho regulatorio para el primer paquete de permisos (campaña institucional + Search + Meta).
4. Elegir proveedor de WhatsApp Business API y de números de seguimiento de llamadas.
5. Confirmar el dominio web y la herramienta de analítica (GA4 u otra con hospedaje compatible con LFPDPPP †).

---

## Fuentes

- Ley General de Salud, art. 306: https://mley.mx/LGS/articulo/306/
- RLGSMP arts. 18, 79, 80: https://mley.mx/Reg_LGS_MP/articulo/18/ · https://mley.mx/Reg_LGS_MP/articulo/79/ · https://mley.mx/Reg_LGS_MP/articulo/80/
- Acuerdo de simplificación de trámites COFEPRIS 2025 (SIDOF): https://sidof.segob.gob.mx/notas/docFuente/5756000
- Manual COFEPRIS de aviso de publicidad: https://www.gob.mx/cms/uploads/attachment/file/795383/Manual_Aviso_de_Publicidad.pdf
- LFPDPPP 2025: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf
- NOM-004-SSA3-2012: https://www.gob.mx/cms/uploads/attachment/file/512094/NOM-004-SSA3-2012.pdf
- Código de conducta para el personal de salud: https://www.gob.mx/cms/uploads/attachment/file/242116/CODIGO_DE_CONDUCTA_PARA_EL_PERSONAL_DE_SALUD_2002.pdf
- Google Ads, Healthcare and medicines: https://support.google.com/adspolicy/answer/176031?hl=en
- Google Ads, tratamientos especulativos y experimentales: https://support.google.com/adspolicy/answer/15596627
- Google Ads, cambio de publicidad personalizada (29-05-2025): https://support.google.com/adspolicy/answer/16258024?hl=en
- Directrices del Perfil de Empresa de Google: https://support.google.com/business/answer/3038177?hl=en
- TikTok, Healthcare and Pharmaceuticals (filas de México): https://ads.tiktok.com/help/article/tiktok-ads-policy-healthcare-pharmaceuticals
- LinkedIn Advertising Policies: https://members.linkedin.com/legal/ads-policy
- WhatsApp Business Messaging Policy: https://www.whatsappbusiness.com/en-gb/policy/
- Waze Ads, formatos: https://support.google.com/wazelocal/answer/9227698?hl=en
- Meta, restricciones de datos para salud (resumen de agencia): https://www.cardinaldigitalmarketing.com/healthcare-resources/blog/meta-announces-major-changes-healthcare-advertising/
- Resumen 2026 de políticas de salud en redes (agencia): https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/
- Meta, atributos personales (no legible en esta revisión †): https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- Meta, categorías especiales de anuncios (no se pudo consultar; la lista crédito/empleo/vivienda/temas sociales queda †): https://www.facebook.com/business/help/298000447747885
