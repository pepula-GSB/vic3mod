"""Flagi Cesarstwa Bułgarsko-Romejskiego (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_romania/generuj_flagi.py
Łączy romejski krzyż z czterema krzesiwami (tetragrammatyczny, Paleologowie) z bułgarską tamgą IYI rodu Dulo."""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
KRZ=b64('krzesiwo_bizantyjskie_maska.png'); KW,KH=676,908
HAMZ=b64('mlot_zloty_s.png'); HW,HH=240,623
RED='#b0001a'; GOLD='#fdc70f'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
_n=[0]
def krzesiwo(cx,cy,h,col,flip=False):
    _n[0]+=1; mid=f"kz{_n[0]}"; w=h*KW/KH
    t=f' transform="translate({2*cx},0) scale(-1,1)"' if flip else ''
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="-300" y="0" width="900" height="200"><g{t}><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KRZ}"/></g></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def iyi(cx,cy,w,col):
    """Tamga IYI: trzy pionowe belki złączone u dołu."""
    h=w*0.453; bw=w*0.176; bb=h*0.31; x0=cx-w/2; y0=cy-h/2
    d=(f'M{x0:.2f},{y0:.2f} h{bw:.2f} v{h-bb:.2f} h{(w-3*bw)/2:.2f} v{-(h-bb):.2f} h{bw:.2f} v{h-bb:.2f} h{(w-3*bw)/2:.2f} v{-(h-bb):.2f} h{bw:.2f} v{h:.2f} h{-w:.2f}Z')
    return f'<path d="{d}" fill="{col}"/>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'
def tetragram(center=''):
    return (f'<rect width="300" height="200" fill="{RED}"/><rect x="133" width="34" height="200" fill="{GOLD}"/><rect y="82" width="300" height="36" fill="{GOLD}"/>'
            +krzesiwo(65,37,57,GOLD)+krzesiwo(65,163,57,GOLD)+krzesiwo(234,37,57,GOLD,True)+krzesiwo(234,163,57,GOLD,True)+center)

F={
 # Cesarstwo (start): romejski krzyż z krzesiwami, na skrzyżowaniu czerwona tamga IYI
 '1_cesarstwo': svg(tetragram(iyi(150,100,26,RED))),
 # Republika: na wzór flagi greckiej. Dziewięć pasów czerwień-złoto, w kantonie czerwień ze złotym krzyżem
 '2_republika': svg(''.join(f'<rect y="{k*200/9:.3f}" width="300" height="{200/9+0.05:.3f}" fill="{RED if k%2==0 else GOLD}"/>' for k in range(9))
                    +f'<rect width="{200*5/9:.3f}" height="{200*5/9:.3f}" fill="{RED}"/>'
                    +f'<rect x="{200*2/9:.3f}" width="{200/9:.3f}" height="{200*5/9:.3f}" fill="{GOLD}"/><rect y="{200*2/9:.3f}" width="{200*5/9:.3f}" height="{200/9:.3f}" fill="{GOLD}"/>'),
 # Rewolucja: wzór republiki (greckie pasy), w kantonie złoty młot zamiast krzyża, na złotych pasach hasło po grecku:
 # „Proletariusze wszystkich krajów, łączcie się!”
 '3_rewolucja': svg(''.join(f'<rect y="{k*200/9:.3f}" width="300" height="{200/9+0.05:.3f}" fill="{RED if k%2==0 else GOLD}"/>' for k in range(9))
                    +f'<rect width="{200*5/9:.3f}" height="{200*5/9:.3f}" fill="{RED}"/>'
                    +f'<g transform="translate({100*5/9:.2f},{100*5/9:.2f}) rotate(35)"><image x="{-84*HW/HH/2:.1f}" y="-42" width="{84*HW/HH:.1f}" height="84" href="data:image/png;base64,{HAMZ}"/></g>'
                    +f'<g font-family="DejaVu Sans" font-weight="bold" fill="{RED}" text-anchor="middle">'
                     f'<text x="150" y="{200*6/9-5.2:.2f}" font-size="13.5" letter-spacing="0.6">ΠΡΟΛΕΤΑΡΙΟΙ ΟΛΩΝ ΤΩΝ ΧΩΡΩΝ,</text>'
                     f'<text x="150" y="{200*8/9-5.2:.2f}" font-size="13.5" letter-spacing="2">ΕΝΩΘΕΙΤΕ!</text></g>'),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
