# EJERCICIO 9

diccionario = {"Juan":111, "Antonio":222, "Pedro":333}
tupla = ("Luis", 5, "sol", "luna")

listaDic1 = list(diccionario.keys())
listaDic2 = list(diccionario.values())

print("     Recorrido por zip(diccionario, tupla)")

for tupla, listaDic1, listaDic2 in zip(tupla, listaDic1, listaDic2):
    print(f"    De la tupla es: {tupla} y del Diccionario es: {listaDic1} con valor {listaDic2}")