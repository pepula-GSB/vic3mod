#!/usr/bin/env python3
"""Flagi Sułtanatu Omanu i Zanzibaru w wariantach ustrojowych."""
import os, base64, subprocess, math
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
EMB = os.path.join(HERE, '..', 'emblematy')
R = '#d40000'; W = '#ffffff'; Y = '#facc00'; G = '#00843d'


def b64(name):
    p = os.path.join(EMB, name)
    w, h = Image.open(p).size
    return base64.b64encode(open(p, 'rb').read()).decode(), w, h


def maska(name, cx, cy, width, col, mid):
    """Monochromatyczny emblemat (biała maska) przemalowany na kolor col, wyśrodkowany w (cx, cy)."""
    b, w0, h0 = b64(name)
    h = width * h0 / w0
    x, y = cx - width / 2, cy - h / 2
    return (f'<mask id="{mid}"><image x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" height="{h:.2f}" '
            f'href="data:image/png;base64,{b}"/></mask>'
            f'<rect width="300" height="200" fill="{col}" mask="url(#{mid})"/>')


def star(cx, cy, r, col):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.382
        pts.append(f'{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'


def svg(b):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'


F = {
    # Sułtanat (Al Bu Sa'id, Maskat i Zanzibar): gładka czerwień, jak realna bandera sułtanów
    'oman_1_sultanat': svg(f'<rect width="300" height="200" fill="{R}"/>'),
    # Imamat ibadycki: biel, czerwona szabla i napis „Nasrun min Allahi wa fathun qarib” (wzór od autora moda)
    'oman_2_imamat': svg(f'<rect width="300" height="200" fill="{W}"/>'
                         + maska('oman_imamat_maska.png', 150, 100, 200, R, 'm')),
    # Republika: czerwień z białą szablą, bez napisu religijnego
    'oman_3_republika': svg(f'<rect width="300" height="200" fill="{R}"/>'
                            + maska('szabla_oman_maska.png', 150, 100, 200, W, 'm')),
    # Rewolucja: czerwień, biała szabla, nad nią żółta gwiazda
    'oman_4_rewolucja': svg(f'<rect width="300" height="200" fill="{R}"/>'
                            + maska('szabla_oman_maska.png', 150, 116, 200, W, 'm')
                            + star(150, 62, 24, Y)),
}

for k, v in F.items():
    p = os.path.join(HERE, k + '.svg')
    open(p, 'w').write(v)
    subprocess.run(['rsvg-convert', '-w', '600', '-h', '400', p, '-o', p[:-4] + '.png'], check=True)
