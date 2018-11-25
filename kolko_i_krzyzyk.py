import random
from random import choice

def plansza(pole):
    print('  7|  8| 9')
    print(' ' + pole[7] + ' | ' + pole[8] + ' | ' + pole[9])
    print('   |   |')
    print('-----------')
    print('  4|  5| 6')
    print(' ' + pole[4] + ' | ' + pole[5] + ' | ' + pole[6])
    print('   |   |')
    print('-----------')
    print('  1|  2| 3')
    print(' ' + pole[1] + ' | ' + pole[2] + ' | ' + pole[3])
    print('   |   |')

def przydzial_symboli():
    symbol = ""
    while not (symbol == 'X' or symbol == 'O'):
        print('Wybierasz O czy X?')
        symbol = input().upper()
    if symbol == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def kto_zaczyna():
    if random.randint(0,1) == 0:
        return 'Zaczyna komputer'
    else:
        return 'Zaczynasz Ty'


def sprawdz_wolne_pola(numer_pola):
    wolne_pola = []
    for i in [1,2,3,4,5,6,7,8,9]:
        if numer_pola[i] == '':
            wolne_pola.append(str(i))
    return wolne_pola

def ruch_gracza(numer_pola):
    wybrane_pole =''
    while wybrane_pole not in sprawdz_wolne_pola(numer_pola):
        print("Wolne sa pola "+" ".join(sprawdz_wolne_pola(numer_pola)))
        print('Ktore pole wybierasz?')
        wybrane_pole = input()
        try:
            wybrane_pole = int(wybrane_pole)
        except:
            continue
        return wybrane_pole

def zrob_ruch(numer_pola,symbol,wybrane_pole):
    wybrane_pole = int(wybrane_pole)
    numer_pola[wybrane_pole]=symbol

def ruch_komputera(numer_pola):
    wybrane_pole = random.choice(sprawdz_wolne_pola(numer_pola))
    return wybrane_pole

def wygrany(numer_pola, symbol):
   
    return (
        (numer_pola[7] == symbol and numer_pola[8] == symbol and numer_pola[9] == symbol) or
        (numer_pola[4] == symbol and numer_pola[5] == symbol and numer_pola[6] == symbol) or
        (numer_pola[1] == symbol and numer_pola[2] == symbol and numer_pola[3] == symbol) or
        (numer_pola[7] == symbol and numer_pola[4] == symbol and numer_pola[1] == symbol) or
        (numer_pola[8] == symbol and numer_pola[5] == symbol and numer_pola[2] == symbol) or
        (numer_pola[9] == symbol and numer_pola[6] == symbol and numer_pola[3] == symbol) or
        (numer_pola[7] == symbol and numer_pola[5] == symbol and numer_pola[3] == symbol) or
        (numer_pola[9] == symbol and numer_pola[5] == symbol and numer_pola[1] == symbol)
        )

def plansza_zapelniona(numer_pola):
    if len(sprawdz_wolne_pola(numer_pola)) == 0:
        return True
    else:
        return False

def zagraj_jeszcze_raz():
    print('Czy chcesz zagrac jeszcze raz? (yes or no)')
    return input().lower().startswith('y')


print('Gramy w kolko i krzyzyk')
while True:
    plansza_gry = ['pusta','','','','','','','','','']
    gracz, komputer = przydzial_symboli()
    kolej = kto_zaczyna()
    kolej = 'gracz'
    print(kolej + ' zaczyna pierwszy.')
    trwa_gra = True
    while trwa_gra:
        if kolej == 'gracz':
            plansza(plansza_gry)
            wybrane_pole = ruch_gracza(plansza_gry)
            zrob_ruch(plansza_gry,gracz,wybrane_pole)

            if wygrany(plansza_gry,gracz):
                plansza(plansza_gry)
                print("Wygrales")
                trwa_gra = False
            elif plansza_zapelniona(plansza_gry):
                plansza(plansza_gry)
                print('Remis')
                break
            else:
                kolej = 'komputer'
        else:
            wybrane_pole = ruch_komputera(plansza_gry)
            zrob_ruch(plansza_gry, komputer, wybrane_pole)
            if wygrany(plansza_gry,komputer):
                plansza(plansza_gry)
                print("Wygral komputer")
                trwa_gra = False
            elif plansza_zapelniona(plansza_gry):
                plansza(plansza_gry)
                print('remis, nikt nie wygral')
                break
            else:
                kolej = 'gracz'
    if not zagraj_jeszcze_raz():
         break
