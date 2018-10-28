my_matrix=[[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]
print('Oto tablica' + (str(my_matrix)))
for wiersz in [0,1,2]:
    print('Oto wiersz numer' + ' ' + str(wiersz) + ' ' + str(my_matrix[wiersz]))

my_matrix_tr = dict()
for wiersz in [0,1,2]: 
    for kolumna in [0,1,2,3]:
        if kolumna not in my_matrix_tr.keys():
            my_matrix_tr[kolumna] = []
        if kolumna in my_matrix_tr.keys():
            my_matrix_tr[kolumna].append(my_matrix[wiersz][kolumna])
            
print (my_matrix_tr)

for key in my_matrix_tr.keys():
   print('Oto kolumna numer' + ' ' + str(key) + ' ' + str(my_matrix_tr[key]))