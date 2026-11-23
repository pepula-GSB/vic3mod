# Własny, uproszczony Trygław w stylu heraldycznym (bez związku z cudzą ilustracją)
import math
RED='#c8102e'; W='#f6f2e8'; K='#151515'; G='#e2b53a'
S='M10,10 L190,10 L190,130 Q190,205 100,232 Q10,205 10,130Z'
sw=2.6
def head_front(cx,cy):
    # włosy „pod garnek”, twarz owalna, wąsy opadające
    hair=f'<path d="M{cx-21},{cy-4} Q{cx-23},{cy-32} {cx},{cy-33} Q{cx+23},{cy-32} {cx+21},{cy-4} L{cx+21},{cy+6} L{cx-21},{cy+6}Z" fill="{G}" stroke="{K}" stroke-width="{sw}"/>'
    face=f'<path d="M{cx-16},{cy-6} L{cx+16},{cy-6} L{cx+16},{cy+14} Q{cx+14},{cy+34} {cx},{cy+38} Q{cx-14},{cy+34} {cx-16},{cy+14}Z" fill="{W}" stroke="{K}" stroke-width="{sw}"/>'
    fringe=f'<path d="M{cx-16},{cy-6} L{cx+16},{cy-6}" stroke="{K}" stroke-width="{sw}"/>'
    eyes=f'<circle cx="{cx-7}" cy="{cy+5}" r="2" fill="{K}"/><circle cx="{cx+7}" cy="{cy+5}" r="2" fill="{K}"/>'
    nose=f'<path d="M{cx},{cy+3} L{cx-2},{cy+16} L{cx+2},{cy+17}" fill="none" stroke="{K}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    must=f'<path d="M{cx},{cy+21} Q{cx-8},{cy+19} {cx-13},{cy+30} Q{cx-6},{cy+26} {cx},{cy+25} Q{cx+6},{cy+26} {cx+13},{cy+30} Q{cx+8},{cy+19} {cx},{cy+21}Z" fill="{K}"/>'
    strands=''.join(f'<path d="M{cx+dx},{cy-6} Q{cx+dx*1.05},{cy-20} {cx+dx*0.7},{cy-30}" stroke="{K}" stroke-width="1.1" fill="none"/>' for dx in (-14,-7,0,7,14))
    return hair+strands+face+fringe+eyes+nose+must
def head_profile(cx,cy,d):
    # d=-1 patrzy w lewo, d=+1 w prawo
    def X(x): return cx+d*x
    hair=f'<path d="M{X(16)},{cy+8} Q{X(26)},{cy-30} {X(-2)},{cy-32} Q{X(-20)},{cy-30} {X(-20)},{cy-6} L{X(-12)},{cy-6} L{X(16)},{cy+8}Z" fill="{G}" stroke="{K}" stroke-width="{sw}"/>'
    face=(f'<path d="M{X(-12)},{cy-6} L{X(4)},{cy-6} L{X(4)},{cy+20} Q{X(4)},{cy+34} {X(-4)},{cy+38} '
          f'Q{X(-14)},{cy+36} {X(-16)},{cy+28} L{X(-18)},{cy+24} L{X(-15)},{cy+21} L{X(-17)},{cy+18} '
          f'L{X(-23)},{cy+14} L{X(-16)},{cy+3} Z" fill="{W}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>')
    eye=f'<circle cx="{X(-9)}" cy="{cy+4}" r="2" fill="{K}"/>'
    must=f'<path d="M{X(-17)},{cy+21} Q{X(-8)},{cy+20} {X(-4)},{cy+28} Q{X(-10)},{cy+25} {X(-17)},{cy+25}Z" fill="{K}"/>'
    strands=''.join(f'<path d="M{X(dx)},{cy-6+ (dx+12)*0.5:.1f} Q{X(dx+3)},{cy-20} {X(dx*0.6)},{cy-30}" stroke="{K}" stroke-width="1.1" fill="none"/>' for dx in (-14,-6,2,10))
    return hair+strands+face+eye+must
def body():
    m=f'<path d="M34,232 L36,150 Q44,124 100,122 Q156,124 164,150 L166,232Z" fill="{W}" stroke="{K}" stroke-width="{sw}"/>'
    fold=f'<path d="M100,140 L100,232 M70,140 L62,232 M130,140 L138,232" stroke="{K}" stroke-width="1.6" fill="none"/>'
    brooch=f'<circle cx="100" cy="142" r="9" fill="{G}" stroke="{K}" stroke-width="{sw}"/><circle cx="100" cy="142" r="3" fill="{K}"/>'
    return m+fold+brooch
def halo():
    out=''
    for cx in (58,100,142):
        out+=f'<circle cx="{cx}" cy="{82 if cx!=100 else 74}" r="40" fill="{G}" opacity="1"/>'
    return f'<g>{out}</g>'
def nimbus_rays():
    rays=''
    for a in range(-170,-9,10):
        r1,r2=62,86; ca=math.cos(math.radians(a)); sa=math.sin(math.radians(a))
        rays+=f'<line x1="{100+r1*ca:.1f}" y1="{104+r1*sa:.1f}" x2="{100+r2*ca:.1f}" y2="{104+r2*sa:.1f}" stroke="{G}" stroke-width="3" stroke-linecap="round"/>'
    return rays
body_svg=(f'<defs><clipPath id="c"><path d="{S}"/></clipPath></defs><path d="{S}" fill="{RED}"/>'
          f'<g clip-path="url(#c)">{nimbus_rays()}{body()}'
          f'<rect x="50" y="120" width="14" height="16" fill="{W}" stroke="{K}" stroke-width="{sw}"/><rect x="136" y="120" width="14" height="16" fill="{W}" stroke="{K}" stroke-width="{sw}"/><rect x="92" y="114" width="16" height="18" fill="{W}" stroke="{K}" stroke-width="{sw}"/>'
          f'{head_profile(58,90,-1)}{head_profile(142,90,1)}{head_front(100,80)}</g>'
          f'<path d="{S}" fill="none" stroke="{K}" stroke-width="4"/>')
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 242" width="800" height="968">{body_svg}</svg>'
open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"..","emblematy","tryglaw_herb.svg"),"w").write(svg)
