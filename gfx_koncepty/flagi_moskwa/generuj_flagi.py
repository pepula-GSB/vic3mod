"""Flagi Wielkiego Księstwa Moskiewskiego (pozostałość Ordy: prawosławny zachód, zislamizowany wschód). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_moskwa/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
JERZY=b64('jerzy_moskiewski.png'); JW,JH=622,732
PKO=b64('polksiezyc_ozdobny_maska.png'); PKW,PKH=492,510
CRIM='#a8002c'; WHITE='#ffffff'; GOLD='#f2c230'; GREEN='#00703c'; NAVY='#0e3a73'; RED='#c8102e'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def jerzy(cx,cy,h): w=h*JW/JH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{JERZY}"/>'
def star(cx,cy,r,col,rot=0):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+rot+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+rot+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
_n=[0]
def polksiezyc(cx,cy,r,col,bg,dx=0.32):
    """Półksiężyc otwarty w prawo: koło minus przesunięte koło (maską)."""
    _n[0]+=1; mid=f"pk{_n[0]}"
    return (f'<defs><mask id="{mid}"><rect width="300" height="200" fill="white"/><circle cx="{cx+r*dx:.2f}" cy="{cy:.2f}" r="{r*0.82:.2f}" fill="black"/></mask></defs>'
            f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{col}" mask="url(#{mid})"/>')
def maska(b,w0,h0,cx,cy,h,col,mid):
    w=h*w0/h0
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def krzyz_prawoslawny(cx,top,h,col):
    """Krzyż ośmioramienny: tabliczka, belka główna i skośny podnóżek."""
    t=h*0.09; w1=h*0.30; w2=h*0.58; w3=h*0.36
    y1=top+h*0.12; y2=top+h*0.30; y3=top+h*0.74
    return (f'<rect x="{cx-t/2:.2f}" y="{top:.2f}" width="{t:.2f}" height="{h:.2f}" fill="{col}"/>'
            f'<rect x="{cx-w1/2:.2f}" y="{y1:.2f}" width="{w1:.2f}" height="{t:.2f}" fill="{col}"/>'
            f'<rect x="{cx-w2/2:.2f}" y="{y2:.2f}" width="{w2:.2f}" height="{t*1.1:.2f}" fill="{col}"/>'
            f'<g transform="rotate(-20 {cx:.2f} {y3+t/2:.2f})"><rect x="{cx-w3/2:.2f}" y="{y3:.2f}" width="{w3:.2f}" height="{t:.2f}" fill="{col}"/></g>')

F={
 # Wielkie Księstwo (start): karmazyn z Jerzym zabijającym smoka (wzór od autora moda)
 '1_ksiestwo': svg(f'<rect width="300" height="200" fill="{CRIM}"/>'+jerzy(150,99,171)),
 # Republika świecka: czerń, zieleń i biel (wzór od autora moda bez półksiężyca)
 '2_republika': svg('<rect width="300" height="67" fill="#000000"/><rect y="67" width="300" height="66" fill="#0e7644"/><rect y="133" width="300" height="67" fill="#ffffff"/>'),
 # Republika islamska (gdy islam weźmie górę): ta sama trójbarwa ze złotym, zdobionym półksiężycem i gwiazdą (wzór od autora moda)
 '2b_republika_islamska': svg('<rect width="300" height="67" fill="#000000"/><rect y="67" width="300" height="66" fill="#0e7644"/><rect y="133" width="300" height="67" fill="#ffffff"/>'+maska(PKO,PKW,PKH,148,99.5,47,'#fac01e','pko')),
 # Republika dwóch wiar (wariant): karmazyn, na środku białe koło, w nim złoty krzyż i złoty półksiężyc obok siebie (dwie wiary jako równe)
 '2c_republika_dwoch_wiar': svg(f'<rect width="300" height="200" fill="{CRIM}"/><circle cx="150" cy="100" r="58" fill="{WHITE}"/>'
                    +krzyz_prawoslawny(127,68,64,GOLD)+polksiezyc(176,100,24,GOLD,WHITE)),
 # Teokracja prawosławna (metropolita moskiewski): granat z płaszcza Jerzego, złoty krzyż ośmioramienny
 '3a_teokracja_prawoslawna': svg(f'<rect width="300" height="200" fill="{NAVY}"/>'+krzyz_prawoslawny(150,30,140,GOLD)),
 # Teokracja islamska (rządy ulemów z Kazania, chanat): zieleń, biały półksiężyc i gwiazda
 '3b_teokracja_islamska': svg(f'<rect width="300" height="200" fill="{GREEN}"/>'+polksiezyc(140,100,48,WHITE,GREEN)+star(168,100,16,WHITE,rot=18)),
 # Rewolucja: czerwień, złoty półksiężyc z gwiazdą w rogu (półksiężyc jak sierp, wspólny znak Rusinów i Tatarów)
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/>'+polksiezyc(48,48,30,GOLD,RED)+star(64,48,11,GOLD,rot=18)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
