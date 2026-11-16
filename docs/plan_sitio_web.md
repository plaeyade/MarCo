# Plan de arreglo del sitio web GAMMA (gammadiagnosticos.com)

Fecha de corte: 15-nov-2026. **†** = no verificado en fuente primaria o criterio interpretativo. Fuentes al final. Sin nombres de personas: los cargos (responsable sanitario, médico nuclear, ESR) se completan con los datos de cada sede.

**En una línea:** el sitio carga en 24 s en móvil (LCP), se mueve mientras carga (CLS 0.485), no mide nada, pide adjuntar la orden médica en un formulario abierto y publica una afirmación de exclusividad («Único centro autorizado en el sureste») y una marca de medicamento de prescripción (Xofigo) sin sustento visible. En 2 semanas se puede llegar a LCP < 2.5 s y CLS < 0.1, medir clics a WhatsApp/teléfono por sede y dejar el contenido listo para el permiso de publicidad COFEPRIS.

---

## 1. Diagnóstico

### 1.1 Rendimiento (PageSpeed Insights, laboratorio)

| Métrica | Móvil (15-11-2026, dato entregado) | Escritorio (16-11-2026 04:33 UTC, Supermetrics `pagespeed_check`) | Objetivo |
|---|---|---|---|
| Rendimiento | **35** | 53 | ≥ 90 escritorio, ≥ 75 móvil |
| Accesibilidad | 79 | 79 | ≥ 95 |
| Buenas prácticas | 92 | 96 | ≥ 95 |
| SEO | 100 | 100 | 100 |
| LCP | **24.3 s** | 10.0 s | **< 2.5 s** |
| CLS | **0.485** | 0.184 | **< 0.1** |
| TBT | 300 ms | 170 ms | < 200 ms |
| FCP | 2.3 s | 0.4 s | < 1.8 s |
| Speed Index | 17.2 s | 4.0 s | < 3.4 s |
| Ahorro: entrega de imágenes | 15.7 s | 5.25 s | — |
| Ahorro: caché | 2.45 s | 0.70 s | — |
| Ahorro: recursos que bloquean | 2.0 s | 0.65 s | — |

No hay datos de campo (CrUX): el tráfico real no alcanza el umbral de Chrome, así que el seguimiento será con laboratorio + GA4 (§ 3).

**Lectura:** el 80 % del problema son **imágenes** (ahorro de 15.7 s de 24.3 s): fotos subidas a tamaño de cámara, en PNG/JPG, sin `srcset` útil y probablemente con la imagen principal (hero) en carga diferida o como fondo CSS de Elementor, lo que retrasa el LCP. El CLS de 0.485 apunta a imágenes y carruseles sin dimensiones, fuentes web que cambian al cargar y bloques de Elementor que se insertan tarde.

### 1.2 Plataforma y dominio

| Elemento | Hallazgo | Fuente |
|---|---|---|
| CMS | WordPress + Elementor 4.3.4 | dato entregado |
| Hosting | Panel con Imunify (CloudLinux/cPanel típico); tipo de servidor web **por confirmar** (LiteSpeed o Apache) † | dato entregado; § 2.4 dice cómo confirmarlo |
| Redirección | `www` → `https://gammadiagnosticos.com/` | dato entregado |
| Certificado | Vence 08-02-2027 (renovación automática esperada) | Supermetrics `safety_check` |
| Dominio | Registrado 15-04-2021, **vence 15-04-2027** → renovar con autorrenovación | `safety_check` |
| Malware/phishing | Sin alertas (Google Web Risk) | `safety_check` |
| Correo | SPF y DKIM (`default`) presentes; **sin DMARC** (crítico para entregabilidad en Gmail/Yahoo) | Supermetrics `email_dns` |
| `.com.mx` | Página en blanco titulada «Gamma App»; certificado vence 13-02-2027; registro del dominio no disponible en la consulta | dato entregado; `safety_check` |
| Analítica | Sin GA4, GTM ni Meta Pixel; sí `google-site-verification` (Search Console ya verificada por alguien) | dato entregado |
| Vista al compartir | `og:image` de 500 × 682 px (vertical) → miniatura pequeña y recortada; LinkedIn no muestra descripción | Supermetrics `link_preview` |

### 1.3 Contenido y conversión (página de inicio)

| Hallazgo | Riesgo | Prioridad |
|---|---|---|
| Formulario «¿Necesitas información?» con **adjunto obligatorio de la orden médica**; Elementor guarda los adjuntos en `wp-content/uploads/elementor/forms/` con URL pública † | Dato sensible (salud) en carpeta pública, sin consentimiento expreso; LFPDPPP | **Crítica** |
| «Único centro autorizado en el sureste del país, para aplicación de Xofigo en Cáncer prostata» | Afirmación de exclusividad sin sustento visible; marca de medicamento de prescripción ante público general (§ 4) | **Crítica** |
| «Con más de 20 años de experiencia» en la página vs. «más de 10 años» en la meta descripción | Afirmación no comprobable/inconsistente (LGS 306 fr. I; LFPC 32) | Alta |
| Sin direcciones, horarios ni responsable sanitario por sede | Confianza, SEO local, cumplimiento | Alta |
| CDMX aparece bajo «Alianzas y Colaboraciones» como «Solo WhatsApp: 55 7460 8020» en texto plano | No es clicable; no queda claro si es sede propia | Alta |
| Teléfonos en texto, sin `tel:` ni botón de WhatsApp | Se pierden conversiones en móvil y no se pueden medir | Alta |
| Menú «Consultoría» y «Para el paciente» apuntan a `#`; «Solicita una cita» enlaza con `http://` | Navegación rota; contenido mixto | Media |
| Etiqueta «Message» en inglés; «Empresa méxicana» y «pais» sin acento | Calidad percibida | Baja |
| Página «Tienda» | Revisar qué vende: si ofrece insumos o medicamentos requiere otros permisos † | Media |
| Aviso de privacidad en `/privacy-policy/` (slug de plantilla en inglés) | Verificar contenido contra LFPDPPP 2025 (§ 3.2) | Alta |

**Limitación:** las páginas internas (`/privacy-policy/`, `/informacion-para-el-paciente/`, `/tratamiento-yodo-radiactivo-yodo-131-tratamiento/`) no se pudieron leer hoy (permiso de acceso no respondido). Revisarlas con la lista de verificación del § 8 antes del día 3.

