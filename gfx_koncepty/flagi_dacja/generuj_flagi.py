"""Flagi Dacji i jej regionów (koncepty). Uruchom z katalogu repo:
python3 gfx_koncepty/flagi_dacja/generuj_flagi.py"""
import os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200" width="1536" height="1024">{b}</svg>'
F={
 # Panonia (katolicki zachód Dacji między Karpatami a Cisą, jeśli się oderwie): błękit, czerwień, żółć (wzór od autora moda)
 'panonia': svg('<rect width="300" height="67" fill="#0b5685"/><rect y="67" width="300" height="66" fill="#b20000"/><rect y="133" width="300" height="67" fill="#facc00"/>'),
}
for k,v in F.items():
    p=os.path.join(HERE,k+'.svg'); open(p,'w').write(v)
    subprocess.run(['rsvg-convert','-w','600','-h','400',p,'-o',p[:-4]+'.png'],check=True)
