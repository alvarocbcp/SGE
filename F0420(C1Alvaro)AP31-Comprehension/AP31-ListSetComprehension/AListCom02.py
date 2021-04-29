# EJERCICIO 2

inicio = 0

paso = 1

final = 15

lista = [inicio, inicio+paso]

[lista.append(lista[rango-1]+lista[rango-2]) for rango in range(inicio, final, paso) if rango>1]

print(lista)