# EJERCICIO 3

print("Convertir de decimal a: binario, octal y hexadecimal")
print("****************************************************")

num = int(input("Teclea el numero a convertir: "))

print(f"El numero {num}")
print(f"En base 2 es: {bin(num).replace('0b', '')}")
print(f"En base 8 es: {oct(num).replace('0o', '')}")
print(f"En base 16 es: {hex(num).replace('0x', '').upper()}")