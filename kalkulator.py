a=float(input('podaj pierwsza liczbe '))
b=float(input('podaj druga liczbe '))
znak=input('podaj operacje ')

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
