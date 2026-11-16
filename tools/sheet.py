import re, json, sys
D = sys.argv[1]; OUT = sys.argv[2]
titles = json.load(open(f"{D}/titles.json"))
def inner(path):
    s=open(path).read()
    vb=re.search(r'viewBox="([^"]+)"',s).group(1)
    body=re.sub(r'^.*?<svg[^>]*>','',s,flags=re.S); body=re.sub(r'</svg>\s*$','',body)
    body=re.sub(r'<title>.*?</title>','',body)
    return vb, body
def place(path,x,y,w,h):
    vb,b=inner(path); return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vb}">{b}</svg>'
keys=list(titles)
ROW=230; W=1700; H=90+ROW*len(keys)
o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
   f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
   f'<rect x="{W//2}" y="0" width="{W//2}" height="{H}" fill="#16181D"/>',
   '<text x="24" y="40" font-family="Inter" font-size="26" font-weight="700" fill="#1A1A1A">MarCo — propuestas de logo (48×48, trazo 3, un color)</text>',
   f'<text x="{W//2+24}" y="40" font-family="Inter" font-size="26" font-weight="700" fill="#F5F5F2">Fondo oscuro (#16181D, tinte #9C9AF2)</text>',
   '<text x="24" y="66" font-family="Inter" font-size="15" fill="#555">Tamaños: 180 px · 48 px · 24 px · wordmark horizontal. Fondo claro #FFFFFF, color #5250CC.</text>']
for i,k in enumerate(keys):
    y=90+i*ROW
    lab=f"{i}. {titles[k]}" if i else f"0. {titles[k]} (referencia)"
    o.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#CCCCCC" stroke-width="1"/>')
    for side,(dx,suf,tc) in enumerate([(0,"","#1A1A1A"),(W//2,"_dark","#F5F5F2")]):
        o.append(f'<text x="{dx+24}" y="{y+28}" font-family="Inter" font-size="17" font-weight="600" fill="{tc}">{lab}</text>')
        f=f"{D}/marco_{k}{suf}.svg"
        o.append(place(f,dx+24,y+40,180,180))
        o.append(place(f,dx+230,y+106,48,48))
        o.append(place(f,dx+300,y+118,24,24))
        o.append(place(f"{D}/marco_{k}_wordmark{suf}.svg",dx+350,y+98,450,96))
o.append('</svg>')
open(OUT,"w").write("\n".join(o))