---

## 2. Arreglos priorizados (WordPress/Elementor)

Antes de tocar nada: **respaldo completo** (archivos + base de datos) desde cPanel → Backup, o con UpdraftPlus; trabajar en un **staging** (Softaculous → Staging, o el de LiteSpeed/hosting) y publicar al final de cada bloque. Medir con PageSpeed después de cada bloque (`pagespeed_check` con `refresh=true`).

| # | Arreglo | Impacto esperado | Esfuerzo | Día |
|---|---|---|---|---|
| 1 | Imágenes: redimensionar, WebP/AVIF, `srcset` | LCP −10 a −15 s móvil | Medio | 2–3 |
| 2 | Imagen LCP: sin lazy-load, `fetchpriority="high"`, precarga | LCP −2 a −5 s | Bajo | 3 |
| 3 | Caché de página + navegador (LiteSpeed Cache o WP Rocket) | −2.45 s (caché), TTFB | Bajo | 2 |
| 4 | Dimensiones fijas y fuentes locales con `font-display: swap` | CLS 0.485 → < 0.1 | Medio | 4 |
| 5 | Diferir/retrasar JS y CSS no crítico | −2.0 s (bloqueo), TBT | Medio | 4–5 |
| 6 | CDN (QUIC.cloud o Cloudflare) | TTFB y descarga en todo México | Bajo | 5 |
| 7 | Limpieza de Elementor (experimentos de rendimiento, widgets sin uso) | −CSS/JS, DOM más chico | Bajo | 5 |

### 2.1 Imágenes (arreglo 1)

1. **Inventario:** Medios → vista de lista, ordenar por tamaño; o en cPanel → Administrador de archivos → `wp-content/uploads/` y revisar archivos > 300 KB. La imagen de `og:image` (`vinil-muestra1.png`, 2023) y los fondos del hero son los primeros candidatos.
2. **Redimensionar originales** a un máximo de 1920 px de ancho (hero) y 1200 px (contenido). Plugin: *Imsanity* o la opción de tamaño máximo del optimizador.
3. **Convertir a WebP/AVIF:**
   - Si el servidor es LiteSpeed: **LiteSpeed Cache → Image Optimization** → «Auto Request Cron» ON, «Create WebP/AVIF Versions» ON, «Image WebP/AVIF Replacement» ON, «Optimize Original Images» ON (con respaldo).
   - Si no: **ShortPixel** o **Imagify** (WebP + AVIF, entrega por `<picture>` o reescritura `.htaccess`), o **EWWW Image Optimizer**.
4. **Tamaños correctos en Elementor:** en cada widget Imagen elegir «Image Size» = *Large* o *Custom* al tamaño real mostrado (no *Full*). En móvil, usar el control responsivo para cargar una variante más pequeña.
5. **Hero como `<img>`, no como fondo CSS:** los fondos de sección de Elementor no tienen `srcset` ni prioridad. Reemplazar el fondo del hero por un widget Imagen (posición absoluta, `object-fit: cover`) o, si se mantiene el fondo, crear un fondo distinto para móvil (Elementor → Estilo → Fondo → vista móvil) a 800 px.
6. **Lazy-load para todo excepto la primera imagen visible:** WordPress lo aplica nativo; en LiteSpeed Cache → Page Optimization → Media → «Lazy Load Images» ON y en «Lazy Load Image Excludes» poner el nombre de archivo del hero; o «Add Missing Sizes» ON. En WP Rocket: Media → LazyLoad ON + excluir el hero.
7. Logos y pictogramas en **SVG** (con *Safe SVG*) o WebP pequeños.
8. Nueva **imagen para compartir** 1200 × 630 px (WebP/JPG < 200 KB) en el plugin SEO (Yoast/Rank Math → Social).

### 2.2 Precarga y prioridad de la imagen LCP (arreglo 2)

1. Identificar el elemento LCP en PageSpeed («Elemento de Largest Contentful Paint»).
2. Quitarle lazy-load (paso 2.1.6) y añadir `fetchpriority="high"`: WordPress 6.3+ lo hace para la primera imagen de contenido; para Elementor, usar en LiteSpeed Cache → Page Optimization → Media → «Preload Featured Image»/«LCP» o en WP Rocket → Media → «Optimize critical images» (Rocket 3.16+ detecta y precarga el LCP).
3. Si se necesita a mano (tema hijo, `functions.php` o *Code Snippets*):

```php
add_action('wp_head', function () {
  if (is_front_page()) {
    echo '<link rel="preload" as="image" fetchpriority="high" href="/wp-content/uploads/2026/11/hero-gamma-800.avif" imagesrcset="/wp-content/uploads/2026/11/hero-gamma-800.avif 800w, /wp-content/uploads/2026/11/hero-gamma-1600.avif 1600w" imagesizes="100vw" type="image/avif">' . "\n";
  }
}, 1);
```

4. Sin carruseles/sliders en el primer pantallazo: un slider retrasa el LCP y genera CLS. Sustituir por una imagen fija + titular.

### 2.3 Caché (arreglo 3)

**Confirmar el servidor:** Chrome → DevTools → Red → documento → encabezados de respuesta. `server: LiteSpeed` o `x-litespeed-cache` = LiteSpeed. En cPanel, la presencia de «LiteSpeed Web Cache Manager» también lo confirma. (Hoy no se pudieron leer los encabezados desde este entorno.)

| Si el servidor es… | Plugin | Ajustes clave |
|---|---|---|
| **LiteSpeed** (frecuente en hosting con CloudLinux/Imunify †) | **LiteSpeed Cache** (gratuito) | Cache → Enable ON; Browser Cache ON (TTL 31 536 000 para estáticos); Object Cache si hay Redis/Memcached; Page Optimization según § 2.5; excluir de caché `/registro-de-paciente/`, `/encuesta-de-satisfaccion/` y cualquier página con formulario si usa nonce |
| Apache/Nginx sin LiteSpeed | **WP Rocket** (pago, más sencillo) o **W3 Total Cache** (gratuito) | Caché de página ON, «Cache lifespan» 10 h, precarga del sitemap, caché de navegador ON; en W3TC: Page Cache «Disk: Enhanced», Browser Cache ON |

