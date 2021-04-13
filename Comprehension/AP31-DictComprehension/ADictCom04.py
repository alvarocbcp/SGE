# EJERCICIO 4

tupla = (1, 2, 3, 4, 5, 6)
lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

dic = {tupla:lista for tupla,lista in zip(tupla, lista)}

print(dic)