"""Flagi Marchii Miśnieńskiej (lenno Moraw, husyci). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_misnia/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
LEW=b64('lew_misnienski.png'); LEWZ=b64('lew_misnienski_zloty.png'); LW,LH=547,652
KM=b64('kielich_maska_s.png'); KW,KH=300,581
GOLD='#fdd800'; BLACK='#0b0b0b'; RED='#c8102e'; WHITE='#fbfaf6'; STAR='#f2c230'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def lew(b,cx,cy,h): w=h*LW/LH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def chalice(cx,cy,h,col):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col,sw=0.6):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}" stroke="#000" stroke-width="{sw}" stroke-linejoin="round"/>'

F={
 # Marchia (start, lenno Moraw): złote pole z czarnym lwem, czarne pasy u góry i dołu
 '1_marchia': svg(f'<rect width="300" height="200" fill="{GOLD}"/><rect width="300" height="18" fill="{BLACK}"/><rect y="182" width="300" height="18" fill="{BLACK}"/>'+lew(LEW,150,100,150)),
 # Republika: czerń i złoto dzielone pionowo, bez lwa
 '2_republika': svg(f'<rect width="150" height="200" fill="{BLACK}"/><rect x="150" width="150" height="200" fill="{GOLD}"/>'),
 # Teokracja husycka: złoto z czarnym lwem, czarny pas u dołu z białym kielichem
 '3_teokracja': svg(f'<rect width="300" height="200" fill="{GOLD}"/><rect y="160" width="300" height="40" fill="{BLACK}"/>'+lew(LEW,150,82,138)+chalice(150,180,30,WHITE)),
 # Miśnia rewolucyjna: czerwień, złoty lew, czarny pas u dołu, złota gwiazda w lewym górnym rogu
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="176" width="300" height="24" fill="{BLACK}"/>'+lew(LEWZ,156,92,150)+star(34,32,18,STAR)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
