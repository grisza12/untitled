import random
# liczba losowana z zakresu krotry podal uzytkownik - za malo i za duzo ilosc prob 3 proby - zmiana skryptu

print 'Masz trzy proby zgadniecia wylosowanej liczby z zakresu'
x = input('Lewy zakres przedzialu')
y = input('Prawy zakres przedzialu')

win = False;
wylosowana = random.randint(x, y)

while not win:
    print 'Wylosowano liczbe z podanego zakresu'
    for x in range(0,3):
        m = input('Podaj liczbe z zakresu' )
        if m == wylosowana:
            win = True
            print 'Brawo udalo Ci sie!'
            break
    if  win == False:
        print 'Niestety nie udalo Ci sie'
    win = False
    print 'Jesli chcesz zakonczyc zgadywanie wcisnij 1.'
    t = input()


    if  t!=1 : wylosowana=random.randint(x,y)
    else: break