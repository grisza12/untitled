'''
Zbiory
'''

A=set([1,2,3])
print A

# dodawanie i usiwanie elementow zbioru
A.discard(3)
print A
A.add(8)
print A
# zbiory niezmienne
B=frozenset([3,5,6])
print B
# klucze w slownikach
# slownik = {B,9}
# print slownik
# elementy innych zbiorow
C=set([5,4,9])
C.add(B)
print C
#zbior pusty
D = set()
print D
#operacje na zbiorach

#liczba elementow
print len(A), len(B), len(C), len(D)

#sprawdzanie czy dany obiekt jest elementem zbioru
print 5 in A, 5 in B, 5 in C, 5 in D

#sprawdzanie czy dany obiekt nie jest elementem zbioru
print 8 not in A , 8 not in B, 8 not in C, 8 not in D
print '\n'

#sprawdzanie czy dany zbior jest podzbiorem innego zbioru
print set([1,2]) <= A
print set([3,4]) <= B
print set([5]) <= B
print set([1,3,5]) <= A

print A.issubset(B)
print '\n'

#sprawdzanie czy dany zbior jest nadzbiorem innego zbioru
print A>=set([1,2])
print A>=set([3,4])

print A.issubset(B)
print '\n'

#laczenie zbiorow
E=A|B
print E
print '\n'

#czesc wspolna dwoch zbiorow
F = A & B
print F
print '\n'

#roznica symetryczna
G = A^B
print G

'''
Klasy
'''

class Napis:
    txt = 'Pierwsza klasa'
    def wyswietl(self):
        return 'witaj'

#konkretyzacja klasy (wywolanie obiektu kklasy)

napis = Napis()

#odowalkenie sie do metody
print napis.wyswietl();

#odwolanie do atrybutu klasy
print napis.txt
#konkrety klasy
class Zespolona:
    def __init__(self, rzeczywista, urojona):
        self.r = rzeczywista
        self.i = urojona

x = Zespolona(5.0,-3.2)
print x.r, x.i

'''
metody operujace na napisach
'''

napis = 'Witaj w swiecie PYTHONA!'

print napis.capitalize()
print napis.center(64)
print napis.center(64,'*')
print napis.count('e')
print napis.find('Taj')
print napis.find('taj')
print napis.isdigit()
print '12'.isdigit()
print '12.4'.isdigit()
print ' '.join((['Python', 'jest', 'super']))
print napis.join(['***']*5)
print napis.lower()
print napis.replace('PYTHONA', 'programowania')
print napis.rfind('PYTHONA')
print 'Python jest super'.rfind('e')
print napis.rjust(32)
print napis.rjust(64)
print napis.rjust(64,'.')