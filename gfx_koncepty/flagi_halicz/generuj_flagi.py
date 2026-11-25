"""Flagi Królestwa Halicko-Wołyńskiego (unickie, Lwów, Halicz, Łuck, Mołdawia). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_halicz/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
LEW=b64('lew_halicki.png'); LEWN=b64('lew_halicki_niebieski.png'); LW,LH=395,514
BLUE='#1264be'; GOLD='#fed503'; WHITE='#ffffff'; RED='#c8102e'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def lew(b,cx,cy,h): w=h*LW/LH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
F={
 # Królestwo (start): złoty lew halicki na błękicie, złote pasy u góry i dołu
 '1_krolestwo': svg(f'<rect width="300" height="200" fill="{BLUE}"/><rect width="300" height="14" fill="{GOLD}"/><rect y="186" width="300" height="14" fill="{GOLD}"/>'+lew(LEW,150,100,150)),
 # Republika: błękit nad złotem, lew w kantonie (barwy halickie)
 '2_republika': svg(f'<rect width="300" height="100" fill="{BLUE}"/><rect y="100" width="300" height="100" fill="{GOLD}"/>'+lew(LEW,52,50,82)),
 # Teokracja unicka (metropolita lwowski w unii z Rzymem): barwy papieskie, złoto i biel pionowo, błękitny lew na środku
 '3_teokracja': svg(f'<rect width="150" height="200" fill="{GOLD}"/><rect x="150" width="150" height="200" fill="{WHITE}"/>'+lew(LEWN,150,100,150)),
 # Rewolucja: czerwień, złoty lew i złota gwiazda w rogu, błękitny pas u dołu
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="170" width="300" height="30" fill="{BLUE}"/>'+star(48,28,16,GOLD)+lew(LEW,48,98,94)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
