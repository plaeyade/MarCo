import math, os, sys
OUT = sys.argv[1]
C = "#5250CC"
S = 'fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'

def P(d): return f'<path d="{d}" {S}/>'
def circ(cx,cy,r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" {S}/>'
def dot(cx,cy,r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{{c}}"/>'

def arcpts(cx,cy,r,a):
    a=math.radians(a); return cx+r*math.cos(a), cy+r*math.sin(a)

# 0 actual
L = {}
L["m0_actual"] = ("Actual: γ con arcos de emisión", [
 P("M6 11.5 C10 11 12.8 14 14.8 19.5 L19 30.5 L26 10.5"),
 P("M19 30.5 C15.4 35.5 15.6 40.5 19 40.5 C22.4 40.5 22.6 35.5 19 30.5"),
 P("M29.4 18.6 a7 7 0 0 1 0 10.8 M32.5 14.6 a12 12 0 0 1 0 18.8 M35.5 10.6 a17 17 0 0 1 0 26.8")])

# 1 monograma M+C con arco de emision
x1,y1 = arcpts(22,24,17,-42); x2,y2 = arcpts(22,24,17,42)
L["m1_monograma"] = ("Monograma M+C con arco de emisión", [
 P(f"M{x1:.2f} {y1:.2f} A17 17 0 1 0 {x2:.2f} {y2:.2f}"),
 P("M14 30 V18 L20.5 25 L27 18 V30"),
 P("M38 19.5 a6 6 0 0 1 0 9"),
 P("M42.5 15.5 a11.5 11.5 0 0 1 0 17")])

# 2 gamma como burbuja de dialogo
L["m2_burbuja"] = ("γ en burbuja de diálogo", [
 P("M11 7 H37 a5 5 0 0 1 5 5 V29 a5 5 0 0 1 -5 5 H23 L14 42 V34 H11 a5 5 0 0 1 -5 -5 V12 a5 5 0 0 1 5 -5 Z"),
 P("M14.5 13 C17.5 13 19.3 15 20.6 18.5 L23.5 25 L29.5 13"),
 P("M23.5 25 C21.6 27.6 21.8 29.6 23.5 29.6 C25.2 29.6 25.4 27.6 23.5 25")])

# 3 ondas concentricas tipo gammagrafia formando M
L["m3_gammagrafia"] = ("Isocontornos de gammagrafía que forman una M", [
 P("M6 41 V23 a9 9 0 0 1 18 0 a9 9 0 0 1 18 0 V41"),
 P("M24 23 V33"),
 P("M11.5 35 V23 a3.5 3.5 0 0 1 7 0 V35"),
 P("M29.5 35 V23 a3.5 3.5 0 0 1 7 0 V35")])

# 4 megafono + centelleo
L["m4_megafono"] = ("Megáfono con centelleo", [
 P("M7 20 V28 H13 L27 36 V12 L13 20 Z"),
 P("M13 28 L15.5 37 H19.5 L18 31"),
 P("M38 13.5 Q38 24 46 24 Q38 24 38 34.5 Q38 24 30 24 Q38 24 38 13.5 Z")])

# 5 C como orbita (isotipo)
x1,y1 = arcpts(24,24,18,-38); x2,y2 = arcpts(24,24,18,38)
dx,dy = arcpts(24,24,18,-38)
L["m5_orbita"] = ("C como órbita con fotón", [
 P(f"M{x1:.2f} {y1:.2f} A18 18 0 1 0 {x2:.2f} {y2:.2f}"),
 circ(24,24,5.5),
 dot(round(dx,2),round(dy,2),3.6)])

# 6 red de referentes
hub=(24,24); hr=5; nr=3.2; R=17
parts=[circ(24,24,hr)]
for k in range(5):
    a=-90+72*k
    nx,ny=arcpts(24,24,R,a)
    parts.append(circ(round(nx,2),round(ny,2),nr))
    sx,sy=arcpts(24,24,hr+1.6,a); ex,ey=arcpts(24,24,R-nr-1.6,a)
    parts.append(P(f"M{sx:.2f} {sy:.2f} L{ex:.2f} {ey:.2f}"))
L["m6_red"] = ("Red de referentes con nodo GAMMA", parts)

def icon_svg(key, color, title):
    body = "\n  ".join(x.replace("{c}",color).replace(C,color) for x in L[key][1])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48" role="img" aria-label="MarCo — {title}">
  <title>MarCo — {title}</title>
  {body.replace(C,color)}
</svg>
'''

def wordmark_svg(key, color, title, text_color=None):
    tc = text_color or color
    body = "\n    ".join(x.replace("{c}",color).replace(C,color) for x in L[key][1])
    if key=="m5_orbita":
        # C de MarCo dibujada como orbita
        x1,y1 = arcpts(0,0,11,-38); x2,y2 = arcpts(0,0,11,38)
        word = f'''<text x="64" y="38" font-family="Inter, 'Source Sans 3', Arial, sans-serif" font-size="30" font-weight="600" fill="{tc}">Mar</text>
    <g transform="translate(134 27)"><path d="M{x1:.2f} {y1:.2f} A11 11 0 1 0 {x2:.2f} {y2:.2f}" fill="none" stroke="{tc}" stroke-width="3.4" stroke-linecap="round"/><circle cx="{x1:.2f}" cy="{y1:.2f}" r="2.6" fill="{tc}"/></g>
    <text x="145" y="38" font-family="Inter, 'Source Sans 3', Arial, sans-serif" font-size="30" font-weight="600" fill="{tc}">o</text>'''
    else:
        word = f'<text x="64" y="38" font-family="Inter, \'Source Sans 3\', Arial, sans-serif" font-size="30" font-weight="600" fill="{tc}">MarCo</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 64" width="300" height="64" role="img" aria-label="MarCo — GAMMA Marketing &amp; Communication">
  <title>MarCo — GAMMA Marketing &amp; Communication</title>
  <g transform="translate(4 8)">
    {body}
  </g>
  {word}
  <text x="65" y="56" font-family="Inter, 'Source Sans 3', Arial, sans-serif" font-size="11.5" font-weight="500" letter-spacing="0.4" fill="{tc}">GAMMA · Marketing &amp; Communication</text>
</svg>
'''

os.makedirs(OUT, exist_ok=True)
for k,(t,_) in L.items():
    open(f"{OUT}/marco_{k}.svg","w").write(icon_svg(k,C,t))
    open(f"{OUT}/marco_{k}_wordmark.svg","w").write(wordmark_svg(k,C,t))
    open(f"{OUT}/marco_{k}_dark.svg","w").write(icon_svg(k,"#9C9AF2",t))
    open(f"{OUT}/marco_{k}_wordmark_dark.svg","w").write(wordmark_svg(k,"#9C9AF2",t))
import json; json.dump({k:v[0] for k,v in L.items()}, open(f"{OUT}/titles.json","w"), ensure_ascii=False, indent=1)
