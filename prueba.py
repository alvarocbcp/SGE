# Esto es un comentario

#-*- coding:utf-8 *-*

#Importando los modilos: platform y math
import platform
import math as m

#Utilización---------------------------------------------
print ("Tiene como documentacion " + platform.__doc__)
print ("El sistemea operativo es " + platform.system())
print ("El nombre del modulo es: " + platform.__name__)
print ("")
print ("Las propiedades y métodos de módulo: " + platform.__name__)
print ("-------------------------------------------------------------")
pro_met = dir(platform)
print (pro_met) #Listar las propiedades y métodos del módulo
print ("-------------------------------------------------------------")
#print ("pro_met es una variable del tipo: ", type(pro_met))
print ("")
#Esperar pulsacion para continuar
input ("Pulsa cualquier tecla para continuar")
print("")
print("El contenido de pi es: " + m.pi)
print ("Las propiedades y metodos del modulo: " + m.__name__)
print ("-------------------------------------------------------------")
pro_met = dir(m)
print (pro_met) #Listar las propiedades y metodos del modulo

#Esperar pulsacion para salir
input ("Pulsa cualquier tecla para terminar")