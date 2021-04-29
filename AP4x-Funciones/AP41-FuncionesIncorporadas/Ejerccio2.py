# EJERCICIO 2

# C
print("*************C***************")

from itertools import combinations
valores = combinations('ACTG', 2)

for i in list(valores):
    print(i)

print("*************D***************")

# D

from itertools import product

valores = product('123', 'ABC')

for i in list(valores):
    print(i)

print("*************E***************")

# E

from itertools import groupby

nombres = ['Paco', 'Julia', 'Javier', 'Sara', 'Jose', 'Gala', 'Jorge', 'Ruben', 'Marta', 'Alex', 'Carmen']

valores = groupby(sorted(nombres, key=len), key=len)

for k,g in valores:
    print(f"Nombres con {k} letras")
    print(f"{list(g)}")

print("*************F***************")

# F

from itertools import permutations

lista = [1, 2, 3]

valores = permutations(lista)

for i in valores:
    print(i)
    
print("*************G***************")

def cadenaBase(longitud, base):
    