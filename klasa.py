class Wojewodzctwo:

    def __init__(self):
        self.lata = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.wojewodzctwo = ""
        self.mezczyzniPrzystapilo = []
        self.kobietyPrzystapilo = []
        self.mezczyzniZdalo = []
        self.kobietyZdalo =[]

    def addRow(self, values):
        self.wojewodzctwo = values[0]
        if(values[1] == 'przystąpiło' and values[2] == 'mężczyźni'):
            self.mezczyzniPrzystapilo.append(values[4])
        elif(values[1] == 'przystąpiło' and values[2] == 'kobiety'):
            self.kobietyPrzystapilo.append(values[4])
        elif(values[1] == 'zdało' and values[2] == 'mężczyźni'):
            self.mezczyzniZdalo.append(values[4])
        elif(values[1] == 'zdało' and values[2] == 'kobiety'):
            self.kobietyZdalo.append(values[4])

    def avgAttendence(self, *args):
        rok = 0
        for i in range (len(self.lata)):
            if int(args[0]) == self.lata[i]:
                rok = i + 1
        lista = []
        przystapilo = 0
        if(len(args) == 1):
            for i in range(rok):
                przystapilo += int(self.mezczyzniPrzystapilo[i]) + int(self.kobietyPrzystapilo[i])
            return (str(self.lata[rok-1]) + " - " + str(round(przystapilo/rok,2)))
        if(len(args) == 2):
            for i in range(rok):
                if(args[1] == 'mezczyzni'):
                    przystapilo += int(self.mezczyzniPrzystapilo[i])
                elif(args[1] == 'kobiety'):
                    przystapilo += int(self.kobietyPrzystapilo[i])
            return (str(self.lata[rok-1]) + " - " + str(round(przystapilo/rok,2)))


    def passRate(self, *args):
        rok = 0
        for i in range (len(self.lata)):
            if int(args[0]) == self.lata[i]:
                rok = i + 1
        lista = []
        if(len(args)) == 1:
            for i in range(rok):
                przystapilo = int(self.mezczyzniPrzystapilo[i]) + int(self.kobietyPrzystapilo[i])
                zdalo = int(self.mezczyzniZdalo[i]) + int(self.kobietyZdalo[i])
                procentowo = 100 * zdalo / przystapilo
                lista.append(str(self.lata[i]) + " - " + str(round(procentowo, 2)))
        if(len(args)) == 2:
            for i in range (rok):
                if(args[1] == 'mezczyzni'):
                    przystapilo = int(self.mezczyzniPrzystapilo[i])
                    zdalo = int(self.mezczyzniZdalo[i])
                elif(args[1] == 'kobiety'):
                    przystapilo = int(self.kobietyPrzystapilo[i])
                    zdalo = int(self.kobietyZdalo[i])
                procentowo = 100*zdalo/przystapilo
                lista.append(str(self.lata[i]) + " - " + str(round(procentowo, 2)))
        return lista

    def bestPassRate(self, *args):
        rok = 0
        for i in range(len(self.lata)):
            if int(args[0]) == self.lata[i]:
                rok = i
        if(len(args) == 1):
            przystapilo = int(self.mezczyzniPrzystapilo[rok]) + int(self.kobietyPrzystapilo[rok])
            zdalo = int(self.mezczyzniZdalo[rok]) + int(self.kobietyZdalo[rok])
            procentowo = 100 * zdalo / przystapilo
        if(len(args) == 2):
            if(args[1] == 'mezczyzni'):
                przystapilo = int(self.mezczyzniPrzystapilo[rok])
                zdalo = int(self.mezczyzniZdalo[rok])
                procentowo =  100 * zdalo / przystapilo
            if(args[1] == 'kobiety'):
                przystapilo = int(self.kobietyPrzystapilo[rok])
                zdalo = int(self.kobietyZdalo[rok])
                procentowo = 100 * zdalo / przystapilo
        return round(procentowo, 2)

    def regression(self, *args):
        rok = len(self.lata)
        lista = []
        lista2 =[]
        if(len(args)) == 0:
            for i in range(rok):
                przystapilo = int(self.mezczyzniPrzystapilo[i]) + int(self.kobietyPrzystapilo[i])
                zdalo = int(self.mezczyzniZdalo[i]) + int(self.kobietyZdalo[i])
                procentowo = 100 * zdalo / przystapilo
                lista.append(procentowo)
        if(len(args)) == 1:
            for i in range (rok):
                if(args[0] == 'mezczyzni'):
                    przystapilo = int(self.mezczyzniPrzystapilo[i])
                    zdalo = int(self.mezczyzniZdalo[i])
                elif(args[0] == 'kobiety'):
                    przystapilo = int(self.kobietyPrzystapilo[i])
                    zdalo = int(self.kobietyZdalo[i])
                procentowo = 100*zdalo/przystapilo
                lista.append(procentowo)
        for i in range(rok-1):
                if(lista[i] > lista[i+1]):
                    lista2.append(str(self.lata[i]) + " -> " + str(self.lata[i+1]))
        return (self.wojewodzctwo+ " - " + str(lista2))

    def compare(self, other, *args):
        rok = len(self.lata)
        lista = []
        if (len(args)) == 0:
            for i in range(rok):
                przystapilo1 = int(self.mezczyzniPrzystapilo[i]) + int(self.kobietyPrzystapilo[i])
                zdalo1 = int(self.mezczyzniZdalo[i]) + int(self.kobietyZdalo[i])
                procentowo1 = 100 * zdalo1 / przystapilo1
                przystapilo2 = int(other.mezczyzniPrzystapilo[i]) + int(other.kobietyPrzystapilo[i])
                zdalo2 = int(other.mezczyzniZdalo[i]) + int(other.kobietyZdalo[i])
                procentowo2 = 100 * zdalo2 / przystapilo2
                if(procentowo1 > procentowo2):
                    lista.append(str(self.lata[i]) + " - " + self.wojewodzctwo)
                else:
                    lista.append(str(self.lata[i]) + " - " + other.wojewodzctwo)
        if (len(args) == 1):
            for i in range(rok):
                if (args[0] == 'mezczyzni'):
                    przystapilo1 = int(self.mezczyzniPrzystapilo[i])
                    zdalo1 = int(self.mezczyzniZdalo[i])
                    procentowo1 = 100 * zdalo1 / przystapilo1
                    przystapilo2 = int(other.mezczyzniPrzystapilo[i])
                    zdalo2 = int(other.mezczyzniZdalo[i])
                    procentowo2 = 100 * zdalo2 / przystapilo2
                if (args[0] == 'kobiety'):
                    przystapilo1 = int(self.kobietyPrzystapilo[i])
                    zdalo1 = int(self.kobietyZdalo[i])
                    procentowo1 = 100 * zdalo1 / przystapilo1
                    przystapilo2 = int(other.kobietyPrzystapilo[i])
                    zdalo2 = int(other.kobietyZdalo[i])
                    procentowo2 = 100 * zdalo2 / przystapilo2
                if (procentowo1 > procentowo2):
                    lista.append(str(self.lata[i]) + " - " + self.wojewodzctwo)
                else:
                    lista.append(str(self.lata[i]) + " - " + other.wojewodzctwo)
        return lista
















