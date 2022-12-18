#!/usr/bin/env python
""" Menu """
import random
import tkinter as tk
from PIL import Image, ImageTk
import os 
import lab2
import lab3 
import lab4 
import lab5 
import lab6 
import lab7 
import lab8 
import sys



class Menu(tk.Frame):
    def __init__(self,parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # color 239D60
        self.parent = parent
        self.parent.geometry("1000x670+150+10")
        self.parent.title("Home")
        self.parent.resizable(width = 0, height = 0)
        self.parent.iconbitmap(rf"imagenes/pc.ico")

        self.color = random.randint(30,60)
        self.color1 = random.randint(60, 99)
        self.color2 = random.randint(30,60)

        self.color3 = random.randint(30,60)
        self.color4 = random.randint(60,99)
        self.color5 = random.randint(30,60)

        # frame - barra superior 
        self.barraSuperior = tk.LabelFrame(self.parent, relief = tk.SUNKEN, 
            padx = 5, pady = 3, text = "Hecho por ABC-Software", fg = "#000000", 
            font = ("Bauhaus 93", 13))

        self.titulo = tk.Label(self.barraSuperior, text = "            Mi gran enciclopedia Visual", 
            bg = "#D6CDA4", font = ("Bauhaus 93", 35)).pack()

        self.barraSuperior.config(width = "1000", height = "80",bg = "#D6CDA4", bd = 9)
        self.barraSuperior.pack(fill = "x",expand = 0) # fin de declaracion de LabelFrame


        # ---- frame principal ----
        self.frame = tk.Frame(self.parent)
        self.frame.config(width = "1000", height = "590", bg = "#000000")
        self.frame.pack(fill = "x", expand = 0)


        # ..... Canvas de imagenes .....
        self.can = tk.Canvas(self.frame,width=1000,height=590)
        self.can.pack()
        self.photo = Image.open(rf"imagenes/hojas.png")
        self.fondo = Image.open(rf"imagenes/fondo.jpg")

            # fondo de menu
        self.fondo = self.fondo.resize((1000,670), Image.Resampling.LANCZOS)
        self.fondo = ImageTk.PhotoImage(self.fondo) # menu
        self.can.create_image(500,250, image = self.fondo)

            # hojas 
        self.photo = self.photo.resize((1000,670), Image.Resampling.LANCZOS)
        self.photo=ImageTk.PhotoImage(self.photo) # hojas
        self.can.create_image(500,250, image = self.photo)
        


        # imagen enves de boton
        self. imagen = Image.open(rf"imagenes/imagen.png")
        self. imagen = self.imagen.resize((250, 60), Image.Resampling.LANCZOS)
        self. imagen = ImageTk.PhotoImage(self.imagen)
        tk.Label(self.barraSuperior, image = self.imagen).place(x = 3, y = 0)

        # resize imagenes
        def resizeImagen(nuevaImagen, ancho = 50, alto = 50): # funcion de resize imagenes 
            botonImagen = Image.open(rf"imagenes/{nuevaImagen}")
            botonImagen = botonImagen.resize((ancho, alto), Image.Resampling.LANCZOS)
            botonImagen = ImageTk.PhotoImage(botonImagen)
            tk.Label(root, image = botonImagen)
            return botonImagen

        # ---- botones ---- 

            # variables de botones
        xinicial = 30
        yinicial = 20

            # .... boton 1 ....
        def funcion1():
            lab2.pag2(self.parent)

        self.imagenBoton1 = resizeImagen("mundo.png")
        self.boton1 = tk.Button(self.frame, command = funcion1, image = self.imagenBoton1, 
            text = "Geografia", compound = tk.LEFT, font = ("Bauhaus 93", 21),
            bd = 9, bg = f"#{self.color}{self.color4}{self.color5}")
        self.boton1.place(x = 30, y = yinicial)

            # .... boton 2 ....
        def funcion2():
            lab3.pag3(self.parent)

        self. imagenBoton2 = resizeImagen("seres vivos.png")
        self. boton2 = tk.Button (self.frame, command = funcion2, image = self.imagenBoton2,
            bd = 9, bg = f"#{self.color3}{self.color4}{self.color2}", compound = tk.LEFT, font = ("Bauhaus 93",21),
            text = "Biologia")
        self.boton2.place(x = 30, y = yinicial + 100)

            # .... boton 3 ....
        def funcion3():
            lab4.pag4(self.parent)

        self.imagenBoton3 = resizeImagen("math.png", 80, 80)
        self.boton3 = tk.Button(self.frame, command = funcion3, image = self.imagenBoton3,
            bd = 9, bg = f"#{self.color}{self.color1}{self.color2}", compound = tk.LEFT, font = ("Bauhaus 93", 21),
            text = "Ciencia de \nla tecnologia")
        self.boton3.place(x = 30, y = yinicial + 200)

            # .... boton 4 ....
        def funcion4():
            lab5.pag5(self.parent)

        self.imagenBoton4 = resizeImagen("deportes.png", 60,60)
        self.boton4 = tk.Button(self.frame, command = funcion4 , image = self.imagenBoton4,
            bd = 9, bg = f"#{self.color}{self.color4}{self.color2}", compound = tk.LEFT, font = ("Bauhaus 93", 21),
            text = "deportes") 
        self.boton4.place(x = 30, y = yinicial + 325)

            # .... boton 5 .....
        def funcion5():
            lab6.pag6(self.parent)

        self.imagenBoton5 = resizeImagen("bandera.png")
        self.boton5 = tk.Button(self.frame, command = funcion5, image = self.imagenBoton5,
            bd = 9, bg = f"#{self.color}{self.color1}{self.color5}", compound = tk.RIGHT, font = ("Bauhaus 93", 21),
            text = "Historia del Peru")
        self.boton5.place(x = xinicial + 670, y = yinicial)


            # .... boton 6 ....
        def funcion6():
            lab7.pag7(self.parent)
        self.imagenBoton6 = resizeImagen("literatura.png")
        self.boton6 = tk.Button(self.frame, command = funcion6, image = self.imagenBoton6,
            bd = 9, bg = f"#{self.color}{self.color1}{self.color2}", compound = tk.RIGHT, font = ("Bauhaus 93", 21), 
            text = "Literatura")
        self.boton6.place(x = xinicial + 755, y = yinicial + 100)
            
            # .... boton 7 ....
        def funcion7():
            lab8.pag8(self.parent)
        self.imagenBoton7 = resizeImagen("juegos.png")
        self.boton7 = tk.Button(self.frame, command = funcion7, image = self.imagenBoton7,
            bd = 9, bg = f"#{self.color3}{self.color1}{self.color5}", compound = tk.RIGHT, font = ("Bauhaus 93", 21), 
            text = "Juegos")  
        self.boton7.place(x = xinicial + 790, y = yinicial + 200) 


    

def callback(evento):
    sys.exit()



if __name__ == '__main__':
    root = tk.Tk()
    Menu(root).pack(side = "top", fill = "both", expand = True)
    root.bind("<Return>", callback)
    root.mainloop()
