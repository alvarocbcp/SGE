# EJERCICIO 4

while(True):
    try:
        print("Convertir de decimal a: binario, octal y hexadecimal")
        print("****************************************************")
        auxiliar = input('Teclea el numero a convertir: ')
        if auxiliar == "*":
            print("Hasta otra!")
            break
        else:
            num = int(auxiliar)
            print(f'El numero {num}')
            print(f'En base 2 es: {bin(num).replace("0b", "")}')
            print(f'En base 8 es: {oct(num).replace("0o", "")}')
            print(f'En base 16 es: {hex(num).replace("0x", "").upper()}')
    except ValueError:
        print("Debes introducir un numero decimal")