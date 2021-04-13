# EJERCICIO 7

dic1 = {"Pepe":111, "Juan":222, "Pedro":333}

dic1claves = list(dic1.keys())
dic1valores = list(dic1.values())

dic2 = {elementov:elementoc for elementov, elementoc in zip(dic1valores, dic1claves)}

print(dic2)