"""Flagi Dacji i jej regionów (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_dacja/generuj_flagi.py"""
import os, subprocess, math
B='#0b5685'; R='#b20000'; Y='#facc00'; W='#ffffff'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
TRI=f'<rect width="300" height="67" fill="{B}"/><rect y="67" width="300" height="66" fill="{R}"/><rect y="133" width="300" height="67" fill="{Y}"/>'
def krzyz_trojbelkowy(cx,top,h,col):
    """Krzyż trójbelkowy obrządku wschodniego (unici): tabliczka, belka główna, skośny podnóżek."""
    t=h*0.10; w1=h*0.30; w2=h*0.58; w3=h*0.36
    y1=top+h*0.12; y2=top+h*0.30; y3=top+h*0.74
    return (f'<rect x="{cx-t/2:.2f}" y="{top:.2f}" width="{t:.2f}" height="{h:.2f}" fill="{col}"/>'
            f'<rect x="{cx-w1/2:.2f}" y="{y1:.2f}" width="{w1:.2f}" height="{t:.2f}" fill="{col}"/>'
            f'<rect x="{cx-w2/2:.2f}" y="{y2:.2f}" width="{w2:.2f}" height="{t*1.1:.2f}" fill="{col}"/>'
            f'<g transform="rotate(-20 {cx:.2f} {y3+t/2:.2f})"><rect x="{cx-w3/2:.2f}" y="{y3:.2f}" width="{w3:.2f}" height="{t:.2f}" fill="{col}"/></g>')
def korona(cx,base,w,col):
    h=w*0.62
    pts=f'{cx-w/2},{base} {cx-w/2},{base-h*0.55} {cx-w/4},{base-h*0.25} {cx},{base-h} {cx+w/4},{base-h*0.25} {cx+w/2},{base-h*0.55} {cx+w/2},{base}'
    return f'<polygon points="{pts}" fill="{col}"/><rect x="{cx-w/2}" y="{base}" width="{w}" height="{h*0.22:.2f}" fill="{col}"/>'+''.join(f'<circle cx="{x}" cy="{y:.2f}" r="{w*0.06:.2f}" fill="{col}"/>' for x,y in ((cx-w/2,base-h*0.55),(cx,base-h),(cx+w/2,base-h*0.55)))
HERE=os.path.dirname(os.path.abspath(__file__))
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
F={
 # Republika Panońska (wzór od autora moda): błękit, czerwień, żółć
 'panonia_1_republika': svg(TRI),
 # Królestwo Panonii: ta sama trójbarwa co republika, bez korony
 'panonia_2_monarchia': svg(TRI),
 # Teokracja unicka (biskupi Timișoary w unii z Rzymem, obrządek wschodni): trójbarwa jak republika, na środku biały krzyż trójbelkowy
 'panonia_3_teokracja': svg(TRI+krzyz_trojbelkowy(150,71,58,W)),
 # Panonia rewolucyjna A: trójbarwa jak republika, mała żółta gwiazda na czerwonym pasie
 'panonia_4a_rewolucja': svg(TRI+star(150,101.5,29,Y)),
 # Panonia rewolucyjna B: trójbarwa jak republika, czerwona gwiazda na błękicie przy drzewcu
 'panonia_4b_rewolucja': svg(TRI+star(36,34.5,23,R)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