- **Nunca** dos plugins de caché a la vez; desactivar la caché propia de Elementor/Hosting que choque.
- Caché de navegador para estáticos (si el plugin no lo pone), en `.htaccess`:

```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/avif "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
</IfModule>
```

- Imunify360 puede bloquear el rastreador del optimizador de imágenes o de QUIC.cloud: si falla, poner sus IP en lista blanca desde cPanel → Imunify360 †.

### 2.4 Estabilidad visual: CLS (arreglo 4)

1. **Dimensiones en todas las imágenes:** en Elementor, Imagen → Estilo → ancho y alto fijos o «Aspect ratio»; WordPress añade `width`/`height` a las imágenes de la biblioteca. En LiteSpeed Cache → Media → «Add Missing Sizes» ON.
2. **Espacio reservado** para elementos que llegan tarde: mapas (iframe con `aspect-ratio: 16/9`), formularios, banner de cookies (que **se superponga**, no que empuje el contenido), botón flotante de WhatsApp (`position: fixed`).
3. **Fuentes locales:** Elementor → Configuración → Avanzado → «Google Fonts Load» = *Swap*; mejor aún, **Elementor → Fuentes personalizadas** (o *OMGF*) para servir las fuentes desde el propio dominio en WOFF2, con `font-display: swap`, y desactivar Google Fonts en Elementor (Configuración → Avanzado → «Google Fonts» = Desactivar). Precargar solo 1–2 archivos de fuente (titulares y texto). Usar un máximo de 2 familias y 3 pesos.
4. Ajuste de fuente de respaldo para que el cambio no mueva el texto (CSS):

```css
@font-face { font-family: "GammaSans"; src: url("/wp-content/uploads/fonts/gammasans-400.woff2") format("woff2"); font-weight: 400; font-display: swap; }
@font-face { font-family: "GammaSans-fallback"; src: local("Arial"); size-adjust: 104%; ascent-override: 92%; }
body { font-family: "GammaSans", "GammaSans-fallback", Arial, sans-serif; }
```

5. Quitar animaciones de entrada de Elementor («Entrance Animation») del primer pantallazo y de los contadores.

### 2.5 JS y CSS (arreglo 5)

- **LiteSpeed Cache → Page Optimization:** CSS Minify ON, CSS Combine OFF (probar), «Generate UCSS»/«Load CSS Asynchronously» con CCSS ON; JS Minify ON, «Load JS Deferred» = *Deferred* (o *Delayed* con exclusión de jQuery si rompe menús); «Remove WordPress Emoji» ON; «Remove Google Fonts» ON (si ya son locales).
- **WP Rocket:** File Optimization → minificar CSS/JS, «Remove unused CSS» ON, «Load JavaScript deferred» ON, «Delay JavaScript execution» ON (excluir el menú móvil si falla).
- **Elementor → Configuración → Funciones:** activar «Optimized DOM Output», «Improved Asset Loading», «Improved CSS Loading», «Inline Font Icons», «Lazy Load Background Images» (excepto el hero), y desactivar Font Awesome/eicons si no se usan.
- Desactivar plugins sin uso; *Asset CleanUp* o *Perfmatters* para no cargar WooCommerce/Tienda y formularios en páginas donde no hacen falta.
- Revisar en DevTools → Cobertura qué JS/CSS no se usa en inicio.

### 2.6 CDN (arreglo 6)

- **LiteSpeed:** QUIC.cloud (plan gratuito con cuota; CDN con caché de HTML) → LiteSpeed Cache → General → «Request Domain Key», CDN → QUIC.cloud ON.
- **Otro servidor:** **Cloudflare** (plan gratuito): mover los DNS de `gammadiagnosticos.com` a Cloudflare, proxy ON para `@` y `www`, SSL «Full (strict)», Brotli ON, caché de estáticos; con WP Rocket, su complemento de Cloudflare. Mantener los registros MX, SPF, DKIM y DMARC idénticos al migrar los DNS.

### 2.7 Accesibilidad (79 → ≥ 95) y correo

- Contraste de botones y texto sobre fotos (≥ 4.5:1), `alt` descriptivo en imágenes, etiquetas visibles en el formulario (en español), orden de encabezados H1→H2, tamaño táctil ≥ 48 px en móvil, atributo `lang="es-MX"`.
- **DMARC** en la zona DNS de `gammadiagnosticos.com` (cPanel → Zone Editor → TXT `_dmarc`): `v=DMARC1; p=none; rua=mailto:dmarc@gammadiagnosticos.com` (sugerencia de `email_dns`), y pasar a `p=quarantine` tras 4 semanas de informes limpios.

**Meta del bloque:** LCP < 2.5 s y CLS < 0.1 en laboratorio móvil al día 5; rendimiento móvil ≥ 75. Si con todo lo anterior el LCP sigue > 4 s, el cuello es el hosting (TTFB): pedir PHP 8.2+, OPcache y LiteSpeed, o cambiar de plan.

---

## 3. Medición

### 3.1 Site Kit by Google (GA4 + Search Console)

1. Instalar **Site Kit by Google**; conectar con la cuenta de Google corporativa (no personal). Search Console: Site Kit detecta la verificación existente; si la propiedad es de otra cuenta, pedir acceso de **propietario** al titular actual (Search Console → Configuración → Usuarios y permisos) en vez de verificar otra vez.
2. Crear propiedad **GA4** «GAMMA – sitio web» (zona horaria America/Mexico_City, moneda MXN), flujo web para `https://gammadiagnosticos.com`.
3. En GA4: Google Signals **OFF**, personalización de anuncios **OFF**, retención 14 meses, filtrar tráfico interno (IP de cada sede), sin User-ID.
4. **Etiquetas fuera de páginas de estudios y tratamientos** (regla del plan base, `docs/plan_publicidad_multicanal.md` § 6): Site Kit no excluye páginas por sí mismo, así que la etiqueta se coloca con **Google Tag Manager** (Site Kit puede instalarlo) y un activador «Todas las páginas *excepto* Ruta de página coincide con `^/(tratamiento|gammagrafia|ganglio|dolor|xofigo|radio-223|pet)`». Alternativa: filtro de Site Kit para bloquear la etiqueta por plantilla †.
5. Conectar Search Console con GA4 (Administrar → Vínculos de productos) y enviar el sitemap (`/sitemap_index.xml` de Yoast/Rank Math).

