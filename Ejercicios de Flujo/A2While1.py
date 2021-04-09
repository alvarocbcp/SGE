# EJERCICIO 1

num = 1

while (num == 1):
    si_teclean = input("Teclee algun valor distinto a enter: ")
    print ("valor booleano ", bool(si_teclean))
    if si_teclean:
        print("Has pulsado una tecla")
        contador = 2
    else:
        print ("Por favor tecleen")
