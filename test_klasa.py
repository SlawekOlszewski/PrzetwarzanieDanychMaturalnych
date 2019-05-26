from klasa import Wojewodzctwo
import csv

filename = "Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv"
scores = []
lista_wojewodzctw = []
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    for row in csvReader:
        scores.append(row)
    lines = csvReader.line_num

wojewodzctwa_nazwy = ['Polska', 'Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Łódzkie', 'Małopolskie',
                          'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie',
                          'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Zachodniopomorskie']

for x in range(0, 16):
    lista_wojewodzctw.append(Wojewodzctwo())
for j in range(0, 16):
    for i in range(0, lines):
        if scores[i][0] == wojewodzctwa_nazwy[j]:
            lista_wojewodzctw[j].addRow(scores[i])

def test_avgAttendence():
    polska = lista_wojewodzctw[0].avgAttendence(2010)
    dolnos = lista_wojewodzctw[1].avgAttendence(2015, 'mezczyzni')
    pomorskie = lista_wojewodzctw[11].avgAttendence(2012, 'kobiety')

    assert polska == ('2010 - 366623.0')
    assert dolnos == ('2015 - 8988.5')
    assert pomorskie == ('2012 - 10979.33')

def test_passRate():
    mazowieckie = lista_wojewodzctw[7].passRate(2013)
    lodzkie = lista_wojewodzctw[5].passRate(2012, 'kobiety')
    slaskie = lista_wojewodzctw[12].passRate(2011, 'mezczyzni')

    assert mazowieckie == ['2010 - 81.61', '2011 - 76.4', '2012 - 80.57', '2013 - 80.93']
    assert lodzkie == ['2010 - 83.26', '2011 - 76.44', '2012 - 80.64']
    assert slaskie == ['2010 - 81.03', '2011 - 75.33']

def test_bestPassRate():
    najlepszy = 0
    for i in lista_wojewodzctw:
        if (najlepszy < i.bestPassRate(2012)):
            najlepszy, wojewodzctwo = i.bestPassRate(2012), i.wojewodzctwo
    returining1 = (str(2012) + " - " + str(wojewodzctwo))

    najlepszy = 0
    for i in lista_wojewodzctw:
        if (najlepszy < i.bestPassRate(2014)):
            najlepszy, wojewodzctwo = i.bestPassRate(2014, 'mezczyzni'), i.wojewodzctwo
    returining2 = (str(2014) + " - " + str(wojewodzctwo))

    najlepszy = 0
    for i in lista_wojewodzctw:
        if (najlepszy < i.bestPassRate(2018)):
            najlepszy, wojewodzctwo = i.bestPassRate(2018, 'kobiety'), i.wojewodzctwo
    returining3 = (str(2018) + " - " + str(wojewodzctwo))

    assert returining1 == ('2012 - Małopolskie')
    assert returining2 == ('2014 - Lubuskie')
    assert returining3 == ('2018 - Małopolskie')

def test_regression():
    warm = lista_wojewodzctw[14].regression()
    podkar = lista_wojewodzctw[9].regression('mezczyzni')
    opolsk = lista_wojewodzctw[8].regression('kobiety')

    assert warm == ("Warmińsko-Mazurskie - ['2010 -> 2011', '2013 -> 2014', '2016 -> 2017']")
    assert podkar == ("Podkarpackie - ['2010 -> 2011', '2012 -> 2013', '2013 -> 2014', '2016 -> 2017']")
    assert opolsk == ("Opolskie - ['2010 -> 2011', '2013 -> 2014', '2016 -> 2017']")

def test_compare():
    warmVSpolska = lista_wojewodzctw[14].compare(lista_wojewodzctw[0])
    opolVSlodz = lista_wojewodzctw[8].compare(lista_wojewodzctw[5], 'mezczyzni')
    kujpomVSzachodpom = lista_wojewodzctw[2].compare(lista_wojewodzctw[15], 'kobiety')

    assert warmVSpolska == (['2010 - Polska', '2011 - Polska', '2012 - Polska', '2013 - Polska', '2014 - Polska', '2015 - Polska', '2016 - Polska', '2017 - Polska', '2018 - Polska'])
    assert opolVSlodz == (['2010 - Opolskie', '2011 - Łódzkie', '2012 - Łódzkie', '2013 - Opolskie', '2014 - Łódzkie', '2015 - Opolskie', '2016 - Opolskie', '2017 - Łódzkie', '2018 - Opolskie'])
    assert kujpomVSzachodpom == (['2010 - Kujawsko-pomorskie', '2011 - Kujawsko-pomorskie', '2012 - Kujawsko-pomorskie', '2013 - Kujawsko-pomorskie', '2014 - Kujawsko-pomorskie', '2015 - Kujawsko-pomorskie', '2016 - Kujawsko-pomorskie', '2017 - Kujawsko-pomorskie', '2018 - Kujawsko-pomorskie'])