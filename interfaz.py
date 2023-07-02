from tkinter import *
from PIL import Image, ImageTk
import pygame


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



def juego():
  #ventana1= Tk()
  botonStart.place_forget()
  botonmusica.place_forget()

  botoncirculo.place(x=120,y=450)
  botontriangulo.place(x=420,y=450)
  botoncuadrado.place(x=720,y=450)

  def menu():
   ventana
   botvolvermenu.place_forget()
   botoncirculo.place_forget()
   botontriangulo.place_forget()
   botoncuadrado.place_forget()
   botonStart = Button(ventana,text="JUGAR",width=20, height=4,command=juego)
   botonStart.place(x=450,y=250)

   botonmusica = Button(ventana,text="MÚSICA",width=20, height=4,command=menumusica)
   botonmusica.place(x=450,y=350) 

   
   ventana.geometry("1030x600") #definiendo el tamaño de la ventana
   imagen = Image.open('fond0.png')
   imagen = imagen.resize((1030,600), Image.ANTIALIAS)
   img = ImageTk.PhotoImage(imagen)
   fondo = Label(ventana, image=img)
   fondo.pack()
   
  botvolvermenu= Button(ventana,text="MENU",width=10, height=2,command=menuVolver)
  botvolvermenu.place(x=5,y=2)



  #ventana1.geometry("1030x600") #definiendo el tamaño de la ventana
  #ventana1.configure(bg="red")
  #ventana1.mainloop()


def menumusica():
  #ventana

  if botonmusica.winfo_ismapped():
    apagar()
    botonmusica.configure(text="MUSICA: OFF")

  else:
    encender()
    botonmusica.configure(text="MUSICA: ON")
  
def apagar():

   pygame.mixer.init()
   pygame.mixer.music.load("Raiders March.mp3")
   pygame.mixer.music.pause()

 
  #botonoff= Button(ventana,text="OFF",width=20, height=4,command=apagar)
  #botonoff.place(x=450,y=250)

def encender():
   #pygame.mixer.music.play()
   pygame.mixer.init()
   pygame.mixer.music.load("Raiders March.mp3")
   pygame.mixer.music.play(-1)


  #botonon= Button(ventana,text="ON",width=20, height=4,command=encender)
  #botonon.place(x=450,y=350)


  #botvolvermenu= Button(ventana,text="MENU",width=10, height=2,command=menuVolver)
  #botvolvermenu.place(x=5,y=2)



  #ventana.geometry("1030x600") #definiendo el tamaño de la ventana
  #imagen = Image.open('fond0.png')
  #imagen = imagen.resize((1030,600), Image.ANTIALIAS)
  #img = ImageTk.PhotoImage(imagen)
  #fondo = Label(ventana, image=img)
  #fondo.pack()
  #ventana.mainloop()

def menuVolver():
   ventana
   #botvolvermenu.place_forget()
   botoncirculo.place_forget()
   botoncuadrado.place_forget()
   botontriangulo.place_forget()
   botonStart = Button(ventana,text="JUGAR",width=20, height=4,command=juego)
   botonStart.place(x=450,y=250)

   botonmusica = Button(ventana,text="MÚSICA",width=20, height=4,command=menumusica)
   botonmusica.place(x=450,y=350) 

   ventana.geometry("1030x600") #definiendo el tamaño de la ventana
   imagen = Image.open('fond0.png')
   imagen = imagen.resize((1030,600), Image.ANTIALIAS)
   img = ImageTk.PhotoImage(imagen)
   fondo = Label(ventana, image=img)
   fondo.pack()

botonStart = Button(ventana,text="JUGAR",width=20, height=4,command=juego)
botonStart.place(x=450,y=250)

botonmusica = Button(ventana,text="MÚSICA: ON",width=20, height=4,command=menumusica)
botonmusica.place(x=450,y=350)


ventana.geometry("1030x600") #definiendo el tamaño de la ventana
ventana.title("GEOMETRY SAFARI") #Nombre de la ventana

#botones juego
def circulo():

   circulo=1
   print(circulo)

def triangulo():

   triangulo=0
   print(triangulo)

def cuadrado():

   cuadrado=2
   print(cuadrado)

botoncirculo= Button(ventana,text="CIRCULO",width=30, height=4,command=circulo)
botontriangulo= Button(ventana,text="TRIANGULO",width=30, height=4,command=triangulo)
botoncuadrado= Button(ventana,text="CUADRADO",width=30, height=4,command=cuadrado)
#boton menu





ventana.mainloop()