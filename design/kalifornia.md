# Łańcuch wydarzeń: wyzwolenie Kalifornii (1836–ok. 1850)

Projekt na poziomie koncepcji. Nazwy efektów i warunków Vic3 trzeba sprawdzić przed pisaniem skryptów.

## Realny zaczep
W listopadzie 1836 roku Juan Bautista Alvarado i Kalifornijczycy (*californios*) wyrzucili gubernatora mianowanego przez Meksyk i ogłosili Kalifornię **„wolnym i suwerennym państwem”**. Pomogli im zagraniczni strzelcy (Isaac Graham i jego ludzie). Meksyk w 1838 roku zrobił z Alvarado gubernatora i bunt wygasł. W 1846 roku przyszedł bunt pod „flagą niedźwiedzia” (Bear Flag Revolt), a potem aneksja przez USA.

W tym świecie nie ma USA, za to są Nowogród (Fort Ross), Nowa Francja (traperzy nad Columbią), Luizjana (awanturnicy), Nova Dania i Hiszpania.

## Postacie
### Juan Bautista Alvarado: główna postać łańcucha
- **Realnie**: urodzony w 1809 roku w Monterey. W 1836 roku poprowadził bunt Kalifornijczyków, ogłosił Kalifornię wolnym państwem, a potem był gubernatorem w latach 1836–1842. Wykształcony, ambitny, z wielkim ranczem.
- **W grze**: postać startowa w Kalifornii, agitator i przywódca ruchu Kalifornijczyków (liberalny federalista). Jego losy prowadzą łańcuch:
  - **Gubernator**: jeśli Meksyk go uzna (kalifornia.1), autonomia rośnie, bunt cichnie, ale Alvarado buduje własną władzę.
  - **Prezydent Republiki Kalifornijskiej**: jeśli dojdzie do niepodległości za jego życia, zostaje pierwszym przywódcą i odpowiednikiem założyciela państwa.
  - **Wygnaniec albo męczennik**: jeśli Meksyk zdusi bunt, Alvarado ucieka (do Fortu Ross albo do Nowej Francji) i wraca przy następnym kryzysie. Jeśli zginie, autonomia rośnie z gniewu, ale ruch traci przywódcę.
  - **Człowiek obcych**: przy przewadze cudzoziemców może stać się marionetką Nowogrodu albo Nowej Francji. Wydarzenie „Alvarado i strzelcy” zmusza go do wyboru między niezależnością a obcą pomocą.

### Postacie poboczne (realne)
- **Mariano Guadalupe Vallejo**: wuj Alvarado, dowódca wojskowy północy (Sonoma), sąsiad Fortu Ross. Kluczowy dla stosunków z Nowogrodem: może zawrzeć umowę zbożową albo bronić granicy.
- **José Castro**: towarzysz broni Alvarado, generał, a w razie wojny dowódca armii kalifornijskiej.
- **Pío Pico**: rywal z południa (Los Angeles). Realnie trwała rywalizacja północy (Monterey) z południem (Los Angeles). Tu Pico może poprowadzić frakcję „południową”, która woli Meksyk albo własną władzę zamiast Monterey. To grozi wojną domową w samej Kalifornii.

## Kraje biorące udział
- **Meksyk** (MEX): właściciel prowincji.
- **Kalifornia** (powstaje w trakcie łańcucha).
- **Nowogród** (Ameryka Nowogrodzka): potrzebuje zboża dla Alaski i ma Fort Ross.
- **Nowa Francja**: traperzy i koloniści nad Columbią i w dolinie Sacramento.
- **Luizjana**: awanturnicy, bonapartyści i kupcy.
- **Hiszpania**: marzy o odzyskaniu dawnej prowincji.

## Zmienne (na Meksyku)
| Zmienna | Znaczenie | Na start |
|---|---|---|
| `kal_autonomia` | dążenie Kalifornijczyków do samorządu | 40 |
| `kal_cudzoziemcy` | liczba i wpływ cudzoziemców w Kalifornii | 15 |
| `kal_kontrola` | realna władza Meksyku w Kalifornii | 30 |

Kontrola spada przy kryzysach w stolicy (zamachy, wojny, bankructwo). Liczba cudzoziemców rośnie z każdą falą osadników i z rozbudową Fortu Ross.

