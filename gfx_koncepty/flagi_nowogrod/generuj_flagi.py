"""Flagi Republiki Nowogrodzkiej (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_nowogrod/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
TRON=b64('nowogrod_tron_niedzwiedzie.png'); TW,TH=824,832
RYBY=b64('nowogrod_ryby.png'); RYBYW=b64('nowogrod_ryby_biale.png'); RW,RH=704,164
GOLG=b64('krzyz_golgota_maska.png'); GW,GH=1245,1254
WHITE='#ffffff'; BLUE='#0087dd'; GOLD='#e8a317'; RED='#c8102e'; PURPLE='#4a1a5c'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def img(b,w0,h0,cx,cy,h): w=h*w0/h0; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def maska(b,w0,h0,cx,cy,h,col,mid):
    w=h*w0/h0
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
YB=133  # granica bieli i błękitu (2/3)
F={
 # Republika (start, wiece i Rada Panów): biel nad błękitem, tron z niedźwiedziami, ryby na błękicie (wzór od autora moda)
 '1_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{BLUE}"/>'
                    +img(TRON,TW,TH,150,72,112)+img(RYBY,RW,RH,150,166,32)),
 # Teokracja „Dom Świętej Zofii”: granat ze złotym krzyżem na Golgocie z włócznią i gąbką (wzór od autora moda)
 '2_teokracja': svg('<rect width="300" height="200" fill="#1a417a"/>'+maska(GOLG,GW,GH,150,99,163,'#dda733','golg')),
 # Nowogród rewolucyjny: czerwień nad błękitem, białe ryby (rybacy i flisacy), złota gwiazda
 '3_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{BLUE}"/>'
                    +star(150,66,40,GOLD)+img(RYBYW,RW,RH,150,166,32)),
 # Republika Nowego Nowogrodu (Sitka, po buncie Kompanii): układ w stylu flagi Republiki Kalifornijskiej.
 # Wielki Wóz i Gwiazda Polarna (jak na fladze Alaski) w granacie na bieli, napis w ówczesnej pisowni z jerem, granatowy pas u dołu.
 'nowy_nowogrod': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="167" width="300" height="33" fill="#2d2dcc"/>'
                      +star(95.4,55.1,4.2,'#2d2dcc')+star(115.0,62.4,4.2,'#2d2dcc')+star(124.8,72.8,4.2,'#2d2dcc')+star(134.7,83.7,4.2,'#2d2dcc')+star(133.4,99.2,4.2,'#2d2dcc')+star(155.5,106.4,4.2,'#2d2dcc')+star(164.0,94.2,4.2,'#2d2dcc')+star(204.6,31.0,7,'#2d2dcc')
                      +'<text x="150" y="152" font-family="DejaVu Sans" font-weight="bold" font-size="13.2" fill="#2d2dcc" text-anchor="middle" letter-spacing="0.2">РЕСПУБЛИКА НОВЫЙ НОВГОРОДЪ</text>'),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
