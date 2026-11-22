# Łańcuch wydarzeń: Bezkrólewie śląskie (1836–ok. 1850)

Projekt łańcucha do journal entry „Bezkrólewie śląskie”. Opis jest na poziomie projektu. Nazwy efektów i warunków Vic3 trzeba sprawdzić w aktualnej wersji gry przed pisaniem skryptów.

## Założenia
- **Start**: 1836.1.1. Stary książę z wrocławskiej linii Przemyślidów żyje, ale nie ma syna.
- **Śmierć księcia: ok. 1845.** Okno losowe od 1844.6 do 1846.6, żeby gracz nie znał dokładnej daty. Do tego czasu trwa **faza przygotowań** (ok. 9 lat), w której stronnictwa zbierają poparcie.
- **Kraje biorące udział**: Śląsk (SIL), Morawy (MOR), Czechy (CZE), Polska (POL). Pozostali (Pomorze, Francja, Niderlandy, Burgundia, Saksonia, Austria, Łużyce, Miśnia) wchodzą dopiero w fazie wojny.

## Zmienne (na kraju SIL)
| Zmienna | Znaczenie | Na start |
|---|---|---|
| `slask_republika` | poparcie dla republiki | 25 |
| `slask_praga` | poparcie dla linii praskiej | 30 |
| `slask_welehrad` | poparcie dla wcielenia do Moraw | 25 |
| `slask_polska` | poparcie dla polskiego kandydata | 20 |
| `slask_napiecie` | ryzyko wojny domowej (0–100) | 10 |

**Comiesięczny dryf** (pulse), zależny od siły grup interesu na Śląsku:
- przemysłowcy, mieszczaństwo i inteligencja wzmacniają republikę,
- ziemianie wzmacniają linię praską albo polską (zależnie od regionu),
- armia i urzędnicy wzmacniają opcję morawską,
- radykałowie i niezadowolenie podnoszą napięcie.

## Faza I: przygotowania (1836 – śmierć księcia)

**silesia.1 „Stary książę”** (start gry, SIL)
Książę wie, że linia gaśnie. Kogo wskazać?
- *Zwołać Sejm wcześniej* (+republika, +napięcie, Sejm zyskuje legitymację).
- *Napisać do Pragi* (+Praga, Morawy dostają silesia.3 wcześniej).
- *Zdać się na Welehrad* (+Welehrad, −legitymacja dynastii, niezadowolenie mieszczan).

**silesia.2 „Posłowie z Pragi”** (ok. 1837, SIL i CZE)
Praga proponuje małżeństwo albo adopcję.
- SIL: *przyjąć* (+Praga), *odesłać z honorami* (bez zmian), *ujawnić Welehradowi* (+Welehrad, gniew Pragi).
- CZE: koszt w autorytecie albo pieniądzach za każdą kolejną ofertę.

**silesia.3 „Prawo lenne”** (ok. 1838, MOR)
Prawnicy Welehradu twierdzą, że wygasłe lenno wraca do korony.
- *Ogłosić roszczenie* (+Welehrad, +napięcie, Czechy dostają modyfikator obrazy).
- *Obiecać Śląskowi autonomię po wcieleniu* (+Welehrad, −napięcie, koszt w legitymacji centralizatorów).
- *Przekupić magnatów* (pieniądze, +Welehrad u przemysłowców).

**silesia.4 „Wesele w Gnieźnie”** (ok. 1839, POL i SIL)
Córka księcia wychodzi za polskiego królewicza.
- POL: *ogłosić prawa dziedziczne* (+Polska, gorsze stosunki z MOR), *zachować w tajemnicy* (+Polska, mniej).
- SIL: *błogosławić* (+Polska), *zakazać* (−Polska, gniew Polski).

**silesia.5 „Petycja wrocławskich mieszczan”** (warunek: republika ≥ 35, SIL)
Rada Wrocławia żąda, żeby Sejm sam wybrał formę rządu.
- *Przyjąć do obrad Sejmu* (+republika, legalizacja ruchu).
- *Rozwiązać milicje miejskie* (−republika, +napięcie, możliwe zamieszki: silesia.6).
- *Kompromis: konstytucja księstwa* (+republika, mniej; −napięcie; reforma ustroju Śląska).

**silesia.6 „Zamieszki we Wrocławiu”** (po rozwiązaniu milicji albo przy napięciu ≥ 50)
- *Stłumić siłą* (−republika na krótko, +napięcie na długo).
- *Ustąpić* (+republika).
- *Wezwać wojsko morawskie* (+Welehrad, ++napięcie, republikanie radykalizują się).

**silesia.7 „Kredyt z Antwerpii”** (republika ≥ 40, wysyłane do BUR i NED)
Bankierzy proponują finansowanie śląskich republikanów w zamian za koncesje kopalniane.
- *Finansować* (koszt, +republika, prawa do śląskiego przemysłu po zwycięstwie republiki).
- *Odmówić*.