## Faza I: bunt Alvarado (1836)
**kalifornia.1 „Wolne i suwerenne państwo”** (start gry, MEX)
Kalifornijczycy pod przywództwem **Juana Bautisty Alvarado** wyrzucają gubernatora z Meksyku. Meksyk wybiera:
- *Wysłać wojsko* (koszt, ryzyko porażki przy niskiej kontroli),
- *Uznać Alvarado za gubernatora* (realne wyjście, autonomia rośnie, bunt cichnie),
- *Ogłosić Kalifornię zbuntowaną* (napięcie, a kontrola spada przy każdej porażce).

**kalifornia.2 „Strzelcy z Fortu Ross”** (wysyłane do Nowogrodu)
Alvarado prosi Nowogródzian o pomoc.
- *Wysłać strzelców i proch* (więcej cudzoziemców w Kalifornii, wdzięczność Kalifornijczyków, gniew Meksyku),
- *Zostać neutralnym*,
- *Zażądać zapłaty w zbożu*, czyli handel w zamian za pomoc (spichlerz Alaski).

**kalifornia.3 „Traperzy z Columbii”** (wysyłane do Nowej Francji): wybór analogiczny do kalifornia.2.

## Faza II: lata autonomii (ok. 1838–1845)
**kalifornia.4 „Kalifornijczycy kontra Meksyk”**: spory o podatki, cła w Monterey i ziemię misji (sekularyzacja misji, realna od 1834 roku).
**kalifornia.4a „Monterey kontra Los Angeles”**: Pío Pico i południe kwestionują władzę Alvarado. Ustąpić, podzielić władzę albo stłumić.
**kalifornia.5 „Rancza i obcy”**: cudzoziemcy kupują ziemię i żenią się z córkami kalifornijskich rodów. Rośnie wpływ zagranicy.
**kalifornia.6 „Spichlerz Alaski”**: Nowogród proponuje stałą umowę zbożową albo dzierżawę doliny (Bodega, Sonoma).
**kalifornia.7 „Złoto?”**: realnie złoto odkryto w Sutter's Mill w 1848 roku. Tu odkrycie (losowo ok. 1845–1850) zmienia wszystko: napływ awanturników z całego świata, liczba cudzoziemców gwałtownie rośnie, a wszyscy sąsiedzi nagle chcą Kalifornii.

## Faza III: rozstrzygnięcie (warunek: autonomia albo cudzoziemcy powyżej progu, albo kryzys w Meksyku)
**kalifornia.10 „Flaga niedźwiedzia”**
Osadnicy i Kalifornijczycy ogłaszają niepodległość. Kto prowadzi, zależy od zmiennych:
- przewaga Kalifornijczyków: **Republika Kalifornijska** pod przywództwem kalifornijskich rodów, hiszpańskojęzyczna i katolicka,
- przewaga cudzoziemców: **republika osadników**, wielojęzyczna, a z czasem zależna od jednego z mocarstw.

**kalifornia.11 „Kto pomoże?”**: Nowogród, Nowa Francja, Luizjana i Hiszpania wybierają: wsparcie, neutralność albo interwencję we własnym interesie.

## Możliwe wyniki
1. **Niepodległa Republika Kalifornijska**, wielokulturowa i bogata, zwłaszcza po złocie.
2. **Autonomia w Meksyku**, czyli kompromis jak realnie w 1838 roku.
3. **Protektorat nowogrodzki**: Kalifornia jako spichlerz Alaski, jedyna ciepła kolonia Nowogrodu.
4. **Protektorat Nowej Francji**: dostęp do Pacyfiku dla Quebecu.
5. **Powrót Hiszpanii**: najmniej prawdopodobny, ale możliwy przy rozpadzie Meksyku i wsparciu Kuby i Nowej Granady.
6. **Odzyskanie przez Meksyk**: wymaga wysokiej kontroli i stabilnego rządu w stolicy.

## Powiązania
- Rewolucja w Teksasie (Luizjana) i Jukatan osłabiają Meksyk naraz.
- Spór oregoński (cztery strony) splata się z losem Kalifornii.
- Gorączka złota zasila mechanikę poszukiwania kolonistów u wszystkich sąsiadów.
