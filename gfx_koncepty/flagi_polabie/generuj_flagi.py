"""Flagi państw połabskich (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_polabie/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
TRY=b64('tryglaw_herb_s.png'); TW,TH=400,438
TRYR=b64('tryglaw_czerwony_s.png')
TG='#ecb22e'; TR='#c8101c'  # złoto i czerwień z herbu Trygława
KOL=b64('kolowrot_maska_s.png')
GO=b64('gryf_obodrzycki.png'); GOW,GOH=332,410
BLUE='#1d6091'; GOLD='#f2b84b'; WHITE='#fbfaf6'; RED='#c8102e'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def img(b,w0,h0,cx,cy,h): w=h*w0/h0; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
def kolowrot(cx,cy,d,col):
    mid=f"kol{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-d/2:.1f}" y="{cy-d/2:.1f}" width="{d:.1f}" height="{d:.1f}" href="data:image/png;base64,{KOL}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'

F={
 # Obodryci, księstwo (start, Niklotowice): złoty gryf na błękicie, złoty pas u dołu
 'obodryci_1_ksiestwo': svg(f'<rect width="300" height="200" fill="{BLUE}"/><rect y="172" width="300" height="28" fill="{GOLD}"/>'+img(GO,GOW,GOH,150,88,152)),
 # Obodryci, republika kupiecka (Liubice, słowiańska Hanza): biel nad czerwienią jak barwy Hanzy, na środku błękitne koło ze złotym gryfem
 'obodryci_2_republika': svg(f'<rect width="300" height="100" fill="{WHITE}"/><rect y="100" width="300" height="100" fill="{RED}"/>'
                            f'<circle cx="150" cy="100" r="62" fill="{BLUE}" stroke="{GOLD}" stroke-width="4"/>'+img(GO,GOW,GOH,147.5,105,98)),
 # Obodryci rewolucyjni: czerwień, złoty gryf trzyma się gwiazdy (gwiazda przed szponami)
 'obodryci_3_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="172" width="300" height="28" fill="{BLUE}"/>'+img(GO,GOW,GOH,154,90,150)+star(34,32,18,GOLD).replace('/>',' stroke="#000000" stroke-width="0.6" stroke-linejoin="round"/>')),
 # Wieletia, rządy kapłanów Radogoszczy i Arkony (start): biel z czerwonymi pasami u góry i dołu, czerwony kołowrót
 'wieletia_1_kaplani': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="300" height="26" fill="{RED}"/><rect y="174" width="300" height="26" fill="{RED}"/>'+kolowrot(150,100,112,RED)),
 # Wieletia, księstwo świeckie: czerwień, złoty kołowrót
 'wieletia_2_ksiestwo': svg(f'<rect width="300" height="200" fill="{RED}"/>'+kolowrot(150,100,140,GOLD)),
 # Wieletia, republika: biel i czerwień dzielone pionowo, kołowrót w kontrbarwach
 'wieletia_3_republika': svg(f'<rect width="150" height="200" fill="{WHITE}"/><rect x="150" width="150" height="200" fill="{RED}"/>'
                            +'<defs><clipPath id="lw"><rect width="150" height="200"/></clipPath><clipPath id="pw"><rect x="150" width="150" height="200"/></clipPath></defs>'
                            +f'<g clip-path="url(#lw)">{kolowrot(150,100,130,RED)}</g><g clip-path="url(#pw)">{kolowrot(150,100,130,WHITE).replace("kol150100","kol150100b")}</g>'),
 # Wieletia rewolucyjna: czerwień, biały pas u dołu, złota gwiazda w rogu (bez symbolu religijnego)
 'wieletia_4_rewolucja': svg(f'<rect width="300" height="200" fill="{RED}"/><rect y="160" width="300" height="16" fill="{WHITE}"/>'+star(46,46,26,GOLD).replace('/>',' stroke="#000000" stroke-width="0.6" stroke-linejoin="round"/>')),
 # Stodorania, księstwo (start, Brenna): czerwień ze złotymi pasami u góry i dołu, herb z Trygławem
 'stodorania_1_ksiestwo': svg(f'<rect width="300" height="200" fill="{TR}"/><rect width="300" height="16" fill="{TG}"/><rect y="184" width="300" height="16" fill="{TG}"/>'+img(TRY,TW,TH,150,100,72)),
 # Stodorania, republika: czerwień ze złotym pasem przez środek, bez godła
 'stodorania_2_republika': svg(f'<rect width="300" height="200" fill="{TR}"/><rect y="80" width="300" height="40" fill="{TG}"/>'),
 # Stodorania, rządy kapłanów Trygława: złote pole, herb na środku
 'stodorania_3_kaplani': svg(f'<rect width="300" height="200" fill="{TG}"/>'+img(TRYR,TW,TH,150,100,72)),
 # Stodorania rewolucyjna: czerwień, trzy złote gwiazdy w rzędzie (trzy głowy Trygława bez bóstwa)
 'stodorania_4_rewolucja': svg(f'<rect width="300" height="200" fill="{TR}"/>'+star(92,100,24,TG)+star(150,100,24,TG)+star(208,100,24,TG)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
