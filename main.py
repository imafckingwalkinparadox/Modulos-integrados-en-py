#Modulos
from programas.sumas import suma
from programas.restas import resta
from vistas.menu import menu
from vistas.lineas import cargar_lineas
from datetime import datetime

#Modulos de python
import os

while (True):
    os.system("clear")
    print("Hora: ",datetime.now().strftime("%H:%H:%S"))

programa = True

while(programa):
    cargar_lineas(30)
    menu()
    respuesta = int(input("[?] "))

    if respuesta == 1:
        print("Sumar")
        suma()
    elif respuesta == 2:
        print("Restar")
        resta()
    elif respuesta == 0:
        print("Salir")

        programa = False

os.system("clear")