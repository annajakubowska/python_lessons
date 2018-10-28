tupla=()
for i in range(10):
    print('podaj liczbe')
    liczba=input()
    tupla=tupla +tuple((liczba))
print(tupla)
print(min(tupla))
print(max(tupla))
