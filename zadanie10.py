lista_liczb_podzielnych_przez_7=[]
for i in range(1,100):
    reszta=i%7
    if reszta==0:
        lista_liczb_podzielnych_przez_7=lista_liczb_podzielnych_przez_7+[i]
print(lista_liczb_podzielnych_przez_7)