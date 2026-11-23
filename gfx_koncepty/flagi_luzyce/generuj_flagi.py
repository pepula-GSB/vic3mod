"""Flagi Łużyc (Serbołużyczanie, lenno Moraw, husyci). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_luzyce/generuj_flagi.py
Godła: mur Górnych Łużyc (rysowany wektorowo) i czerwony wół Dolnych Łużyc (od autora moda)."""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
WOL=b64('wol_luzycki.png'); WW,WH=768,801
KM=b64('kielich_maska_s.png'); KW,KH=300,581
BLUE='#0d5eaf'; RED='#c8102e'; WHITE='#fbfaf6'; GOLD='#f7e017'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def wol(cx,cy,h): w=h*WW/WH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{WOL}"/>'
def mur(x,y,w,h,rows=4,merlons=3,col=GOLD,line=BLACK,sw=1.2):
    """Złoty mur z blankami: prostokąt (x,y,w,h), blanki nad nim na wysokość cegły."""
    bh=h/rows; bw=w/4
    out=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" stroke="{line}" stroke-width="{sw}"/>']
    # blanki
    mw=w/(2*merlons-1)
    for i in range(merlons):
        mx=x+i*2*mw
        out.append(f'<rect x="{mx:.2f}" y="{y-bh:.2f}" width="{mw:.2f}" height="{bh:.2f}" fill="{col}" stroke="{line}" stroke-width="{sw}"/>')
    for r in range(1,rows):
        out.append(f'<line x1="{x}" y1="{y+r*bh:.2f}" x2="{x+w}" y2="{y+r*bh:.2f}" stroke="{line}" stroke-width="{sw}"/>')
    for r in range(rows):
        off=0 if r%2==0 else bw/2
        k=0
        while True:
            vx=x+off+k*bw
            if vx>=x+w-0.5: break
            if vx>x+0.5: out.append(f'<line x1="{vx:.2f}" y1="{y+r*bh:.2f}" x2="{vx:.2f}" y2="{y+(r+1)*bh:.2f}" stroke="{line}" stroke-width="{sw}"/>')
            k+=1
    return ''.join(out)
def chalice(cx,cy,h,col):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col,sw=0.6):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}" stroke="#000" stroke-width="{sw}" stroke-linejoin="round"/>'
def trojbarwa(): return f'<rect width="300" height="67" fill="{BLUE}"/><rect y="67" width="300" height="66" fill="{RED}"/><rect y="133" width="300" height="67" fill="{WHITE}"/>'
SH='M94,40 L206,40 L206,102 Q206,146 150,164 Q94,146 94,102Z'
def tarcza():
    # jedno pole: złoty mur Górnych Łużyc na błękicie, przed murem czerwony wół Dolnych Łużyc
    return (f'<defs><clipPath id="sh"><path d="{SH}"/></clipPath></defs>'
            f'<g clip-path="url(#sh)"><rect x="90" y="30" width="120" height="150" fill="{BLUE}"/>'
            f'{mur(90,110,120,60,rows=5,merlons=3,sw=1)}'
            f'{wol(150,84,66)}</g>'
            f'<path d="{SH}" fill="none" stroke="{BLACK}" stroke-width="2.4"/>')

F={
 # Margrabstwo (start, lenno Moraw): łużycka trójbarwa (błękit, czerwień, biel) z tarczą dzieloną: mur i wół
 '1_margrabstwo': svg(trojbarwa()+tarcza()),
 # Republika: sama trójbarwa łużycka (narodowa, bez dynastycznej tarczy)
 '2_republika': svg(trojbarwa()),
 # Teokracja husycka: biel z czerwonym wołem, czarny pas u dołu z białym kielichem (jak Pomorze i Morawy)
 '3_teokracja': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="160" width="300" height="40" fill="{BLACK}"/>'+wol(150,84,138)+chalice(150,180,30,WHITE)),
 # Łużyce rewolucyjne: czerwień, u dołu złoty mur z blankami (budujemy nowy świat), nad nim złota gwiazda
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/>'+mur(0,140,300,60,rows=4,merlons=5,sw=1.4)+star(150,62,34,GOLD)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
