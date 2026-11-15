# Lista de verificación por pieza (COFEPRIS + plataformas)

Id de pieza: `MC-{SEDE}-{canal}-{aaaamm}-{nn}`. Un "no" en un punto ● bloquea la publicación.

| # | Verificación | Aplica | Evidencia |
|---|---|---|---|
| ● 1 | Permiso 02-001 mod. A (establecimiento, aunque el público sea médico) o aviso 02-002 supuesto A (profesional, presentado ≥ 5 días antes y con cédula) para versión y medio, o dictamen de no requerido | Todas | Número / acuse / dictamen |
| ● 2 | Servicio autorizado y operando en la sede (licencia sanitaria, CNSNS, CBPF si aplica) | Todas | Licencias |
| ● 3 | Sin promesas de curación, % no sustentados, "100 %", "sin riesgo", "el mejor" | Todas | Firma médica |
| ● 4 | Afirmaciones con sustento archivado | Todas | Carpeta |
| ● 5 | Sin datos/imagen/voz/caso de pacientes, o consentimiento escrito específico + desidentificación | Todas | Folio |
| 6 | Mensajes de radiación revisados por ESR/física médica | Si mencionan radiación | Firma |
| ● 7 | Meta: sin atributos personales; sin audiencias de salud; categoría de dominio revisada | Meta | Captura |
| ● 8 | Google: sin segmentación por salud; sin tratamientos experimentales; sin fármacos de prescripción a público general; verificación de anunciante | Google/YouTube | Captura |
| ● 9 | TikTok: ≥ 18; registro local; sin prescripción; píxel fuera de páginas de salud | TikTok | Captura |
| ● 10 | LinkedIn: sin datos sensibles; < 18 excluido; Insight Tag sólo B2B | LinkedIn | Captura |
| ● 11 | WhatsApp: opt-in; plantilla aprobada; cero información clínica | WhatsApp | Id plantilla |
| 12 | Waze/GBP: nombre, dirección y horario idénticos; sin palabras clave en el nombre | Waze/GBP | Captura |
| ● 13 | Destino con aviso de privacidad; formulario sin datos clínicos; sin píxeles en páginas de estudios | Digitales | URL |
| 14 | UTM correcta, sin términos de salud; `utm_content` = id de pieza | Digitales | URL |
| 15 | Leyendas exigidas por el permiso † e identificación del establecimiento | Todas | Captura |
| 16 | Sin comparaciones denigrantes ni ofertas para atraer pacientes de otros médicos | Todas | Firma |
| 17 | Software/IA: "herramienta de investigación/apoyo", sin afirmaciones diagnósticas | Si aplica | Firma |
| 18 | Accesibilidad (subtítulos, contraste, lenguaje claro; lengua indígena †) | Todas | Revisión |
| ● 19 | VHSA2 (CINO): puerta de lanzamiento cumplida (apertura confirmada —prevista fines 2027—, licencias, permiso, simulacro, autorizaciones de terceros) | VHSA2 | Lista firmada |

Fuentes: LGS art. 306 (https://mley.mx/LGS/articulo/306/); RLGSMP arts. 18, 79, 80 (https://mley.mx/Reg_LGS_MP/articulo/79/); LFPDPPP 2025 (https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf); NOM-004-SSA3-2012 (https://www.gob.mx/cms/uploads/attachment/file/512094/NOM-004-SSA3-2012.pdf); políticas de plataformas en `docs/plan_publicidad_multicanal.md`.

## Palabras bloqueadas (prueba automática sobre `copy`)

cura, curar, curación, elimina el cáncer, 100 %, 100%, sin riesgo, sin radiación, garantizado, el mejor, ¿tienes cáncer, ¿padeces
