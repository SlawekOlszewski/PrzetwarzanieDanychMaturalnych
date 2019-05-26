# Przetwarzanie Danych z Matur 2010-2018
Projekt umożliwia analizę danych ze strony https://dane.gov.pl/dataset/1567/resource/17363, są to dane dotyczące osób które przystąpiły oraz zdały maturę w latach 2010-2018 z uwzględnieniem podziału na wojewódzctwo oraz płeć.
## Pobieranie projektu
Aby postawić projekt należy sklonować repozytorium. W folderze w którym znajdują się pliki należy uruchomić wiersz poleceń. Każdą z funkcji skryptu uruchamiamy wpisując najpierw:
```bash
python matura.py 
```
następnie dodając odpowiednią komendę według instrukcji poniżej. 

## Dostępne komendy
Jeżeli chcemy, aby dane były wyświetlone tylko dla danej płci, jako ostatni argument podajemy:
```bash
-k #kobiety
-m #mężczyźni
```
Jeśli dane mają być wyświetlone dla obu płci, nie musimy nic dodatkowo podawać.
#### Średnia liczba osób, które przystąpiły do egzaminu dla danego wojewódzctwa(lista skrótów wojewódzctw na samym dole) na przestrzeni lat
Składnia
```bash
-wojewodzctwo avg rok
```
Przykładowa pełna komenda - zwróci ona dane dotyczące średniej liczby mężczyzn jakie przystąpiły do matury w wojewódzctwie Dolnośląskim do roku 2011
```bash
python matura.py -ds avg 2011 -m
```
Ta sama komenda, lecz dla obydwu płci wyglądała by:
```bash
python matura.py -ds avg 2011
```

#### Procentowa zdawalność dla danego wojewódzctwa na przestrzeni lat
Składnia
```bash
-wojewodzctwo pr rok
```

Przykładowa pełna komenda - zwróci dane dotyczące procentowej zdawalności matur w wojewódzctwie Pomorskim do roku 2018 wśród obu płci
```bash
python matura.py -po pr 2018
```

#### Podanie wojewódzctwa o najlepszej zdawalności w konkretnym roku
Składnia
```bash
bpr rok
```

Przykładowa pełna komenda - zwróci wojewódzctwo które w roku 2016 miało najlepszą zdawalność wśród kobiet
```bash
python matura.py bpr 2016 -k
```

#### Wykrycie wojewódzctw które zanotowały regresję
Składnia
```bash
r
```

Przykładowa pełna komenda - zwróci listy dla każdego wojewódzctwa pokazujące czy nastąpiła regresja wśród kobiet
```bash
python matura.py r -k
```

#### Porównanie dwóch wojewódzctw pod względem zdawalności w każdym dostępnym roku
Składnia
```bash
-wojewodzctwo1 c -wojewodzctwo2
```

Przykładowa pełna komenda - zwróci które z wojewódzctw(Małopolskie czy Mazowieckie) miało lepszą zdawalność w każdym dostępnym roku wśród obu płci
```bash
python matura.py -mp c -mz
```

## Lista skrótów wojewódzctw
Cała Polska -pl

Dolnośląskie -ds

Kujawsko-Pomorskie -kp

Lubelskie -lbe

Lubuskie -lbu

Łódzkie -lo

Małopolskie -mp

Mazowieckie -mz

Opolskie -op

Podkarpackie -pdk

Podlaskie -pdl

Pomorskie -po

Śląskie -sl

Świetokrzyskie -sw

Warmińsko-Mazurskie -wm

Zachodniopomorskie -zp

## Testy
Aby uruchomić napisane przeze mnie testy jednostkowe, należy najpierw zainstalować bibliotekę pytest poprzez wpisanie w linii poleceń
```bash
pip install pytest
```
Następnym krokiem jest uruchomienie wiersza poleceń w lokalizacji plików projektu i wpisanie komendy
```bash
python -m pytest
```
## Alternatywne rozwiązanie używając zewnętrznych bibliotek
Możnaby użyc biblioteki pandas. Wymagałoby to początkowo przekonwertowania pliku z danymi do struktury DataFrame. Wyliczanie danych wartości ograniczyłoby się wtedy do kilku linijek. Przykładowo wyliczenie  średniej liczby osób jakie przystąpiły do matury do 2015 roku w wojewódzctwie Pomorskim
```python
import pandas as pd
data = pd.read_csv("Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv")
avgAttendence = data.liczba_osob[(data.przystąpiło_zdało == 'Przystąpiło') & (data.terytorium == 'Pomorskie') & (data.rok <= 2015)].mean()
```
