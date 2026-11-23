"""Flagi Księstwa Pruskiego (koncepty). Uruchom z katalogu repo: python3 gfx_koncepty/flagi_prusy/generuj_flagi.py
Wzór bazowy: flaga od autora moda (czerń, czerwień z białymi lamówkami, biała tarcza z postacią Prusa)."""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
PRUS=b64('prus_s.png'); PW,PH=400,537
PRY=b64('prus_zolty_s.png')
PRB=b64('prus_bialy_s.png'); PBW,PBH=300,413
BLACK='#000000'; WHITE='#ffffff'; RED='#d40000'; GOLD='#e2b53a'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def prus(cx,cy,h): w=h*PW/PH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{PRUS}"/>'
def bands(mid=RED): return (f'<rect width="300" height="200" fill="{BLACK}"/><rect y="63" width="300" height="74" fill="{WHITE}"/>'
                          f'<rect y="70" width="300" height="60" fill="{mid}"/>')
SHIELD='M110,48 L190,48 L189,100 Q186,138 150,152 Q114,138 111,100Z'
def shield(fill=WHITE,stroke=BLACK): return f'<path d="{SHIELD}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def star(cx,cy,r,col,stroke=None,sw=0):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    s=f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ''
    return f'<polygon points="{" ".join(p)}" fill="{col}"{s}/>'
def cross(cx,cy,h,col):
    w=h*.62; t=h*.16
    return f'<rect x="{cx-t/2:.1f}" y="{cy-h/2:.1f}" width="{t:.1f}" height="{h:.1f}" fill="{col}"/><rect x="{cx-w/2:.1f}" y="{cy-h/2+h*.22:.1f}" width="{w:.1f}" height="{t:.1f}" fill="{col}"/>'

F={
 # Księstwo (start): wzór od autora moda
 '1_ksiestwo': svg(bands()+shield()+prus(150,96,84)),
 # Republika: same pasy, na czerwonym pasie biały, konturowy Prus (bez tarczy)
 '2_republika': svg(bands()+(lambda h:f'<image x="{150-h*PBW/PBH/2:.1f}" y="{100-h/2:.1f}" width="{h*PBW/PBH:.1f}" height="{h:.1f}" href="data:image/png;base64,{PRB}"/>')(54)),
 # Republika, wariant bez godła
 '2b_republika_bez_godla': svg(bands()),
 # Teokracja katolicka (biskupi warmińscy z Fromborka): środkowy pas złoty, nad tarczą złoty krzyż
 '3_teokracja': svg(bands(GOLD)+shield()+prus(150,100,80)+cross(150,30,30,GOLD)),
 # Prusy rewolucyjne: sama czerwień, żółty konturowy Prus
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/>'+(lambda h:f'<image x="{150-h*PBW/PBH/2:.1f}" y="{100-h/2:.1f}" width="{h*PBW/PBH:.1f}" height="{h:.1f}" href="data:image/png;base64,{PRY}"/>')(130)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
