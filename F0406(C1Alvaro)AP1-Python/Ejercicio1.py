# EJERCICIO 1
import os
import platform
from datetime import date, datetime, time
import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

nombre = input("¿Cuál es tu nombre?")

print("Hola " + nombre)

today = date.today()

tiempo = datetime.now()

hora = tiempo.hour

minutos = tiempo.minute

dia = today.strftime("%d")

mes = today.strftime("%B")

año = today.strftime("%Y")

diaSemana = today.strftime("%A")

print("Estamos a " + diaSemana.capitalize() + ", " + dia + " de " + mes.capitalize() + " del año: " +  año)
print("A las " + str(hora) + " horas y " + str(minutos) + " minutos")
print(str(platform.python_version()) + " es la version con la que estas trabajando")