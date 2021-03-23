#-*- coding:utf-8 *-*

# Importo el modulo os, para ejecutar el comando DOS cls. EJECUTAR desde la consola cmd de windows

import os

# help("keyword") #Para llenar la ventana de la consola cmd
# Esperar pulsacion
print("-------------------------------------------")
input ("Pulsa cualquier tecla para limpiar pantalla")

os.system("cls") # Siempre si se ejecuta desde cmd de windows

#Esperar pulsacion para salir
input ("Pulsa cualquier tecla para terminar")