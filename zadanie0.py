baza_zagadek={'podaj nazwe jezyka programowania, ktorego dotyczyly zajecia':'python','jaki typ danych jest zapisywany z uzyciem[]':'lista','jaki typ danych jest zapisywany z uzyciem {}':'slownik','czy krotke mozna modyfikowac':'nie','czy liste mozna modyfikowac':'tak','jak zapisujemy typ danych string':'str','jak sie nazywa funkcja, ktora czeka na wpisanie czegos z klawiatury':'input','jakiego typu bedzie wartosc podana przez uzytkownika w ramach funkcji input':'string','jak sie nazywa element, do ktorego przypisana jest wartosc w slowniku':'klucz','jak sie nazywa struktura zapisywana z uzyciem ()':'krotka','do jakiej zmiennej srodowiskowej trzeba dodac sciezke do pythona w systemie windows':'path'}
wskaznik_procentowy_odp_poprawnych=0
liczba_udzielonych_odpowiedzi=0
liczba_odpowiedzi_poprawnych=0
liczba_odpowiedzi_zlych=0
for numer_pytania in baza_zagadek.keys():
    print('Odpowiedz na nastepujace pytanie:' + ' ' + numer_pytania)
    odpowiedz_uzytkownika=str.lower(input())
    if odpowiedz_uzytkownika == baza_zagadek[numer_pytania]:
        print('zgadles')
        liczba_odpowiedzi_poprawnych=liczba_odpowiedzi_poprawnych + 1
        liczba_udzielonych_odpowiedzi=liczba_udzielonych_odpowiedzi+1
    else:
        print('nie zgadles, przechodzimy do nastepnego pytania')
        liczba_udzielonych_odpowiedzi=liczba_udzielonych_odpowiedzi+1
print('Liczba udzielonych odpowiedzi:' + ' ' +str(liczba_udzielonych_odpowiedzi))
print('Liczba poprawnych odpowiedzi:' + ' ' +str(liczba_odpowiedzi_poprawnych))
print('Liczba zlych odpowiedzi:' + ' ' + str(liczba_udzielonych_odpowiedzi-liczba_odpowiedzi_poprawnych))
print('Procent_prawidlowych_odpowiedzi:' + ' ' + str(liczba_odpowiedzi_poprawnych/liczba_udzielonych_odpowiedzi*100) + '%')
