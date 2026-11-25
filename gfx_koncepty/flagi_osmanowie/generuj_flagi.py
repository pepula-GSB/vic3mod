#!/usr/bin/env python3
"""Flagi Imperium Osmańskiego (stolica Adana) w wariantach ustrojowych. Półksiężyc i gwiazda rysowane geometrycznie wg wzoru od autora moda."""
import os, subprocess, math

HERE = os.path.dirname(os.path.abspath(__file__))
G = '#23b04c'; GD = '#0f6b32'; R = '#c8102e'; W = '#ffffff'; Y = '#facc00'; K = '#111111'


def star(cx, cy, r, col, rot=-90):
    pts = []
    for i in range(10):
        a = math.radians(rot) + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.382
        pts.append(f'{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'


def ksiezyc_gwiazda(col, mid, dx=0, s=1.0, star_col=None):
    """Półksiężyc i gwiazda zwrócona jednym ramieniem w stronę półksiężyca, jak we wzorze."""
    cx = 106.2 * s + dx
    c = (f'<mask id="{mid}"><rect width="300" height="200" fill="#000"/>'
         f'<circle cx="{cx:.2f}" cy="100" r="{56.2*s:.2f}" fill="#fff"/>'
         f'<circle cx="{cx + 18.3*s:.2f}" cy="100" r="{45*s:.2f}" fill="#000"/></mask>'
         f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')
    return c + star(cx + 68.4 * s, 100, 27.3 * s, star_col or col, rot=180)


def svg(b):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'


def bg(col):
    return f'<rect width="300" height="200" fill="{col}"/>'


F = {
    # Sułtanat (dynastia Osmanów, Adana): zieleń z białym półksiężycem i gwiazdą (wzór od autora moda)
    'osmanowie_1_sultanat': svg(bg(G) + ksiezyc_gwiazda(W, 'm')),
    # Republika: czerwień z białym półksiężycem i gwiazdą (nawiązanie do realnej czerwonej flagi osmańskiej)
    'osmanowie_2_republika': svg(bg(R) + ksiezyc_gwiazda(W, 'm')),
    # Kalifat (teokracja): ciemna zieleń ze złotym półksiężycem i gwiazdą
    'osmanowie_3_kalifat': svg(bg(GD) + ksiezyc_gwiazda(Y, 'm')),
    # Rewolucja: czerwień ze złotym półksiężycem i gwiazdą
    'osmanowie_4_rewolucja': svg(bg(R) + ksiezyc_gwiazda(Y, 'm')),
}

for k, v in F.items():
    p = os.path.join(HERE, k + '.svg')
    open(p, 'w').write(v)
    subprocess.run(['rsvg-convert', '-w', '600', '-h', '400', p, '-o', p[:-4] + '.png'], check=True)