### 3.2 Consentimiento de cookies (LFPDPPP 2025)

La **LFPDPPP publicada en el DOF el 20-03-2025** sustituyó a la de 2010; las facultades del INAI pasaron a la Secretaría Anticorrupción y Buen Gobierno. Sigue exigiendo aviso de privacidad y **consentimiento expreso y por escrito** (incluye medios electrónicos) para **datos sensibles**, como los de salud ([LFPDPPP, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf)). La ley no exige un banner con opción previa para cookies de analítica, pero el aviso debe informar tecnologías de rastreo †; por ser un sitio de salud se adopta **opción previa (opt-in)**.

| Paso | Cómo |
|---|---|
| Plugin | **Complianz** o **CookieYes** o **Real Cookie Banner** (todos con Google Consent Mode v2 e integración con Site Kit/GTM) |
| Categorías | Necesarias (siempre), Analítica (GA4), Marketing (Meta/Google Ads, cuando existan) — todas **desactivadas por defecto** salvo las necesarias |
| Consent Mode v2 | `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization` = `denied` por defecto; se actualizan al aceptar |
| Texto del banner | «Usamos cookies necesarias para que el sitio funcione y, si lo aceptas, cookies de analítica para saber qué páginas se visitan. No usamos cookies en las páginas de estudios y tratamientos. [Aceptar] [Rechazar] [Configurar] · Aviso de privacidad» |
| Diseño | Superpuesto abajo (no empuja contenido: CLS), botón «Rechazar» con el mismo peso que «Aceptar» |
| Aviso de privacidad | Mover a `/aviso-de-privacidad/` (301 desde `/privacy-policy/`); integral y simplificado; responsable (razón social y domicilio), finalidades primarias/secundarias, **datos sensibles de salud** y su consentimiento expreso, cookies, transferencias, derechos ARCO y medio para ejercerlos, autoridad vigente (Secretaría Anticorrupción y Buen Gobierno), fecha de actualización; revisión por el despacho/oficial de privacidad |

### 3.3 Eventos de conversión (GTM → GA4, marcados como *eventos clave*)

| Evento | Disparo (GTM) | Parámetros | Nunca incluir |
|---|---|---|---|
| `click_whatsapp` | Clic en enlace cuyo URL empieza con `https://wa.me/52` | `sede` (MID, VHSA1, OAX, CDMX), `ubicacion` (header, flotante, pagina_sede) | Estudio, padecimiento, texto del mensaje |
| `click_tel` | Clic en enlace `tel:` | `sede`, `ubicacion` | — |
| `click_ruta` | Clic en enlace a Google Maps/Waze | `sede` | — |
| `generate_lead` | Envío correcto del formulario Elementor (evento `submit_success` vía *Elementor → Acciones tras enviar → Redirección a página de gracias* `/gracias/?sede=MID`, activador «Vista de página /gracias/») | `sede`, `tipo` (informacion, empleo, b2b) | Nombre, correo, teléfono, estudio |
| `click_correo` | Enlace `mailto:` | `sede` | — |

- Implementación por sede: cada botón lleva `data-sede="MID"` (Elementor → Avanzado → Atributos: `data-sede|MID`) y una variable GTM de «Atributo del elemento» lee `data-sede`.
- Llamadas: si se contratan números de seguimiento por canal (plan base) †, usar los del proveedor solo en las páginas de campaña.

### 3.4 UTMs de ejemplo (generadas y validadas con Supermetrics `utm_build`)

Convención del repositorio (`docs/plan_publicidad_multicanal.md` § 6): `utm_campaign` = `{sede}_{objetivo}_{aaaamm}`, `utm_content` = id de pieza, **nunca** un padecimiento o estudio sensible en la UTM. `utm_build` usa por defecto guiones y marcó los guiones bajos solo como estilo; para que la herramienta no los marque, guardar la convención del equipo en Supermetrics (`manage_business_context`, etiqueta `utm-conventions`, `"separator":"_"`).

| Canal | Sede | Enlace |
|---|---|---|
| Google Business Profile (botón «Sitio web») | MID | `https://gammadiagnosticos.com/sedes/merida/?utm_source=google&utm_medium=organic&utm_campaign=gbp_ficha_202612&utm_content=boton_sitio` |
| Google Business Profile | VHSA1 | `https://gammadiagnosticos.com/sedes/villahermosa/?utm_source=google&utm_medium=organic&utm_campaign=gbp_ficha_202612&utm_content=boton_sitio` |
| Google Business Profile | OAX | `https://gammadiagnosticos.com/sedes/oaxaca/?utm_source=google&utm_medium=organic&utm_campaign=gbp_ficha_202612&utm_content=boton_sitio` |
| Google Ads (Search) | OAX | `https://gammadiagnosticos.com/sedes/oaxaca/?utm_source=google&utm_medium=cpc&utm_campaign=oax_estudios_202701&utm_content=mc-oax-google-202701-01` |
| Meta Ads | MID / VHSA1 / OAX | `https://gammadiagnosticos.com/sedes/merida/?utm_source=meta&utm_medium=paid_social&utm_campaign=sur_estudios_202701&utm_content=mc-sur-meta-202701-01` (misma cadena en `/sedes/villahermosa/` y `/sedes/oaxaca/`) |
| LinkedIn Ads (médicos referentes) | MID | `https://gammadiagnosticos.com/sedes/merida/?utm_source=linkedin&utm_medium=paid_social&utm_campaign=mid_referentes_202701&utm_content=mc-mid-linkedin-202701-01` |
| QR en congreso (stand) | VHSA1 | `https://gammadiagnosticos.com/sedes/villahermosa/?utm_source=congreso&utm_medium=referral&utm_campaign=vhsa1_congreso_202702&utm_content=mc-vhsa1-qr-202702-01` |

Hallazgos de la validación que corrigen el plan base:

1. **`utm_medium=qr` queda como «Unassigned» en GA4** (aviso de `utm_build`). Usar `referral` (como arriba) o crear un grupo de canales personalizado «Offline / QR» en GA4.
2. Con Google Ads, activar **etiquetado automático** (`gclid`); las UTM manuales sirven para GA4 sin vincular cuentas. Macros válidas: Google `{campaignid}`, Meta `{{campaign.name}}`/`{{campaign.id}}`, LinkedIn `{{CAMPAIGN_NAME}}`.
3. `utm_source=meta` podría no entrar en «Paid Social» de GA4 porque la lista de fuentes sociales reconoce `facebook`/`instagram` †; alternativa: `utm_source={{site_source_name}}` (macro de Meta) o un grupo de canales personalizado.
4. Las rutas `/sedes/...` aún no existen: se crean en el § 7.

