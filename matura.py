import sys
import csv
from klasa import Wojewodzctwo

def main():

    ##############czytanie pliku###############
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
    ###########################################

    woj_dict = {"-pl": 0, "-ds": 1, "-kp": 2, "-lbe": 3, "-lbu": 4, "-lo": 5, "-mp": 6, "-mz": 7, "-op": 8, "-pdk": 9,
                "-pdl": 10,
                "-po": 11, "-sl": 12, "-sw": 13, "-wm": 14, "-zp": 15, "bpr": 17, "r": 16}

    woj_num = woj_dict[sys.argv[1]]

    if(woj_num < 16):
        lista_wojewodzctw.append(Wojewodzctwo())
        for i in range(0, lines):
            if scores[i][0] == wojewodzctwa_nazwy[woj_num]:
                lista_wojewodzctw[0].addRow(scores[i])
        if(len(sys.argv) == 4):
            if(sys.argv[2] == "avg"):
                print(lista_wojewodzctw[0].avgAttendence(sys.argv[3]))
            if(sys.argv[2] == "pr"):
                print(lista_wojewodzctw[0].passRate(sys.argv[3]))
            if(sys.argv[2] == "c"):
                woj_num2 = woj_dict[sys.argv[3]]
                if (woj_num < 16):
                    lista_wojewodzctw.append(Wojewodzctwo())
                    for i in range(0, lines):
                        if scores[i][0] == wojewodzctwa_nazwy[woj_num2]:
                            lista_wojewodzctw[1].addRow(scores[i])
                    print(lista_wojewodzctw[0].compare(lista_wojewodzctw[1]))
        if (len(sys.argv) == 5):
            if (sys.argv[2] == "avg"):
                if(sys.argv[4] == "-m"):
                    print(lista_wojewodzctw[0].avgAttendence(sys.argv[3], 'mezczyzni'))
                if (sys.argv[4] == "-k"):
                    print(lista_wojewodzctw[0].avgAttendence(sys.argv[3], 'kobiety'))
            if (sys.argv[2] == "pr"):
                if(sys.argv[4] == "-m"):
                    print(lista_wojewodzctw[0].passRate(sys.argv[3], 'mezczyzni'))
                if (sys.argv[4] == "-k"):
                    print(lista_wojewodzctw[0].passRate(sys.argv[3], 'kobiety'))
            if (sys.argv[2] == "c"):
                woj_num2 = woj_dict[sys.argv[3]]
                if (woj_num < 16):
                    lista_wojewodzctw.append(Wojewodzctwo())
                    for i in range(0, lines):
                        if scores[i][0] == wojewodzctwa_nazwy[woj_num2]:
                            lista_wojewodzctw[1].addRow(scores[i])
                    if(sys.argv[4] == "-m"):
                        print(lista_wojewodzctw[0].compare(lista_wojewodzctw[1], 'mezczyzni'))
                    if (sys.argv[4] == "-k"):
                        print(lista_wojewodzctw[0].compare(lista_wojewodzctw[1], 'kobiety'))

    else:
        for x in range(0, 16):
            lista_wojewodzctw.append(Wojewodzctwo())
        for j in range(0, 16):
            for i in range(0, lines):
                if scores[i][0] == wojewodzctwa_nazwy[j]:
                    lista_wojewodzctw[j].addRow(scores[i])
        if (len(sys.argv) == 2):
            if(woj_num == 16):
                for i in lista_wojewodzctw:
                    print(i.regression())
                    print()
        elif(len(sys.argv) == 3):
            if(woj_num == 16 and sys.argv[2] == "-m"):
                for i in lista_wojewodzctw:
                    print(i.regression('mezczyzni'))
                    print()
            elif(woj_num == 16 and sys.argv[2] == "-k"):
                for i in lista_wojewodzctw:
                    print(i.regression('kobiety'))
                    print()
            if (woj_num == 17):
                najlepszy = 0
                for i in lista_wojewodzctw:
                    if (najlepszy < i.bestPassRate(sys.argv[2])):
                        najlepszy, wojewodzctwo = i.bestPassRate(sys.argv[2]), i.wojewodzctwo
                print(str(sys.argv[2])+ " - " + str(wojewodzctwo))
        elif(len(sys.argv) == 4):
            if(woj_num == 17):
                if(sys.argv[3] == "-m"):
                    najlepszy = 0
                    for i in lista_wojewodzctw:
                        if (najlepszy < i.bestPassRate(sys.argv[2], 'mezczyzni')):
                            najlepszy, wojewodzctwo = i.bestPassRate(sys.argv[2], 'mezczyzni'), i.wojewodzctwo
                    print(str(sys.argv[2]) + " - " + str(wojewodzctwo))
                if (sys.argv[3] == "-k"):
                    najlepszy = 0
                    for i in lista_wojewodzctw:
                        if (najlepszy < i.bestPassRate(sys.argv[2], 'kobiety')):
                            najlepszy, wojewodzctwo = i.bestPassRate(sys.argv[2], 'kobiety'), i.wojewodzctwo
                    print(str(sys.argv[2]) + " - " + str(wojewodzctwo))


if __name__ == '__main__':
    main()










