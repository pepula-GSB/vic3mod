"""Flagi Księstwa Pomorskiego (Gryfici, husyci, Hanza). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_pomorze/generuj_flagi.py"""
import base64, os, subprocess, math
HERE=os.path.dirname(os.path.abspath(__file__))
EMB=os.path.join(HERE,'..','emblematy')
def b64(n): return base64.b64encode(open(os.path.join(EMB,n),'rb').read()).decode()
GR=b64('gryf.png'); GRW=b64('gryf_bialy.png'); GW,GH=340,384
KRC=b64('kielich_czerwony_kontur.png'); KRW,KRH=89,162
KM=b64('kielich_maska_s.png'); KW,KH=300,581
WHITE='#fbfaf6'; BLUE='#1f4e8c'; RED='#c8102e'; BLACK='#111111'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
def gryf(b,cx,cy,h,flip=False):
    w=h*GW/GH; t=f' transform="translate({2*cx},0) scale(-1,1)"' if flip else ''
    return f'<g{t}><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{b}"/></g>'
def chalice(cx,cy,h,col):
    w=h*KW/KH; mid=f"k{int(cx)}{int(cy)}"
    return (f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="200"><image x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" href="data:image/png;base64,{KM}"/></mask></defs>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
def ring_text(cx,cy,r,top,bot,col,fs=13,ls=1.6,font='DejaVu Sans',ttf='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'):
    """Napis po okręgu (górny łuk i dolny łuk); każda litera osobno, bo librsvg nie obsługuje textPath."""
    from PIL import ImageFont
    f=ImageFont.truetype(ttf,100)
    def place(txt,upper):
        ws=[f.getlength(c)*fs/100+ls for c in txt]; tot=sum(ws)-ls; rr=r if upper else r+fs*0.72
        ang=tot/rr*180/math.pi; out=[]; acc=0
        for c,w in zip(txt,ws):
            mid=acc+(w-ls)/2; acc+=w; off=(mid/tot-.5)*ang
            a=270+off if upper else 90-off; rot=off if upper else -off
            x=cx+rr*math.cos(math.radians(a)); y=cy+rr*math.sin(math.radians(a))
            out.append(f'<text x="{x:.2f}" y="{y:.2f}" transform="rotate({rot:.2f} {x:.2f} {y:.2f})" text-anchor="middle">{c}</text>')
        return ''.join(out)
    return f'<g font-family="{font}" font-weight="bold" font-size="{fs}" fill="{col}">'+place(top,True)+(place(bot,False) if bot else '')+'</g>'
def star(cx,cy,r,col):
    p=[f"{cx+(r if i%2==0 else r*.4)*math.cos(math.radians(-90+i*36)):.2f},{cy+(r if i%2==0 else r*.4)*math.sin(math.radians(-90+i*36)):.2f}" for i in range(10)]
    return f'<polygon points="{" ".join(p)}" fill="{col}"/>'

F={
 # Księstwo (start, Gryfici): biel z niebieskim pasem morza u dołu, czerwony gryf
 '1_ksiestwo': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="160" width="300" height="40" fill="{BLUE}"/>'+gryf(GR,150,84,140)),
 # Republika kupiecka (Szczecin, Gdańsk, Hanza): niebieski pas przy drzewcu, gryf na bieli
 '2_republika': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="90" height="200" fill="{BLUE}"/>'+gryf(GR,195,100,150)),
 # Teokracja husycka: jak księstwo, ale pas u dołu czarny, a gryf trzyma w uniesionym szponie mały kielich
 '3_teokracja': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect y="160" width="300" height="40" fill="{BLACK}"/>'+gryf(GR,150,92,136)
                    +(lambda h:f'<image x="{104-h*KRW/KRH/2:.1f}" y="{22-h/2:.1f}" width="{h*KRW/KRH:.1f}" height="{h:.1f}" href="data:image/png;base64,{KRC}"/>')(28)),
 # Pomorze rewolucyjne: układ republiki, czerwona gwiazda zamiast gryfa, hasło po kaszubsku: „Cała władza ludowi”
 '4_rewolucja': svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="90" height="200" fill="{BLUE}"/>'+star(195,100,40,RED)+ring_text(195,100,56,'WSZËTKÔ MÒC','LËDOWI',BLUE)),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
