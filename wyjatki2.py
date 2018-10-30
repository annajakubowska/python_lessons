lista=[1,2,3,4,5,6]


last_element = int(len(lista)) - 1
print('wprowadz index listy')
index=int(input())

if index <= last_element:
    print (lista[index])
else:
    raise IndexError ('nie ma takiego indexu na liscie')   