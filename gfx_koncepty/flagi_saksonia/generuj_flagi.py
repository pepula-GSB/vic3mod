"""Flagi Królestwa Saskiego (Welfowie, protestanci, front nad Łabą). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_saksonia/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
KON=b64('kon_saski.png'); KW,KH=598,661
RED='#c8102e'; WHITE='#faf8f2'; GOLD='#f2c230'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def kon(cx,cy,h,flip=False):
    w=h*KW/KH; t=f' transform="translate({2*cx},0) scale(-1,1)"' if flip else ''
    return f'<g{t}><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KON}"/></g>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
SH='M100,38 L200,38 L200,98 Q200,140 150,158 Q100,140 100,98Z'

F={
 # Królestwo (start, Welfowie): czerwień ze złotymi pasami u góry i dołu, biały koń saski
 '1_krolestwo': svg(f'<rect width="300" height="200" fill="{RED}"/><rect width="300" height="18" fill="{GOLD}"/><rect y="182" width="300" height="18" fill="{GOLD}"/>'+kon(150,100,140)),
 # Republika: biel-czerwień-biel poziomo, koń saski na czerwonym pasie
 '2_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="50" width="300" height="100" fill="{RED}"/>'+kon(150,100,92)),
 # Saksonia na czele zjednoczonych Niemiec: czerń-czerwień-złoto, tarcza z koniem saskim
 '3_zjednoczenie': svg(f'<rect width="300" height="67" fill="{BLACK}"/><rect y="67" width="300" height="66" fill="#dd0000"/><rect y="133" width="300" height="67" fill="#ffce00"/>'
                      f'<path d="{SH}" fill="#dd0000" stroke="{BLACK}" stroke-width="2.4"/>'+kon(150,94,82)),
 # Saksonia rewolucyjna: czerwień, w lewym górnym rogu biała gwiazda, koń skacze ku niej (odbity)
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/>'+kon(170,108,140)+star(46,42,24,WHITE)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
