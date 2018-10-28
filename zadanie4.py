lista=[]
print('podaj poczatek przedzialu')
start=int(input())
print('podaj koniec przedzialu')
end=int(input())
for i in range(start,end):
    reszta=i%5
    if reszta==0:
        lista.append(i)
print('Liczby podzielne przez 5 to' + ' ' + str(lista))