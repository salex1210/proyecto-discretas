from tkinter import Tk,Label,Button

def mensaje():
    print("Hola mundo")

ventana = Tk() #creando el objeto ventana a partir del contructor
ventana.geometry("400x280") #definiendo el tamaño de la ventana
ventana.title("Home") #Nombre de la ventana
ventana.mainloop()