---

## 4. Cumplimiento sanitario de la publicidad en la web

### 4.1 Qué dice la norma (fuentes oficiales)

| Norma y artículo | Qué exige | Aplicación al sitio |
|---|---|---|
| [LGS art. 300](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico) | Compete a la Secretaría de Salud autorizar la publicidad sobre salud, tratamiento de enfermedades y servicios | El sitio que promueve servicios es publicidad sujeta a control |
| [LGS art. 301 y 301 Bis](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico) | Requiere autorización la publicidad de los productos y servicios que señale el reglamento; el reglamento define cuándo basta un aviso | Remite al RLGSMP arts. 79 y 86 |
| [LGS art. 306](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico) | La información «deberá ser comprobable» (fr. I); contenido orientador y educativo (fr. II); corresponder a la autorización sanitaria (fr. III); no contravenir principios de prevención y tratamiento (fr. V) | «Único centro autorizado» y «20 años» deben poder probarse con documentos |
| [LGS art. 310](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico) | La publicidad de medicamentos al **público general** solo puede referirse a medicamentos de **libre venta** y remedios herbolarios | **Xofigo** (dicloruro de radio-223) es de prescripción: no nombrar la marca ante público general; describir el **servicio** |
| [LGS art. 312](https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico) | La Secretaría puede exigir textos de advertencia de riesgos | Atender lo que indique el permiso |
| [LGS art. 83](https://mley.mx/LGS/articulo/83/) | Quien ejerza actividades profesionales o especialidades médicas debe mostrar institución que expidió el título, **número de cédula** y certificado de especialidad; «iguales menciones» en su **publicidad** | Si la web presenta médicos: nombre del cargo + institución + cédula profesional y de especialidad |
| [RLGSMP art. 79 fr. I](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) | Requiere **permiso** la publicidad de «Prestación de servicios de salud, salvo cuando se trate de servicios otorgados en forma individual» | Las páginas de servicios de las sedes requieren **permiso** (modalidad A del 02-001 tras la simplificación 2025, ver `docs/legal/aviso_cofepris_02-002-A.md`) |
| [RLGSMP art. 86 fr. I y 87](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) | **Aviso** para actividades profesionales, ≥ 5 días antes de difundir | Perfiles individuales de médicos |
| [RLGSMP arts. 6, 7 y 9](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) (última reforma DOF 08-09-2022) | Publicidad congruente con la autorización; orientadora y educativa, en español claro, con precauciones si hay riesgos; «no comprobable» la que induce a error, exagera propiedades u oculta contraindicaciones | Indicaciones de preparación y protección radiológica deben acompañar la información de I-131 y radio-223 |
| [RLGSMP arts. 16–19](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) | Servicios de salud: informar tipo, características, finalidades y modalidades de acceso (16); no autorizar si ofrece tratamientos sin eficacia comprobada o sin acreditar personal y recursos (18); profesionales expresan institución del título y **cédula** (19) | Describir cada servicio con su finalidad y requisitos (orden médica, preparación) |
| [RLGSMP art. 78](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) | El anunciante entrega al medio copia del permiso o aviso | Conservar acuse/permiso; en la web propia, archivarlo en `compliance/` |
| [RLGSMP arts. 80–83](https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf) | La solicitud de permiso incluye proyecto y **sustento de las afirmaciones**; el permiso es por tiempo indeterminado; **no se puede modificar** la publicidad autorizada sin nuevo trámite | Cada rediseño de contenido promocional = nuevo permiso o modificación |
| [LFPC art. 32](https://mley.mx/LFPC/articulo/32/) | Publicidad «veraz, comprobable, clara», sin elementos que induzcan a error; comparativa permitida si no es engañosa; prohibido decir «avalado/certificado» sin respaldo | Aplica además de la LGS (PROFECO) |

### 4.2 ¿Debe aparecer el número de permiso, el responsable sanitario y leyendas?

- **Número de permiso/aviso en el anuncio:** el RLGSMP **no contiene una obligación general** de imprimirlo en la pieza; el número se usa en la solicitud y ante los medios (arts. 78, 80, 87). La única obligación de clave visible es el **registro sanitario** en publicidad de medicamentos a profesionales (art. 42). Aun así, es práctica común y recomendable mostrar «Permiso de publicidad COFEPRIS No. ______» en el pie del sitio, porque facilita la verificación y lo piden algunas plataformas †.
- **Responsable sanitario y cédula:** la obligación de publicitar **cédula** es del profesional (LGS art. 83; RLGSMP art. 19). La figura del responsable sanitario del establecimiento es obligatoria en su licencia/aviso de funcionamiento; mostrar en cada página de sede «Responsable sanitario: [cargo], cédula profesional ____ y de especialidad ____ ([institución])» cumple ambas a la vez y es lo que esperará el dictaminador †.
- **Leyendas:** la LGS solo fija «Consulte a su médico» para medicamentos de libre venta (art. 310); para servicios, la Secretaría las determina en el permiso (art. 312). Mientras tanto, usar: «Estudio o tratamiento bajo prescripción médica. Requiere orden de su médico.» y, en I-131 y radio-223, «Siga las indicaciones de protección radiológica que le dará el personal de la sede.» †
- **Licencia sanitaria y licencia de la CNSNS:** si se mencionan («centro autorizado»), indicar número y autoridad; es la forma de hacer comprobable la afirmación (LGS 306 fr. I y III).

### 4.3 «Único centro autorizado en el sureste del país» y la marca Xofigo

- **No está prohibida** la afirmación de exclusividad por sí misma (no hay en LGS/RLGSMP una prohibición expresa de superioridad para servicios; las de los arts. 9 fr. V, 22 y 70 se refieren a productos), pero **debe ser comprobable** (LGS 306 fr. I; RLGSMP arts. 6 y 9; LFPC art. 32) y el **sustento se entrega** con la solicitud de permiso (RLGSMP art. 80). Probar «único en el sureste» exige demostrar un hecho negativo sobre todos los demás establecimientos de una región indefinida y en una fecha: es frágil y caduca en cuanto otro centro obtenga licencia.
- **«Autorizado»** implica una autoridad concreta (licencia sanitaria COFEPRIS + licencia de la CNSNS para radio-223) que hoy no se cita.
- **Xofigo** es la **marca** de un medicamento de prescripción: nombrarla ante el público general puede tomarse como publicidad de medicamento no permitida (LGS art. 310) †. Usar el nombre del procedimiento.
- **Recomendación:** retirarla ya (el sitio hoy no tiene permiso visible) y sustituirla por una redacción verificable:

| Hoy | Propuesta |
|---|---|
| «Único centro autorizado en el sureste del país, para aplicación de Xofigo en Cáncer prostata.» | «**Terapia con radio-223 para metástasis óseas de cáncer de próstata**, en [sede] con licencia sanitaria ____ y licencia de la CNSNS ____. Requiere indicación de su oncólogo o urólogo.» |
| (alternativa si se documenta la exclusividad) | «Uno de los pocos centros del sureste con licencia para terapia con radio-223 (consultado en ____ el __/__/____).» — solo con la evidencia archivada en `compliance/` y aprobada en el permiso |
| «Con más de 20 años de experiencia» / «más de 10 años» | Un solo dato comprobable: «Desde [año de la primera licencia] en medicina nuclear» |
| «Somos Especialistas» | «Equipo de médicos especialistas en medicina nuclear (cédulas en cada sede)» |
| «Empresa con presencia en todo México» | «Sedes en Mérida, Villahermosa y Oaxaca; atención por WhatsApp en Ciudad de México» (según lo que realmente opere) |

---

## 5. WhatsApp por sede

**Regla:** WhatsApp sirve para logística (horarios, requisitos, agendar). **Nunca** para resultados, informes, imágenes ni preguntas clínicas (política de WhatsApp Business y plan base § 3.6).

### 5.1 Botón click-to-chat

| Sede | Número (público en el sitio) | Enlace con mensaje predefinido |
|---|---|---|
| Mérida (MID) | 999 109 5578 † (confirmar que tiene WhatsApp) | `https://wa.me/529991095578?text=Hola%2C%20quisiera%20informaci%C3%B3n%20de%20horarios%20y%20requisitos%20para%20agendar%20en%20la%20sede%20M%C3%A9rida.` |
| Villahermosa (VHSA1) | 993 399 9582 † | `https://wa.me/529933999582?text=Hola%2C%20quisiera%20informaci%C3%B3n%20de%20horarios%20y%20requisitos%20para%20agendar%20en%20la%20sede%20Villahermosa.` |
| Oaxaca (OAX) | 951 579 3304 † | `https://wa.me/529515793304?text=Hola%2C%20quisiera%20informaci%C3%B3n%20de%20horarios%20y%20requisitos%20para%20agendar%20en%20la%20sede%20Oaxaca.` |
| Ciudad de México | 55 7460 8020 («Solo WhatsApp») | `https://wa.me/525574608020?text=Hola%2C%20quisiera%20informaci%C3%B3n%20de%20horarios%20y%20requisitos%20para%20agendar%20en%20la%20sede%20Ciudad%20de%20M%C3%A9xico.` |

Mensaje decodificado: «Hola, quisiera información de horarios y requisitos para agendar en la sede [sede].» No menciona estudio ni padecimiento.

**Implementación en Elementor:**
1. En cada página de sede: widget Botón «Escribir por WhatsApp» con el enlace de su sede, atributo `data-sede|MID`, `rel="noopener"`, abrir en pestaña nueva.
2. Botón flotante global: un selector «¿A qué sede?» (Elementor Popup con los 4 botones) en vez de un solo número. Plugin opcional: *Click to Chat* (HoliThemes) o *Joinchat*, con número por página.
3. Teléfonos como enlaces `tel:+529991095578`, etc.
4. Debajo del botón, en letra pequeña: «Al escribirnos aceptas el [aviso de privacidad](/aviso-de-privacidad/). Por WhatsApp solo damos información de horarios y citas; **no envíes órdenes médicas, resultados ni datos de salud** por este medio.»

### 5.2 Horarios

Publicar en cada página de sede y en la ficha de Google el horario de atención por WhatsApp y teléfono (p. ej., «Lun–vie 8:00–18:00, sáb 8:00–13:00» †, a confirmar por sede) y un mensaje de ausencia automático en WhatsApp Business: «Gracias por escribir a GAMMA [sede]. Nuestro horario es ____. Te responderemos el siguiente día hábil. Para una urgencia médica acude a tu servicio de urgencias.»

### 5.3 Canal para resultados (no WhatsApp)

| Opción | Cómo | Nota |
|---|---|---|
| **Portal de resultados** con usuario y contraseña (o enlace + código de un solo uso por SMS/correo) | Visor web del PACS/RIS o el portal de GAMMA OS; enlace «Consultar resultados» en el menú | Preferida; registro de accesos |
| Entrega presencial o al médico tratante | En la sede, con identificación | Siempre disponible |
| Correo con archivo cifrado (contraseña enviada por otro medio) | Solo si el paciente lo pide por escrito | Respaldo |

Quitar el **adjunto obligatorio de la orden médica** del formulario de inicio. Si se necesita la orden antes de la cita, pedirla en el portal seguro o en la sede; mientras tanto, borrar los archivos ya recibidos en `wp-content/uploads/elementor/forms/` tras resguardarlos en el expediente, y bloquear la carpeta (`.htaccess`: `Require all denied`) †.

---

## 6. Dominio `gammadiagnosticos.com.mx`

Hoy sirve una página en blanco «Gamma App» con certificado válido: confunde a quien lo escribe y puede indexarse vacía. Antes de decidir, **preguntar a sistemas qué es «Gamma App»** (¿una aplicación interna en desarrollo?).

| Opción | Cuándo | Pasos |
|---|---|---|
| **A. Redirección 301 a la `.com`** | La app no se usa o puede moverse | cPanel → Dominios → añadir `gammadiagnosticos.com.mx` como **alias** (dominio estacionado) de la cuenta → cPanel → **Redirecciones**: tipo *Permanente (301)*, `gammadiagnosticos.com.mx` → `https://gammadiagnosticos.com/`, «Redirigir con o sin www» y «Redirección comodín» (conserva la ruta) ON. O en el `.htaccess` del docroot del `.com.mx`: ver bloque abajo |
| **B. Subdominio para la app** | La app sí se usa | Mover la app a `app.gammadiagnosticos.com` (cPanel → Dominios → Crear subdominio, docroot propio, SSL AutoSSL) y aplicar la opción A al `.com.mx`; o mantenerla en `app.gammadiagnosticos.com.mx` y redirigir solo la raíz y `www`. En la app: `X-Robots-Tag: noindex` y acceso con inicio de sesión |
| C. Dejarla como está | No recomendado | — |

```apache
# .htaccess en el docroot de gammadiagnosticos.com.mx (opción A)
RewriteEngine On
RewriteCond %{HTTP_HOST} ^(www\.)?gammadiagnosticos\.com\.mx$ [NC]
RewriteRule ^(.*)$ https://gammadiagnosticos.com/$1 [R=301,L]
```

**DNS:** si el `.com.mx` está en otro registrador (NIC México/Akky u otro), apuntar sus registros `A` de `@` y `www` a la IP del hosting de la `.com` (la que muestra cPanel → Información general), o, con Cloudflare, añadir la zona y crear una *Redirect Rule* 301. Activar **autorrenovación** de ambos dominios (la `.com` vence el 15-04-2027). Si el `.com.mx` no envía correo, publicar SPF `v=spf1 -all` y DMARC `p=reject` para impedir suplantación. Verificar con `link_check` y `safety_check` de Supermetrics que la cadena sea una sola redirección 301.

---

## 7. SEO local

### 7.1 Páginas por sede

Crear `/sedes/merida/`, `/sedes/villahermosa/`, `/sedes/oaxaca/` y `/sedes/cdmx/` (esta última solo si es sede o punto de atención real; si es aliado, página «Atención en CDMX» sin dirección propia). Cada página con plantilla de Elementor idéntica:

1. H1 «Medicina nuclear en [ciudad] — GAMMA [sede]».
2. Dirección completa, mapa (iframe con dimensiones fijas), cómo llegar, estacionamiento.
3. Horario, teléfono `tel:`, botón WhatsApp de la sede (§ 5).
4. Servicios **disponibles en esa sede** (solo los autorizados ahí), cada uno con finalidad, requisitos (orden médica), preparación y duración.
5. Responsable sanitario (cargo, cédula profesional y de especialidad, institución), licencia sanitaria y, si aplica, licencia CNSNS.
6. «Permiso de publicidad COFEPRIS No. ____» en el pie.
7. JSON-LD (§ 7.2) y enlace al aviso de privacidad.

Título SEO: «Medicina nuclear y gammagrafía en Mérida | GAMMA Diagnósticos» (≤ 60 caracteres); meta descripción de 150–160 caracteres sin promesas de resultado.

### 7.2 Schema.org `MedicalClinic` (JSON-LD de ejemplo)

Datos públicos del sitio hoy: nombre, ciudad, teléfono, correo `info@gammadiagnosticos.com`. Los campos `____` se completan con la dirección y horario reales; **no publicar con marcadores vacíos**. Insertarlo con el bloque «Esquema personalizado» de Rank Math, o un widget HTML de Elementor en la página de la sede.

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "https://gammadiagnosticos.com/sedes/merida/#clinic",
  "name": "GAMMA Diagnósticos Mérida",
  "url": "https://gammadiagnosticos.com/sedes/merida/",
  "telephone": "+52 999 109 5578",
  "email": "info@gammadiagnosticos.com",
  "image": "https://gammadiagnosticos.com/wp-content/uploads/2026/11/gamma-merida-fachada-1200.webp",
  "logo": "https://gammadiagnosticos.com/wp-content/uploads/2026/11/gamma-logo.svg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "____",
    "addressLocality": "Mérida",
    "addressRegion": "Yucatán",
    "postalCode": "____",
    "addressCountry": "MX"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "____", "longitude": "____" },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "____", "closes": "____" }
  ],
  "medicalSpecialty": ["Radiography", "Oncologic", "Endocrine"],
  "availableService": [
    { "@type": "MedicalTest", "name": "Gammagrafía" },
    { "@type": "MedicalTest", "name": "PET/CT" },
    { "@type": "MedicalTherapy", "name": "Tratamiento con yodo-131" },
    { "@type": "MedicalProcedure", "name": "Localización de ganglio centinela" },
    { "@type": "MedicalTherapy", "name": "Tratamiento paliativo del dolor óseo" }
  ],
  "parentOrganization": {
    "@type": "MedicalOrganization",
    "@id": "https://gammadiagnosticos.com/#organization",
    "name": "GAMMA Diagnósticos",
    "url": "https://gammadiagnosticos.com/"
  },
  "sameAs": ["____ (URL de la ficha de Google Business de la sede)"]
}
```

Para Villahermosa y Oaxaca cambiar `@id`, `name`, `url`, `telephone` (`+52 993 399 9582`, `+52 951 579 3304`), `addressLocality`/`addressRegion` (Villahermosa/Tabasco; Oaxaca de Juárez/Oaxaca) y la lista `availableService` a lo que ofrezca cada sede. `schema.org` no tiene una especialidad «medicina nuclear»: `Radiography` es la más cercana †. Validar en [Rich Results Test](https://search.google.com/test/rich-results) y en el validador de schema.org.

### 7.3 Fichas de Google Business Profile

| Tarea | Detalle |
|---|---|
| Reclamar/verificar | Una ficha por sede física; CDMX solo si hay dirección con atención presencial (si no, ficha de «área de servicio» †) |
| Nombre | Exactamente el nombre comercial, sin palabras clave añadidas («GAMMA Diagnósticos Mérida») |
| Categoría principal | «Centro de medicina nuclear» o la más cercana disponible †; secundarias: «Centro de diagnóstico por imagen», «Clínica de oncología» † |
| NAP | Nombre, dirección y teléfono **idénticos** al sitio y al JSON-LD |
| Sitio web | Enlace con UTM de la sede (§ 3.4) |
| Horario | El mismo del sitio, con días festivos |
| Fotos | Fachada, recepción, acceso; nunca pacientes ni pantallas con datos |
| Servicios | Lista neutra (sin promesas, sin marca de medicamentos) |
| Mensajería / reseñas | Responder reseñas sin confirmar que alguien es paciente ni hablar de su caso |
| Publicaciones | Solo informativas; las promocionales pasan por el checklist del plan base § 9 |

---

## 8. Checklist y cronograma de 2 semanas (16 al 27 de noviembre de 2026)

### 8.1 Checklist

**Urgente (día 1)**
- [ ] Retirar la frase «Único centro autorizado…» y la marca Xofigo; unificar años de experiencia
- [ ] Quitar el adjunto obligatorio del formulario; resguardar y borrar adjuntos previos; bloquear la carpeta de formularios
- [ ] Respaldo completo y staging
- [ ] Confirmar tipo de servidor (LiteSpeed sí/no) y acceso a cPanel, DNS y Search Console
- [ ] Leer páginas internas (privacidad, información para el paciente, I-131, Tienda) y anotar afirmaciones

**Rendimiento**
- [ ] Plugin de caché único configurado (§ 2.3)
- [ ] Imágenes redimensionadas y en WebP/AVIF; hero como `<img>` sin lazy-load con `fetchpriority="high"`
- [ ] Fuentes locales con `font-display: swap`; Google Fonts de Elementor desactivadas
- [ ] Dimensiones fijas en imágenes, mapas y banners; sin slider ni animaciones arriba
- [ ] JS diferido, CSS crítico; experimentos de rendimiento de Elementor activos
- [ ] CDN activo
- [ ] PageSpeed móvil: LCP < 2.5 s, CLS < 0.1, rendimiento ≥ 75

**Medición y privacidad**
- [ ] Aviso de privacidad actualizado a LFPDPPP 2025, en `/aviso-de-privacidad/` con 301
- [ ] Banner de consentimiento con Consent Mode v2 (opt-in)
- [ ] Site Kit + GA4 + Search Console vinculados; GTM excluye páginas de estudios/tratamientos
- [ ] Eventos `click_whatsapp`, `click_tel`, `click_ruta`, `generate_lead` como eventos clave, con `sede`
- [ ] DMARC `p=none` publicado

**Contenido y cumplimiento**
- [ ] Páginas por sede con responsable sanitario, cédulas, licencias y horario
- [ ] Redacciones del § 4.3 revisadas por médico nuclear y despacho
- [ ] Solicitud de **permiso de publicidad** COFEPRIS del sitio (proyecto + sustento) y número en el pie al obtenerlo
- [ ] Botones WhatsApp por sede con aviso; canal de resultados publicado (portal)

**Dominio y SEO local**
- [ ] Decisión sobre «Gamma App»; 301 o subdominio aplicado; autorrenovación de ambos dominios
- [ ] JSON-LD por sede validado
- [ ] Fichas de Google Business con NAP idéntico y UTM
- [ ] Nueva `og:image` 1200 × 630 y caché de LinkedIn/Facebook refrescada

### 8.2 Cronograma

| Día | Fecha | Bloque | Entregable | Responsable |
|---|---|---|---|---|
| 1 | lun 16-nov | Urgencias de cumplimiento y privacidad; respaldo; staging | Frase y adjunto retirados | Web + Calidad |
| 2 | mar 17-nov | Caché + CDN de prueba; inventario de imágenes | Plugin de caché activo | Web |
| 3 | mié 18-nov | Optimización de imágenes y hero/LCP | LCP < 6 s móvil | Web |
| 4 | jue 19-nov | CLS: dimensiones, fuentes locales, sin slider | CLS < 0.1 | Web |
| 5 | vie 20-nov | JS/CSS diferido, CDN definitivo; medición | LCP < 2.5 s, informe PageSpeed | Web + MarCo |
| 6 | lun 23-nov | Aviso de privacidad + banner + Site Kit/GA4/GTM | Analítica con consentimiento | MarCo + Privacidad |
| 7 | mar 24-nov | Eventos de conversión, DMARC, `.com.mx` | Eventos visibles en GA4 DebugView | Web + Sistemas |
| 8 | mié 25-nov | Páginas por sede + WhatsApp + JSON-LD | 3–4 páginas en staging | Web + Sedes |
| 9 | jue 26-nov | Revisión médica, radiológica y legal; armado de la solicitud de permiso | Proyecto para COFEPRIS | Médico nuclear + Despacho |
| 10 | vie 27-nov | Publicación, fichas de Google, `og:image`, prueba final | Sitio en producción + informe de cierre | Todos |

Después del día 10: no difundir campañas que lleven al sitio hasta tener el permiso de publicidad (plan base); revisar PageSpeed y GA4 cada semana en el tablero de MarCo.

---

## Fuentes

Consultadas el 15/16-11-2026.

- Reglamento de la LGS en Materia de Publicidad (texto oficial, Cámara de Diputados; última reforma DOF 08-09-2022): https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LGS_MP.pdf
- RLGSMP art. 79 (consulta): https://mley.mx/Reg_LGS_MP/articulo/79/
- Ley General de Salud, Título Décimo Tercero (arts. 300–312): https://mexico.justia.com/federales/leyes/ley-general-de-salud/titulo-decimo-tercero/capitulo-unico — el PDF oficial https://www.diputados.gob.mx/LeyesBiblio/pdf/LGS.pdf no se pudo abrir hoy (permiso no respondido): cotejar antes del trámite
- LGS art. 83: https://mley.mx/LGS/articulo/83/
- Ley Federal de Protección al Consumidor art. 32: https://mley.mx/LFPC/articulo/32/
- LFPDPPP (DOF 20-03-2025): https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf †
- Acuerdo de simplificación de trámites COFEPRIS 2025 (SIDOF): https://sidof.segob.gob.mx/notas/docFuente/5756000
- Manual COFEPRIS de aviso de publicidad: https://www.gob.mx/cms/uploads/attachment/file/795383/Manual_Aviso_de_Publicidad.pdf
- Supermetrics Marketing Utilities (`pagespeed_check` escritorio, `email_dns`, `link_preview`, `safety_check`, `utm_build`), 16-11-2026
- Página de inicio de gammadiagnosticos.com (lectura del 15-11-2026)
- Documentos relacionados: `docs/plan_publicidad_multicanal.md`, `docs/legal/aviso_cofepris_02-002-A.md`, `compliance/checklist.md`
