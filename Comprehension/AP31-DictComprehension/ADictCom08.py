# EJERCICIO 8

lista = ("Alvaro", "Pablo", "Juanjo")

dic1 = {"Alvaro":1, "Pedro":2, "Antonio":3}

dic1claves = list(dic1.keys())
dic1valores = list(dic1.values())

dic2 = {elementoc:elementov for elementoc, elementov, elementoL in zip(dic1claves, dic1valores, lista) if elementoc != elementoL}

print(dic2)