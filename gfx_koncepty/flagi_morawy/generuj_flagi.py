"""Flagi Królestwa Morawskiego (Mojmirowice, serce kościoła husyckiego). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_morawy/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
ORZ=b64('orzel_morawski.png'); OW,OH=537,582
KM=b64('kielich_maska_s.png'); KW,KH=300,581
BLUE='#252b93'; WHITE='#fbfaf6'; RED='#d0021b'; YEL='#f6c40e'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def orzel(cx,cy,h): w=h*OW/OH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{ORZ}"/>'
def chalice(cx,cy,h,col):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
def szachownica(x,y,w,h,n_cols,c1,c2):
    s=w/n_cols; n_rows=int(round(h/s)); out=[]
    for r in range(n_rows):
        for c in range(n_cols):
            out.append(f'<rect x="{x+c*s:.2f}" y="{y+r*s:.2f}" width="{s+.05:.2f}" height="{s+.05:.2f}" fill="{c1 if (r+c)%2==0 else c2}"/>')
    return ''.join(out)

F={
 # Królestwo (start, Mojmirowice): wzór od autora moda, szachowany orzeł na błękicie
 '1_krolestwo': svg(f'<rect width="300" height="200" fill="{BLUE}"/>'+orzel(150,100,176)),
 # Republika: żółto-czerwone barwy morawskie, błękitny panel przy drzewcu z orłem
 '2_republika': svg(f'<rect width="300" height="100" fill="{YEL}"/><rect y="100" width="300" height="100" fill="{RED}"/><rect width="110" height="200" fill="{BLUE}"/>'+orzel(55,100,104)),
 # Teokracja husycka (stolica kościoła morawskiego): jak królestwo, czarny pas u dołu z małym białym kielichem
 '3_teokracja': svg(f'<rect width="300" height="200" fill="{BLUE}"/><rect y="160" width="300" height="40" fill="{BLACK}"/>'+orzel(150,82,146)+chalice(150,180,30,WHITE)),
 # Morawy rewolucyjne: czerwień, przy drzewcu pionowy pas szachownicy (z orła), złota gwiazda
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/>'+szachownica(0,0,50,200,2,WHITE,RED)+f'<rect x="50" width="3" height="200" fill="{WHITE}"/>'+star(176,100,50,YEL)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
