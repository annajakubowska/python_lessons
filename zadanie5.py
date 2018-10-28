import random
baza_losowania=list(range(-50,50))
los=random.sample(baza_losowania,6)
print('oto wylosowane liczby' + str(los))
los.sort()
print('oto posortowane liczby' + str(los))