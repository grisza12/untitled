'''
Grzegorz Mucha
Zadania
'''
#zadanie1
a = [1,2,3,4,5,6,7,8,9]
print a.index(5)

# nwd i nww
def nwd(x,y):
    if x==y:
        return x
    if x>y:
        t=x
        x=y
        y=t
    while x != 0:
        t = y % x
        y=x
        x=t
    return y
def nww(a,b):
    return abs(a * b / nwd(a, b))

print nww(2,7)

l = range(2,101)
print l


def usunZakres(liczba,granicaGorna,lista):

    m = range(0,granicaGorna,liczba)

    for i in m:
        lista.remove(m[i])

usunZakres(3,101,l)
print l


# class WyswietlanieLiczbPierwszych:
#     def czyJestLiczbaPierwsza(self):



# sito eratostenesa wyszukujacy liczby pierwsze - stosowac klasy