**silesia.8 „Strajk w kopalniach”** (ok. 1842–1844, Górny Śląsk)
Robotnicy żądają praw w zamian za poparcie.
- *Obiecać prawa pracownicze* (+republika, gniew przemysłowców).
- *Wezwać wojsko* (+Welehrad, +radykalizm).
- *Ignorować* (+napięcie).

**silesia.9 „Książę słabnie”** (1843–1844, SIL)
Zapowiedź finału. Ostatnia szansa, żeby wskazać następcę testamentem.
- *Testament na rzecz Pragi / Polski / Sejmu* (+15 dla wybranej opcji, gniew pozostałych).
- *Nie zostawiać testamentu* (+napięcie).

## Faza II: śmierć i Sejm (ok. 1845)

**silesia.10 „Śmierć księcia”** (losowo 1844.6–1846.6, SIL, powiadomienie dla MOR, CZE, POL)
Linia wrocławska wygasa. Zwołanie Wielkiego Sejmu.

**silesia.11 „Wielki Sejm we Wrocławiu”** (kilka miesięcy po silesia.10)
Głosowanie. Opcja z poparciem ≥ 50 wygrywa pokojowo:
- **republika**: silesia.20,
- **Praga**: silesia.21,
- **Welehrad**: silesia.22,
- **Polska**: silesia.23.

Jeśli żadna opcja nie ma 50 albo napięcie ≥ 60: silesia.12.

**silesia.12 „Sejm się rozpada”**
Posłowie wychodzą z sali. Każde stronnictwo ogłasza swojego władcę. **Start wojny domowej.**

## Faza III: wojna domowa

**Mechanika**: Śląsk dzieli się na państwa stronnictw według regionów:
- republikanie: Wrocław, miasta nad Odrą, część Górnego Śląska,
- linia praska: Sudety, Kłodzko, Jelenia Góra,
- stronnictwo morawskie: Racibórz, pogranicze z Pszczyną,
- stronnictwo polskie: Opolszczyzna, Wschowa, Milicz.

Słabsze stronnictwa można scalić w jedno „lojalistyczne” albo zostawić osobno, zależnie od tego, co pozwala silnik.

**silesia.13 „Wezwanie o pomoc”** (wysyłane do sąsiadów, każdy wybiera)

| Kraj | Opcje |
|---|---|
| Pomorze | wspierać republikę (wolna Odra) / neutralność |
| Francja | subsydia dla republiki / neutralność |
| Niderlandy, Burgundia | kredyt i ochotnicy dla republiki / neutralność |
| Nowogród | ochotnicy dla republiki / neutralność |
| Czechy | interwencja zbrojna dla linii praskiej / tylko pieniądze |
| Łużyce, Miśnia | cicha pomoc dla Pragi / lojalność wobec Welehradu |
| Morawy | interwencja zbrojna („przywrócenie porządku”) / mediacja |
| Polska | interwencja dla swojego kandydata / tylko protest |
| Saksonia, Austria | broń i pieniądze dla przeciwników Moraw / neutralność |

Interwencja odbywa się przez dyplomatyczną grę o poparcie stron wojny domowej.

**silesia.14 „Oblężenie Wrocławia”**, **silesia.15 „Most na Odrze”**, **silesia.16 „Kopalnie stają”**: wydarzenia z okresu wojny, które zmieniają morale, gospodarkę i poparcie zagranicy.

## Faza IV: rozstrzygnięcie

**silesia.20 „Republika Śląska”**
Nowy ustrój. Jeśli Morawy jej nie uznają: wojna o niepodległość. Jeśli uznają: Śląsk wychodzi z korony.

**silesia.21 „Unia z Pragą”**
Śląsk przechodzi pod Czechy. Blok Przemyślidów w koronie morawskiej. Uruchamia JE „Korona morawska” w trybie kryzysu.

**silesia.22 „Wcielenie do Moraw”**
Koniec autonomii. Śląski ruch narodowy staje się ruchem secesyjnym.

**silesia.23 „Polski książę we Wrocławiu”**
Zbliżenie z Polską, wojna albo zimna wojna z Morawami. Polska dostaje roszczenia.

**silesia.30 „Echo w koronie”** (po każdym wyniku innym niż silesia.22)
Czechy, Łużyce i Miśnia dostają wydarzenia o rozszerzeniu autonomii. Prawdopodobieństwo jest tym większe, im bardziej Morawy osłabły.

## Do decyzji
- Czy wojna domowa ma 2 strony (republika kontra lojaliści) czy 4 (każde stronnictwo osobno)?
- Czy Republika Śląska może później dołączyć do zjednoczenia lechickiego albo federacji zachodniosłowiańskiej?
- Czy wynik ma wpływać na kwestię śląskiej kultury (np. bonus do tożsamości narodowej przy republice)?
