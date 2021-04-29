# PRACTICA CALCULADORA CON INTERFAZ GRÁFICA

from tkinter import *
from math import *

ventana = Tk()
# Le doy dimensiones a la ventana que voy a crear
window_width = 392
window_height = 600

# Con esto consigo el centro de mi pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Coloco la ventana en el centro de la pantalla
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

ventana.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
ventana.resizable(False, False)
ventana.attributes('-topmost', 1)


ventana.title("CALCULADORA")

# DIMENSIONES DE LOS BOTONES
ancho_boton = 11
alto_boton = 3

# DEFINIMOS LOS COLORES DE LOS BOTONES Y DEL FONDO
ventana.configure(background="SkyBlue4")
color_boton=("gray")

# FUNCION PARA DETECTAR EL CLICK DE TODOS LOS BOTONES
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

# FUNCION PARA EFECTUAR LA OPERACION
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

# FUNCION PARA LIMPIAR LA PANTALLA
def clear():
    global operador
    operador=("")
    input_text.set("0")

# CREAMOS VARIABLES PARA LA FUNCION "btnClick"
input_text=StringVar()
operador=""

Salida=Entry(ventana, font=('arial', 20, 'bold'), width=22, textvariable=input_text, bd=20, insertwidth=4, bg="powder blue", justify="right").place(x=10,y=60)

# CREAMOS LOS BOTONES
BotonParen1=Button(ventana, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("(")).place(x=17,y=180)
BotonParen2=Button(ventana, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(")")).place(x=107,y=180)
BotonPorcen=Button(ventana, text="%", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("%")).place(x=197,y=180)
BotonC=Button(ventana, text="C", bg=color_boton, width=ancho_boton, height=alto_boton, command=clear).place(x=287,y=180)

BotonLn=Button(ventana, text="ln", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("log(")).place(x=17,y=240)
BotonExp=Button(ventana, text="EXP", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("**")).place(x=107,y=240)
BotonSqrt=Button(ventana, text="√", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("sqrt(")).place(x=197,y=240)
BotonSuma=Button(ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("+")).place(x=287,y=240)

Boton7=Button(ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(7)).place(x=17,y=300)
Boton8=Button(ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(8)).place(x=107,y=300)
Boton9=Button(ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(9)).place(x=197,y=300)
BotonResta=Button(ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("-")).place(x=287,y=300)

Boton4=Button(ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(4)).place(x=17,y=360)
Boton5=Button(ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(5)).place(x=107,y=360)
Boton6=Button(ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(6)).place(x=197,y=360)
BotonMulti=Button(ventana, text="x", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("*")).place(x=287,y=360)

Boton1=Button(ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(1)).place(x=17,y=420)
Boton2=Button(ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(2)).place(x=107,y=420)
Boton3=Button(ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(3)).place(x=197,y=420)
BotonDivi=Button(ventana, text="÷", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("/")).place(x=287,y=420)

BotonP=Button(ventana, text="π", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik("pi")).place(x=17,y=480)
Boton0=Button(ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(0)).place(x=107,y=480)
BotonPunto=Button(ventana, text=".", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClik(".")).place(x=197,y=480)
BotonResul=Button(ventana, text="=", bg=color_boton, width=ancho_boton, height=alto_boton, command=resultado).place(x=287,y=480)

clear()


ventana.mainloop()

