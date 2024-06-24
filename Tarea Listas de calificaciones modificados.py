# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:28:56 2024

@author: Tisk
"""

from tkinter import Tk, Label, Entry


# El diccionario se coloca entre llaves
calificaciones = {"Francisco" : 8.4 , "Natalia" : 10 , 
                  "Gael" : 10, "Martin" : 6.9, "Antonio" : 9, "Pedro" : 5}



ventana = Tk() #Así se crea un ventana
ventana.title("Calificación")
ventana.eval("tk::PlaceWindow . center")

#Así se crean los elementos que se pondrán en la ventana
texto = Label(ventana,  font=("Helvetica 15 bold"), text = "¿Cuál es tu nombre?")
entrada = Entry(ventana, font=("Helvetica 15 bold"),background="#ff82e8", width=30)
score = Label(ventana,font=("Helvetica 15 bold"),text='')


# Pongo los elementos en la ventana
texto.pack(side = "left", padx=(20,5), pady=10)
entrada.pack(side="left", padx=(2,20), pady=10)
score.pack(side="bottom", padx= (0,10),pady=(100,5))

# Toma el dato de la entrada después de dar enter e imprime el nombre en consola
def on_entry(event):
    nombre = entrada.get()
    resultado = calificaciones[nombre]
    score.configure(text = "Tu calificación en matemáticas es: "+ str(resultado))
    print(nombre)

# Enlaza el recuadro de entrada con dar Return    
entrada.bind('<Return>', on_entry)

ventana.mainloop()