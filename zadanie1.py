bok_a = float(input('Podaj dlugosc boku a'))
bok_b = float(input('Podaj dlugosc boku b'))
if bok_a==bok_b:
    print('Ta figura to kwadrat')
else:
    print('Ta figura to prostokat')
pole = bok_a*bok_b
print('Pole Twojej figury jest rowne' + ' ' + str(pole))