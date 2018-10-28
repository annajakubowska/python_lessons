lista_liczb_pierwszych=[]

print('Podaj dowolna liczbe')
liczba_uzytkownika = int(input())

wszystkie_liczby = range(1,liczba_uzytkownika+1)
for liczba in wszystkie_liczby:
    LiczbaPierwsza = True
    lista_dzielnikow = range(1,liczba+1)
    for dzielnik in lista_dzielnikow:
        if (liczba % dzielnik == 0) and (liczba != dzielnik) and (dzielnik != 1):
            LiczbaPierwsza = False
    if LiczbaPierwsza:
        lista_liczb_pierwszych.append(liczba)

print ('Lista liczb pierwszych')
print (lista_liczb_pierwszych)