from tkinter import *
from PIL import Image, ImageTk
import pygame

def mensaje():
    print("Hola mundo")

ventana = Tk() #creando el objeto ventana a partir del contructor

# Inicializar pygame
pygame.mixer.init()

# Cargar la música de fondo
pygame.mixer.music.load("Raiders March.mp3")

# Reproducir la música en bucle
pygame.mixer.music.play(-1)

#imagen =  PhotoImage(file = r'C:\Users\GERSONSANCHEZ\OneDrive - UNIVERSIDAD INDUSTRIAL DE SANTANDER\Documents\2023-1\TRATAMIENTO DE SEñALES DISCRETAS O1\proyecto-discretas\fondR.png')
imagen = Image.open('fond0.png')
imagen = imagen.resize((1030,600), Image.ANTIALIAS)


img = ImageTk.PhotoImage(imagen)
fondo = Label(ventana, image=img)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
fondo.pack()

botonStart = Button(ventana,text="START",width=20, height=4)
botonStart.place(x=425,y=500)

#botonStart.pack()


ventana.geometry("1030x600") #definiendo el tamaño de la ventana
ventana.title("Home") #Nombre de la ventana


ventana.mainloop()