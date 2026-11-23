"""Flagi Śląska (koncepty) dla wyników łańcucha „Bezkrólewie śląskie”.
Uruchom z katalogu repo: python3 gfx_koncepty/flagi_slask/generuj_flagi.py"""
import base64, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
BLK=b64('orzel_slaski_s.png');  BW,BH=500,548     # czarny orzeł dolnośląski z przepaską
DIM=b64('orzel_slaski_polaczony_s.png'); DW,DH=500,581   # orzeł dzielony: dolny (czarny) i górny (złoty) Śląsk
GOLD='#fcd116'; BLUE='#3044b5'; WHITE='#fbfaf6'; RED='#b3262b'; YEL='#f2c230'; BLACK='#1b1a1a'

KM=b64('kielich_maska_s.png'); KW,KH=300,581
MG=b64('mloty_gornicze_s.png'); MGW,MGH=400,384
HAM=b64('mlot_s.png'); HW,HH=240,623
import math
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{' '.join(p)}" fill="{col}"/>'
def chalice(cx,cy,h,parts):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    m=f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
    return m+f'<g mask="url(#{mid})">'+''.join(f'<polygon points="{pts}" fill="{c}"/>' for pts,c in parts)+'</g>'
def img(b,w0,h0,cx,cy,h):
    w=h*w0/h0; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'

F={
 # Księstwo (start, Przemyślidzi wrocławscy, cały Śląsk): złoto i błękit dzielone pionowo, orzeł dzielony
 '1_ksiestwo': svg(f'<rect width="150" height="200" fill="{GOLD}"/><rect x="150" width="150" height="200" fill="{BLUE}"/>'+img(DIM,DW,DH,150,102,176)),
 # Republika Śląska (Wrocław, miasta odrzańskie): złoto-biel-błękit poziomo, orzeł dzielony na białym pasie, bez dynastycznych ozdób
 '2_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="300" height="56" fill="{GOLD}"/><rect y="144" width="300" height="56" fill="{BLUE}"/>'+img(DIM,DW,DH,150,100,150)),
 # Unia z Czechami (linia praska): biało-czerwona (barwy czeskie), czarny orzeł śląski w złotym polu przy drzewcu
 '3_unia_czeska': svg(f'<rect width="300" height="100" fill="{WHITE}"/><rect y="100" width="300" height="100" fill="{RED}"/><rect width="110" height="200" fill="{GOLD}"/>'+img(BLK,BW,BH,55,100,108)),
 # Prowincja morawska (wcielenie do Moraw): żółto-czerwone barwy morawskie, orzeł śląski na złotej tarczy w czarnej obwódce
 '4_prowincja_morawska': svg(f'<rect width="300" height="100" fill="{YEL}"/><rect y="100" width="300" height="100" fill="{RED}"/>'
                             f'<path d="M100,30 L200,30 L200,96 Q200,146 150,168 Q100,146 100,96Z" fill="{GOLD}" stroke="{BLACK}" stroke-width="3"/>'+img(BLK,BW,BH,150,96,104)),
 # Śląsk pod polskim kandydatem (po kądzieli): układ polski, białe pasy po bokach, złoto z czarnym orłem w środku
 '5_polski_kandydat': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect x="62" width="176" height="200" fill="{GOLD}"/>'
                          f'<rect x="62" y="186" width="176" height="14" fill="{RED}"/>'+img(BLK,BW,BH,150,96,168)),
 # Śląsk rewolucyjny (górnicy i hutnicy Górnego Śląska): górnicza zieleń nad czernią, żółte skrzyżowane młotki, nad nimi czerwona gwiazda
 '6_rewolucja': svg(f'<rect width="300" height="100" fill="#1e6a3c"/><rect y="100" width="300" height="100" fill="#000000"/>'
                    +img(MG,MGW,MGH,155,100,96)+star(150,34,15,'#d81e1e')),
 # Teokracja husycka (Śląsk jest husyckim lennem Moraw): złoto nad czernią, kielich w kontrbarwach
 '7_teokracja': svg(f'<rect width="300" height="100" fill="{GOLD}"/><rect y="100" width="300" height="100" fill="{BLACK}"/>'
                    +chalice(150,100,160,[('0,0 300,0 300,100 0,100',BLACK),('0,100 300,100 300,200 0,200',GOLD)])),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
