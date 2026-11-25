"""Flagi Republiki Nowogrodzkiej (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_nowogrod/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
TRON=b64('nowogrod_tron_niedzwiedzie.png'); TW,TH=824,832
RYBY=b64('nowogrod_ryby.png'); RYBYW=b64('nowogrod_ryby_biale.png'); RW,RH=704,164
WHITE='#ffffff'; BLUE='#0087dd'; GOLD='#e8a317'; RED='#c8102e'; PURPLE='#4a1a5c'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def img(b,w0,h0,cx,cy,h): w=h*w0/h0; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
YB=133  # granica bieli i błękitu (2/3)
F={
 # Republika (start, wiece i Rada Panów): biel nad błękitem, tron z niedźwiedziami, ryby na błękicie (wzór od autora moda)
 '1_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{BLUE}"/>'
                    +img(TRON,TW,TH,150,72,112)+img(RYBY,RW,RH,150,166,32)),
 # Teokracja (rządy arcybiskupa nowogrodzkiego, który realnie przewodził Radzie Panów): purpura zamiast błękitu, tron bez ryb
 '2_teokracja': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{PURPLE}"/>'
                    +img(TRON,TW,TH,150,72,112)+f'<rect y="{YB+6}" width="300" height="3" fill="{GOLD}"/>'),
 # Nowogród rewolucyjny: czerwień nad błękitem, białe ryby (rybacy i flisacy), złota gwiazda
 '3_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{BLUE}"/>'
                    +star(150,66,40,GOLD)+img(RYBYW,RW,RH,150,166,32)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
