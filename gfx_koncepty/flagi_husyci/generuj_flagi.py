"""Flagi husyckie z kielichem (koncepty). Uruchom z katalogu repo: python3 gfx_koncepty/flagi_husyci/generuj_flagi.py
Kielich to maska PNG (../emblematy/kielich_maska.png) barwiona przez filtr SVG,
więc jedna grafika daje kielich w dowolnym kolorze i w kontrbarwach (pół na pół)."""
import base64, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
MASK=base64.b64encode(open(os.path.join(HERE,'..','emblematy','kielich_maska_s.png'),'rb').read()).decode()
MW,MH=300,581
PLE=base64.b64encode(open(os.path.join(HERE,'..','emblematy','orzel_polski_kielich_s.png'),'rb').read()).decode()
PLW,PLH=566,691
PLR=base64.b64encode(open(os.path.join(HERE,'..','emblematy','orzel_polski_bez_korony_kielich_s.png'),'rb').read()).decode()
KGO=base64.b64encode(open(os.path.join(HERE,'..','emblematy','kielich_zloty_kontur.png'),'rb').read()).decode()
HAM=base64.b64encode(open(os.path.join(HERE,'..','emblematy','mlot_s.png'),'rb').read()).decode()
MZE=base64.b64encode(open(os.path.join(HERE,'..','emblematy','orzel_mazowiecki_s.png'),'rb').read()).decode()
def eagle(b64,cx,cy,h): w=h*PLW/PLH; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b64}"/>'
WHITE='#fbfaf6'; RED='#b3262b'; BLACK='#1b1a1a'; GOLD='#e2b53a'; BLUE='#1f4e8c'; YEL='#f2c230'

def defs():
    return (f'<defs><mask id="k" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200">'
            f'<image id="kimg" x="0" y="0" width="0" height="0" href="data:image/png;base64,{MASK}"/></mask></defs>')

def chalice(cx,cy,h,col,parts=None):
    """Kielich wysokości h w kolorze col; parts=[(wielokąt_punkty, kolor), ...] daje kontrbarwy dowolnie podzielone."""
    w=h*MW/MH; x=cx-w/2; y=cy-h/2; mid=f"km{cx}_{cy}_{h}".replace('.','_')
    img=f'<image x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{MASK}"/>'
    m=f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200">{img}</mask></defs>'
    if not parts:
        return m+f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>'
    return m+f'<g mask="url(#{mid})">'+''.join(f'<polygon points="{pts}" fill="{c}"/>' for pts,c in parts)+'</g>'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def bands(top,bot): return f'<rect width="300" height="100" fill="{top}"/><rect y="100" width="300" height="100" fill="{bot}"/>'

TOP='0,0 300,0 300,100 0,100'; BOT='0,100 300,100 300,200 0,200'
UPL='0,0 300,0 0,200'; LOR='300,0 300,200 0,200'   # podział w skos (od dolnego drzewca do górnego rogu swobodnego)
F={
 # chorągiew wojen husyckich: czerwony kielich na czerni; blok husycki albo rząd radykalny (taboryci)
 '1_liga_husycka': svg(f'<rect width="300" height="200" fill="{BLACK}"/>'+chalice(150,100,150,RED)),
 # Polska (Poznań): białe pionowe pasy po bokach, czerwień z orłem w koronie i czarno obrysowanym kielichem na piersi
 '2_polska': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect x="62" width="176" height="200" fill="{RED}"/>'+eagle(PLE,150,100,170)),
 # Polska, republika: ten sam układ, orzeł bez korony (zdjęta korona = koniec monarchii)
 '2a_polska_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect x="62" width="176" height="200" fill="{RED}"/>'+eagle(PLR,150,100,170)),
 # Polska, teokracja husycka (rządy duchowieństwa): czarne pasy jak chorągiew husycka, duży złoty kielich
 '2c_polska_teokracja': svg(f'<rect width="300" height="200" fill="{BLACK}"/><rect x="62" width="176" height="200" fill="{RED}"/>'
                            +(lambda h:f'<image x="{150-h*222/416/2:.1f}" y="{100-h/2:.1f}" width="{h*222/416:.1f}" height="{h:.1f}" href="data:image/png;base64,{KGO}"/>')(150)),
 # Polska, rewolucyjna/radykalna (taboryci, komuna): czerwień, mały orzeł bez korony w kantonie, pod nim młot
 '2d_polska_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect width="300" height="200" fill="none" stroke="{WHITE}" stroke-width="0"/>'
                            f'<rect y="150" width="300" height="14" fill="{WHITE}"/>'+eagle(PLR,46,54,86)+(lambda L:f'<g transform="translate(46,103) rotate(-90)"><image x="{-L*240/623/2:.1f}" y="{-L/2:.1f}" width="{L*240/623:.1f}" height="{L:.1f}" href="data:image/png;base64,{HAM}"/></g>')(52)),
 # Polska, wersja cywilna: biało-czerwona z małym kielichem przy drzewcu
 '2b_polska_cywilna': svg(bands(WHITE,RED)+chalice(52,50,74,RED)),
 # Morawy, kolebka ruchu: czerwień w złotej obwódce, duży złoty kielich
 '3_morawy': svg(f'<rect width="300" height="200" fill="{GOLD}"/><rect x="10" y="10" width="280" height="180" fill="{RED}"/>'
                 f'<rect x="16" y="16" width="268" height="168" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'+chalice(150,100,140,GOLD)),
 # Pomorze (Gryfici, Hanza): niebieski pas przy drzewcu, biel, niebieski kielich na bieli
 '4_pomorze': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="100" height="200" fill="{BLUE}"/>'+chalice(200,100,140,BLUE)),
 # Czechy: biel i czerwień dzielone w skos, kielich w kontrbarwach
 '5_czechy': svg(f'<polygon points="{UPL}" fill="{WHITE}"/><polygon points="{LOR}" fill="{RED}"/>'+chalice(150,100,150,None,[(UPL,RED),(LOR,WHITE)])),
 # Mazowsze (katolickie, dla porównania): czerwień z białym pasem przez środek, orzeł bez korony na czerwonej tarczy w złotej obwódce
 '6_mazowsze': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="76" width="300" height="48" fill="{WHITE}"/>'
                   f'<path d="M94,36 L206,36 L206,98 Q206,146 150,166 Q94,146 94,98Z" fill="{RED}" stroke="{GOLD}" stroke-width="3.5"/>'+eagle(MZE,150,98,112)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
