# EJERCICIO 1

lista = ['gato', 'perro', 'canario', 'peces']

def analizoLista(lista):
    longitud = len(lista)
    print(f"{longitud}")
    for x in range(0, longitud):
        print(f"{lista[x]} y su longitud es {len(lista[x])}")

analizoLista(lista)