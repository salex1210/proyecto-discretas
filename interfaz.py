from tkinter import *
from PIL import Image, ImageTk

def mensaje():
    print("Hola mundo")

ventana = Tk() #creando el objeto ventana a partir del contructor

#imagen =  PhotoImage(file = r'C:\Users\GERSONSANCHEZ\OneDrive - UNIVERSIDAD INDUSTRIAL DE SANTANDER\Documents\2023-1\TRATAMIENTO DE SEñALES DISCRETAS O1\proyecto-discretas\fondR.png')
imagen = Image.open('fond0.png')
imagen = imagen.resize((1030,600), Image.ANTIALIAS)

img = ImageTk.PhotoImage(imagen)
fondo = Label(ventana, image=img)
fondo.pack()
fondo.place(x=0, y=0, relwidth=1, relheight=1)
ventana.geometry("1030x600") #definiendo el tamaño de la ventana
ventana.title("Home") #Nombre de la ventana


ventana.mainloop()