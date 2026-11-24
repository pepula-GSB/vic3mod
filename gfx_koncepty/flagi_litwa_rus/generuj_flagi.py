"""Flagi Wielkiego Księstwa Litewsko-Ruskiego (prawosławne, Wilno i Kijów). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_litwa_rus/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
HERB=b64('herb_litwa_rus.png'); HW,HH=422,640
BLUE='#2274e0'; WHITE='#ffffff'; RED2='#c42424'; GREEN='#006a44'; RED='#c1272d'; GOLD='#fdb913'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def herb(cx,cy,h): w=h*HW/HH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{HERB}"/>'
def krzyz_podwojny(cx,top,h,col,stroke=BLACK,sw=1.2):
    """Krzyż podwójny (Jagiellonów, Pogoni): pion i dwie poprzeczki, dolna dłuższa."""
    t=h*0.16; w1=h*0.56; w2=h*0.74; y1=top+h*0.18; y2=top+h*0.43
    d=(f'M{cx-t/2:.2f},{top:.2f} H{cx+t/2:.2f} V{y1:.2f} H{cx+w1/2:.2f} V{y1+t:.2f} H{cx+t/2:.2f} V{y2:.2f} H{cx+w2/2:.2f} V{y2+t:.2f} H{cx+t/2:.2f} '
       f'V{top+h:.2f} H{cx-t/2:.2f} V{y2+t:.2f} H{cx-w2/2:.2f} V{y2:.2f} H{cx-t/2:.2f} V{y1+t:.2f} H{cx-w1/2:.2f} V{y1:.2f} H{cx-t/2:.2f}Z')
    return f'<path d="{d}" fill="{col}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="miter"/>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'

F={
 # Wielkie Księstwo / królestwo (start): zieleń-biel-czerwień, tarcza z trzema Pogoniami i koroną na środku
 '1_ksiestwo': svg(f'<rect width="300" height="50" fill="{GREEN}"/><rect y="50" width="300" height="100" fill="{WHITE}"/><rect y="150" width="300" height="50" fill="{RED2}"/>'+herb(150,100,96)),
 # Republika: zieleń, czerwony pas, biel, złoty krzyż podwójny (wzór od autora moda)
 '2_republika': svg(f'<rect width="300" height="90" fill="{GREEN}"/><rect y="90" width="300" height="25" fill="{RED}"/><rect y="115" width="300" height="85" fill="{WHITE}"/>'
                    +krzyz_podwojny(151,38,120,GOLD)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
