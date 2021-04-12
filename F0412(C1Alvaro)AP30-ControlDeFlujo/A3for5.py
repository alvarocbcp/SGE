# EJERCICIO 5

def multiplosDe(fin):
    numero = int(input("Introduce el numero para calcular sus multiplos."))
    for x in range(0, 11, 1):
        print(f" {numero} x {x} = {numero*x}")

num = 9

multiplosDe(num)