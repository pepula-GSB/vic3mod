"""Flagi Księstwa Czeskiego (Przemyślidzi, lenno Moraw, husyci). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_czechy/generuj_flagi.py
Motyw przewodni: szachownica pól z lwem czeskim i orłem św. Wacława."""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
LEW=b64('lew_czeski.png'); LW,LH=287,376
ORZ=b64('orzel_swietowaclawski.png'); OW,OH=569,675
KM=b64('kielich_maska_s.png'); KW,KH=300,581
RED='#ce0000'; WHITE='#fbfaf6'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def img(b,w0,h0,cx,cy,h,flip=False):
    w=h*w0/h0; t=f' transform="translate({2*cx},0) scale(-1,1)"' if flip else ''
    return f'<g{t}><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/></g>'
def lew(cx,cy,h,flip=False): return img(LEW,LW,LH,cx,cy,h,flip)
def orzel(cx,cy,h): return img(ORZ,OW,OH,cx,cy,h)
def chalice(cx,cy,h,col):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
def kwadraty(): return (f'<rect width="150" height="100" fill="{RED}"/><rect x="150" width="150" height="100" fill="{WHITE}"/>'
                        f'<rect y="100" width="150" height="100" fill="{WHITE}"/><rect x="150" y="100" width="150" height="100" fill="{RED}"/>')

F={
 # Księstwo (start, Przemyślidzi praskiej linii): szachownica czterech pól, lew czeski na czerwieni, orzeł św. Wacława na bieli
 '1_ksiestwo': svg(kwadraty()+lew(75,50,84)+orzel(225,50,86)+orzel(75,150,86)+lew(225,150,84)),
 # Republika: ta sama szachownica pól, ale bez godeł dynastycznych: tylko lwy (orzeł św. Wacława to znak książąt)
 '2_republika': svg(kwadraty()+lew(75,50,84)+lew(225,150,84)),
 # Teokracja husycka (Praga, kolebka Husa): szachownica z lwami na czerwieni, a zamiast orła biały kielich na czerni
 '3_teokracja': svg(kwadraty()+lew(75,50,84)+lew(225,150,84)+f'<rect x="150" width="150" height="100" fill="{BLACK}"/><rect y="100" width="150" height="100" fill="{BLACK}"/>'
                    +chalice(225,50,44,WHITE)+chalice(75,150,44,WHITE)),
 # Czechy rewolucyjne: pięć poziomych pasów czerwono-białych, złota gwiazda na środku
 '4_rewolucja': svg(''.join(f'<rect y="{i*40}" width="300" height="40" fill="{RED if i%2==0 else WHITE}"/>' for i in range(5))+star(150,100,46,'#f2c230').replace('/>',' stroke="#8a0000" stroke-width="2.2" stroke-linejoin="round"/>')),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
