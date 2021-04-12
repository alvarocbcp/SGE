# EJERCICIO 1 c

pago = int(input("¿Cuanto tienes que pagar?"))

if(pago > 100):
    print(f"Tu pago es de {pago - (pago*10/100)}")