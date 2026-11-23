"""Flagi państw połabskich (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_polabie/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
GO=b64('gryf_obodrzycki.png'); GOW,GOH=332,410
BLUE='#1d6091'; GOLD='#f2b84b'; WHITE='#fbfaf6'; RED='#c8102e'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def img(b,w0,h0,cx,cy,h): w=h*w0/h0; return f'<image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/>'
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
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
