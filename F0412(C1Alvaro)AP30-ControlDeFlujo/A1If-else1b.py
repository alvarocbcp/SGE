# EJERCICIO 1 b

dinero = int(input("¿Cuanto dinero has gastado?"))

if(dinero <= 100):
    print("Pago en efectivo")
elif(100 < dinero < 300):
    print("Pago con tarjeta de debito")
else:
    print("Pago con tarjeta de credito")

