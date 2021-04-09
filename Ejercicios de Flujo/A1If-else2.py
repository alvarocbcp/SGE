# EJERCICIO 2

def esUnNumero(num):
    tipo = ""
    positivo = "positivo"
    if("0o" in num or "0O" in num):
        tipo = "octal"
        aux_octal = int(num, 8)
        if(aux_octal < 0):
            positivo = "negativo"
    elif("0x" in num or "0X" in num):
        tipo = "Hexadecimal"
        aux_hexa = int(num, 16)
        if(aux_hexa < 0):
            positivo = "negativo"
    elif("0b" in num or "0B" in num):
        tipo = "Binario"
        aux_binario = int(num, 2)
        if(aux_binario < 0):
            positivo = "negativo"
    print(f"El numero introducido es de tipo {tipo} y es {positivo}")

numero = input("Introduce un numero: ")

esUnNumero(numero)