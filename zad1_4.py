# 1 do 49 bez powtorzen
import random

tmp = []
for x in range(0, 6):

    pom = random.randint(1, 49)
    while  pom in tmp: pom = random.randint(1, 49);
    tmp.append(pom)

print tmp
