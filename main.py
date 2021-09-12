from math import *
print('Enter odds')
a = int(input())
b = int(input())
c = int(input())
D = (b * b) - (4 * a * c)

if D > 0:
    print((-b + sqrt(D)) / (2 * a))
    print((-b - sqrt(D)) / (2 * a))
elif D == 0:
    print((-b) / (2 * a))
else:
    print('No solutions')
