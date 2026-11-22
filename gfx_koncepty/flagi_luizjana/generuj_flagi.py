import math, os
OUT='/home/claude/vic3mod/gfx_koncepty/flagi_luizjana'
BLUE='#1f3f8f'; WHITE='#f7f4ec'; GOLD='#d9a92b'; RED='#b8282e'; PURPLE='#5b2a86'; GREEN='#3f7d3a'; BROWN='#6b4423'; INK='#1b2a55'
def star(cx,cy,r,col,rot=-90):
    pts=[]
    for i in range(10):
        rr=r if i%2==0 else r*0.42
        a=math.radians(rot+i*36)
        pts.append(f"{cx+rr*math.cos(a):.2f},{cy+rr*math.sin(a):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
def fleur(x,y,s,col):
    return f'''<g transform="translate({x},{y}) scale({s})" fill="{col}">
<path d="M0,-34 C10,-22 9,-6 2,4 L-2,4 C-9,-6 -10,-22 0,-34Z"/>
<path d="M-3,2 C-10,-8 -22,-14 -28,-6 C-33,1 -27,10 -20,7 C-24,3 -22,-2 -17,-2 C-11,-2 -8,2 -6,6Z"/>
<path d="M3,2 C10,-8 22,-14 28,-6 C33,1 27,10 20,7 C24,3 22,-2 17,-2 C11,-2 8,2 6,6Z"/>
<rect x="-14" y="5" width="28" height="5" rx="1.5"/>
<path d="M-5,10 L5,10 L4,22 L0,17 L-4,22Z"/>
<path d="M-6,10 C-12,14 -16,18 -18,24 C-12,22 -8,18 -5,14Z"/><path d="M6,10 C12,14 16,18 18,24 C12,22 8,18 5,14Z"/></g>'''
def pelican(x,y,s,body=WHITE,line=INK,nest=True):
    n=f'<path d="M-26,24 Q0,36 26,24 L22,30 Q0,40 -22,30Z" fill="{BROWN}"/>' if nest else ''
    return f'''<g transform="translate({x},{y}) scale({s})" stroke="{line}" stroke-width="1.6" stroke-linejoin="round">
{n}<path d="M-4,4 L-34,-26 L-26,-10 L-40,-14 L-22,10Z" fill="{body}"/>
<path d="M12,4 L42,-26 L34,-10 L48,-14 L30,10Z" fill="{body}"/>
<ellipse cx="5" cy="12" rx="18" ry="12" fill="{body}"/>
<path d="M-6,6 C-15,-4 -12,-18 -3,-21" fill="none" stroke-width="5" stroke="{line}"/>
<path d="M-6,6 C-15,-4 -12,-18 -3,-21" fill="none" stroke-width="3" stroke="{body}"/>
<circle cx="-3" cy="-22" r="5.5" fill="{body}"/>
<path d="M-7,-23 L-30,-13 L-7,-17Z" fill="{GOLD}"/>
<circle cx="-2" cy="-23" r="1.1" fill="{line}" stroke="none"/></g>'''
def eagle(x,y,s,col=GOLD,line='#7a5a10',letter=None):
    L=f'<text x="0" y="12" text-anchor="middle" font-family="Georgia,serif" font-weight="bold" font-size="18" fill="{PURPLE}" stroke="none">{letter}</text>' if letter else ''
    return f'''<g transform="translate({x},{y}) scale({s})" fill="{col}" stroke="{line}" stroke-width="1.2" stroke-linejoin="round">
<path d="M-6,-6 L-44,-30 L-38,-20 L-48,-18 L-40,-10 L-48,-4 L-36,0 L-40,8 L-14,8Z"/>
<path d="M6,-6 L44,-30 L38,-20 L48,-18 L40,-10 L48,-4 L36,0 L40,8 L14,8Z"/>
<path d="M-12,-8 Q0,-16 12,-8 L10,20 L0,28 L-10,20Z"/>
<circle cx="-3" cy="-20" r="7"/><path d="M-9,-21 L-17,-17 L-9,-15Z"/>
<rect x="-18" y="28" width="36" height="4" rx="2"/>{L}</g>'''
def laurel(x,y,r,col):
    out=[]
    for side in (-1,1):
        a0,a1=(115,250) if side<0 else (65,-70)
        sa,ea=math.radians(a0),math.radians(a1)
        sx,sy=x+r*math.cos(sa),y+r*math.sin(sa); ex,ey=x+r*math.cos(ea),y+r*math.sin(ea)
        sweep=1 if side<0 else 0
        out.append(f'<path d="M{sx:.1f},{sy:.1f} A{r},{r} 0 0 {sweep} {ex:.1f},{ey:.1f}" fill="none" stroke="{col}" stroke-width="2"/>')
        for i in range(8):
            t=i/7.5
            a=math.radians(a0+(a1-a0)*t)
            px,py=x+r*math.cos(a),y+r*math.sin(a)
            tang=math.degrees(a)+90
            for off in (35,-35):
                ox=px+6*math.cos(math.radians(tang+off+(180 if side<0 else 0)))*0.0
                rot=tang+off
                cx=px+5*math.cos(math.radians(rot)); cy=py+5*math.sin(math.radians(rot))
                out.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="6.5" ry="2.6" fill="{col}" transform="rotate({rot:.0f} {cx:.1f} {cy:.1f})"/>')
    return ''.join(out)
def crown(x,y,s,col=GOLD,gem=RED):
    return f'''<g transform="translate({x},{y}) scale({s})" fill="{col}" stroke="#7a5a10" stroke-width="1">
<path d="M-20,8 L-22,-8 L-10,0 L0,-12 L10,0 L22,-8 L20,8Z"/><rect x="-21" y="8" width="42" height="6"/>
<circle cx="-22" cy="-9" r="2.5"/><circle cx="0" cy="-13" r="2.5"/><circle cx="22" cy="-9" r="2.5"/>
<circle cx="0" cy="11" r="2" fill="{gem}" stroke="none"/></g>'''
def bee(x,y,s,col=GOLD):
    return f'''<g transform="translate({x},{y}) scale({s})" fill="{col}">
<ellipse cx="-5" cy="-3" rx="5" ry="3" opacity=".85"/><ellipse cx="5" cy="-3" rx="5" ry="3" opacity=".85"/>
<ellipse cx="0" cy="3" rx="3.2" ry="6"/><circle cx="0" cy="-4" r="2.4"/></g>'''
def river(y,col=WHITE,w=6):
    return f'<path d="M0,{y} Q37.5,{y-8} 75,{y} T150,{y} T225,{y} T300,{y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
def palm(x,y,s):
    fr=''.join(f'<ellipse cx="{x+18*s*math.cos(math.radians(a)):.1f}" cy="{y-70*s+10*s*math.sin(math.radians(a)):.1f}" rx="{20*s}" ry="{5*s}" fill="{GREEN}" transform="rotate({a} {x+18*s*math.cos(math.radians(a)):.1f} {y-70*s+10*s*math.sin(math.radians(a)):.1f})"/>' for a in (200,160,230,130,265,-20,20,-50,50))
    return f'<path d="M{x},{y} Q{x+6*s},{y-35*s} {x},{y-70*s}" stroke="{BROWN}" stroke-width="{6*s}" fill="none"/>'+fr
def chain(x1,x2,y,col='#e8e8e8'):
    out=[]; x=x1
    while x<x2:
        if abs(x-(x1+x2)/2)>14: out.append(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="3.5" fill="none" stroke="{col}" stroke-width="2.2"/>')
        x+=10
    return ''.join(out)
def anchor_hammer(x,y,col=WHITE):
    return f'''<g transform="translate({x},{y})" fill="{col}" stroke="{col}">
<g transform="rotate(-35)"><rect x="-3" y="-38" width="6" height="66"/><circle cx="0" cy="-42" r="7" fill="none" stroke-width="4"/><rect x="-14" y="-28" width="28" height="5"/><path d="M-24,18 Q0,40 24,18 L18,16 Q0,30 -18,16Z"/></g>
<g transform="rotate(35)"><rect x="-3" y="-30" width="6" height="62"/><rect x="-14" y="-40" width="28" height="12" rx="2"/></g></g>'''
def tobacco(x,y,s,col=GOLD):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M0,-34 C22,-20 22,18 0,34 C-22,18 -22,-20 0,-34Z" fill="{col}"/><path d="M0,-30 L0,34 M0,-10 L-10,-18 M0,-10 L10,-18 M0,8 L-12,0 M0,8 L12,0" stroke="#7a5a10" stroke-width="1.6" fill="none"/></g>'
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{body}</svg>'
F={}
side_fleurs=lambda x: ''.join(fleur(x,y,0.55,GOLD) for y in (45,100,155))
F['1_oligarchia']=svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="60" height="200" fill="{BLUE}"/><rect x="240" width="60" height="200" fill="{BLUE}"/>{side_fleurs(30)}{side_fleurs(270)}{fleur(150,38,0.6,GOLD)}{pelican(150,112,1.2)}')
F['2_demokracja']=svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="60" height="200" fill="{BLUE}"/><rect x="240" width="60" height="200" fill="{BLUE}"/>'+''.join(star(150+52*math.cos(math.radians(a)),112+52*math.sin(math.radians(a)),7,GOLD) for a in range(-160,-10,25))+pelican(150,118,1.05))
F['3_konsulat']=svg(f'<rect width="300" height="200" fill="{WHITE}"/><rect width="60" height="200" fill="{BLUE}"/><rect x="240" width="60" height="200" fill="{BLUE}"/><rect x="60" width="8" height="200" fill="{GOLD}"/><rect x="232" width="8" height="200" fill="{GOLD}"/>{laurel(150,100,62,GREEN)}{eagle(150,96,1.25)}')
F['4_cesarstwo']=svg(f'<rect width="300" height="200" fill="{PURPLE}"/>{laurel(150,108,62,GOLD)}{eagle(150,108,1.25,letter="N")}{crown(150,30,1.0)}'+''.join(bee(x,y,1.3) for x,y in ((28,28),(272,28),(28,172),(272,172))))
semé=''.join(fleur(x,y,0.38,GOLD) for x in range(20,300,40) for y in range(22,200,40) if not (95<x<205 and 40<y<175))
F['5_burbonowie']=svg(f'<rect width="300" height="200" fill="{BLUE}"/>{semé}<path d="M112,58 L188,58 L188,120 Q188,160 150,172 Q112,160 112,120Z" fill="{WHITE}" stroke="{GOLD}" stroke-width="3"/>{pelican(150,122,0.82)}{crown(150,42,0.9)}')
F['6_wolna']=svg(f'<rect width="300" height="100" fill="{BLUE}"/><rect y="100" width="300" height="100" fill="{RED}"/>{river(100,WHITE,10)}{palm(150,178,1.25)}{chain(60,240,150)}')
F['7_komuna']=svg(f'<rect width="300" height="200" fill="{RED}"/>{laurel(150,100,64,WHITE)}{anchor_hammer(150,98)}{river(184,WHITE,4)}')
F['8_konfederacja']=svg(f'<rect width="300" height="100" fill="{WHITE}"/><rect y="100" width="300" height="100" fill="{RED}"/><rect width="70" height="200" fill="{BLUE}"/>{star(35,65,15,WHITE)}{star(35,135,15,WHITE)}{pelican(185,58,0.75,nest=False)}{tobacco(185,150,1.05)}')
for k,v in F.items(): open(f'{OUT}/{k}.svg','w').write(v)
print(len(F))
