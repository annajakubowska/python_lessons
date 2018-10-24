a=float(raw_input('podaj pierwsza liczbe '))
b=float(raw_input('podaj druga liczbe '))
znak=raw_input('podaj operacje ')

if znak=='+':
    print(a+b)
elif znak=='-':
    print(a-b)
elif znak=='*':
   print(a*b)
elif znak=='/' and b==0:
    print('dupa, nie wolno dzielic przez zero')
elif znak=='/' and b!=0:
    print(a/b)
else:
    print('kalkulator nie rozpoznal operacji')
