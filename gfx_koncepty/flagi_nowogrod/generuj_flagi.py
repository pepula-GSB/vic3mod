"""Flagi Republiki Nowogrodzkiej (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_nowogrod/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
TRON=b64('nowogrod_tron_niedzwiedzie.png'); TW,TH=824,832
RYBY=b64('nowogrod_ryby.png'); RYBYW=b64('nowogrod_ryby_biale.png'); RW,RH=704,164
GOLG=b64('krzyz_golgota_maska.png'); GW,GH=1245,1254
LAMP=b64('lampart_pskowski.png'); LPW,LPH=921,499
ZAM=b64('zamek_nowogrod_maska.png'); ZW,ZH=552,580
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
 # Monarchia (Księstwo Nowogrodzkie, gdy książę przejmie władzę od wiecu): złoto, ciemna czerwień i biel, tarcza ze złotym zamkiem (Detyniec) (wzór od autora moda)
 '1b_monarchia': svg('<rect width="300" height="66" fill="#f6c13a"/><rect y="66" width="300" height="67" fill="#8b0000"/><rect y="133" width="300" height="67" fill="#ffffff"/>'
                     +'<path d="M108,43 L192,43 L192,120 Q192,140 162,146 Q153,148 150,155 Q147,148 138,146 Q108,140 108,120Z" fill="#8b0000"/>'
                     +maska(ZAM,ZW,ZH,150,94,68,'#f6c13a','zam')),
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
 # Socjalistyczna Republika Nowego Nowogrodu: czerwień, żółty Wielki Wóz z Gwiazdą Polarną, żółty napis w ówczesnej pisowni (dopełniacz „Новаго”)
 'nowy_nowogrod_rewolucja': svg('<rect width="300" height="200" fill="#c8102e"/>'+star(95.4,47.1,4.2,'#ffd200')+star(115.0,54.4,4.2,'#ffd200')+star(124.8,64.8,4.2,'#ffd200')+star(134.7,75.7,4.2,'#ffd200')+star(133.4,91.2,4.2,'#ffd200')+star(155.5,98.4,4.2,'#ffd200')+star(164.0,86.2,4.2,'#ffd200')+star(204.6,23.0,7,'#ffd200')
                      +'<g font-family="DejaVu Sans" font-weight="bold" fill="#ffd200" text-anchor="middle">'
                       '<text x="150" y="156" font-size="12.4" letter-spacing="0.2">СОЦИАЛИСТИЧЕСКАЯ РЕСПУБЛИКА</text>'
                       '<text x="150" y="178" font-size="12.4" letter-spacing="1">НОВАГО НОВГОРОДА</text></g>'),
 # Republika Pskowska („młodszy brat” Nowogrodu): układ Nowogrodu, biel nad błękitem, lampart pskowski na zielonym wzgórzu
 'psków': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="{YB}" width="300" height="{200-YB}" fill="{BLUE}"/>'+img(LAMP,LPW,LPH,150,72,96)),
 # Wolna Republika Ochocka (Daleki Wschód): biel nad granatem Pacyfiku, złote słońce wschodzące nad horyzontem
 'ochock': svg(f'<rect width="300" height="200" fill="{WHITE}"/>'
               +''.join(f'<polygon points="150,{YB} {150+86*math.cos(math.radians(a-4)):.1f},{YB-86*math.sin(math.radians(a-4)):.1f} {150+86*math.cos(math.radians(a+4)):.1f},{YB-86*math.sin(math.radians(a+4)):.1f}" fill="{GOLD}"/>' for a in range(10,180,20))
               +f'<circle cx="150" cy="{YB}" r="30" fill="{GOLD}"/><rect y="{YB}" width="300" height="{200-YB}" fill="#0b3d6e"/>'),
 # Księstwo Syberyjskie (Stroganowowie, Tobolsk): biel nad zielenią (barwy regionalne Syberii), godło do dodania (sobole z herbu Syberii)
 'syberia': svg(f'<rect width="300" height="100" fill="{WHITE}"/><rect y="100" width="300" height="100" fill="#1b7a3e"/>'),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
