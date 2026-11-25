"""Flagi Dacji i jej regionów (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_dacja/generuj_flagi.py"""
import os, subprocess, math
B='#0b5685'; R='#b20000'; Y='#facc00'; W='#ffffff'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
TRI=f'<rect width="300" height="67" fill="{B}"/><rect y="67" width="300" height="66" fill="{R}"/><rect y="133" width="300" height="67" fill="{Y}"/>'
def korona(cx,base,w,col):
    h=w*0.62
    pts=f'{cx-w/2},{base} {cx-w/2},{base-h*0.55} {cx-w/4},{base-h*0.25} {cx},{base-h} {cx+w/4},{base-h*0.25} {cx+w/2},{base-h*0.55} {cx+w/2},{base}'
    return f'<polygon points="{pts}" fill="{col}"/><rect x="{cx-w/2}" y="{base}" width="{w}" height="{h*0.22:.2f}" fill="{col}"/>'+''.join(f'<circle cx="{x}" cy="{y:.2f}" r="{w*0.06:.2f}" fill="{col}"/>' for x,y in ((cx-w/2,base-h*0.55),(cx,base-h),(cx+w/2,base-h*0.55)))
HERE=os.path.dirname(os.path.abspath(__file__))
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
F={
 # Republika Panońska (wzór od autora moda): błękit, czerwień, żółć
 'panonia_1_republika': svg(TRI),
 # Królestwo Panonii: ta sama trójbarwa, na środku czerwona tarcza w złotej obwódce ze złotą koroną
 'panonia_2_monarchia': svg(TRI+'<path d="M122,54 L178,54 L178,104 Q178,134 150,146 Q122,134 122,104Z" fill="#b20000" stroke="#facc00" stroke-width="3"/>'+korona(150,104,36,Y)),
 # Teokracja katolicka (biskupi Timișoary, pod opieką papieża): błękit ze złotym krzyżem łacińskim, u dołu cienkie pasy czerwień i żółć
 'panonia_3_teokracja': svg(f'<rect width="300" height="200" fill="{B}"/><rect y="164" width="300" height="18" fill="{R}"/><rect y="182" width="300" height="18" fill="{Y}"/>'
                            f'<rect x="141" y="22" width="18" height="128" fill="{Y}"/><rect x="112" y="52" width="76" height="18" fill="{Y}"/>'),
 # Panonia rewolucyjna: czerwień, u dołu cienkie pasy błękit i żółć, złota gwiazda w rogu
 'panonia_4_rewolucja': svg(f'<rect width="300" height="200" fill="{R}"/><rect y="164" width="300" height="18" fill="{B}"/><rect y="182" width="300" height="18" fill="{Y}"/>'+star(44,42,24,Y)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
