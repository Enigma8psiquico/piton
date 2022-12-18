#!/usr/bin/env python
import tkinter as tk
from PIL import Image, ImageTk

class Universo(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Geografia - Universo")
        self.geometry("1000x670+150+10")
        self.resizable(width = 0, height = 0)
        self.protocol("WM_DELETE_WINDOW", self.volver)
        self.ancho = 1000
        # self.iconbitmap("imagenes/pc.ico")

        # barra superior 
        self.barraSuperior = tk.LabelFrame(self, relief = tk.SUNKEN, padx = 5, pady = 3, 
            text = "Hecho por ABC-Software", fg = "#000000", font = ("Bauhaus 93", 13),
            bg = "#D6CDA4")
        self.barraSuperior.config(width = "1000", height = "80" , bd = 9)
        self.barraSuperior.pack(fill = "x", expand = 0)

        self.titulo = tk.Label(self.barraSuperior, text = "            Mi gran enciclopedia Visual", 
            bg = "#D6CDA4", font = ("Bauhaus 93", 35)).pack()


        # ---- frame principal -----
            
            # frame de subtemas 
        self.barraSubtemas = tk.LabelFrame(self, relief = tk.SUNKEN, padx = 0, pady = 3,
            text = "Subtemas", fg = "#bbb", font = ("Bauhaus 93", 13))

        self.barraSubtemas.config(width = 200, height = "80", bg = "#101010", bd = 9)
        self.barraSubtemas.pack(fill = "y", expand = 0, side = tk.LEFT)
            # frame de tema
        self.barraTitulo = tk.LabelFrame(self, relief = tk.SUNKEN, padx = 0, pady = 3,
            text = "Tema", fg = "#bbb", bg = "#101010",font = ("Bauhaus 93", 13))
        self.barraTitulo.config(width = 110, height = "80", bd = 9)
        self.barraTitulo.pack(side = tk.LEFT, fill = "both", expand = 0)



        # boton de volver 
            # llamada de imagen de boton
        self.imagenBoton = Image.open(rf"imagenes/botonHome1.png")
        self.imagenBoton = self.imagenBoton.resize((40,40), Image.Resampling.LANCZOS)
        self.imagenBoton = ImageTk.PhotoImage(self.imagenBoton)
        self.labelBoton = tk.Label(image = self.imagenBoton)
            # declaracion de boton
        tk.Button(self.barraSuperior, text="Inicio", command=self.volver, compound = tk.LEFT, 
            image = self.imagenBoton, font = ("Bauhaus 93", 21, "bold")).place(x = 10, y =0)
        self.parent.withdraw()

        
        # .... contenedor de temas ...        

        titulo = " Geografia / El Universo"

        introduccion = """
Es la gran escala de espacio conformado por masivas agrupaciones de materia que forman la estructura de estrellas.
        """

        texto2 = """
Las Estrellas que conforman el universo tienen diferentes tamaños, estas son parecidas al Sol y la luminoccidad de algunas es solo un diezmilesimo de la que tiene el Sol, es decir

          Luminosidad del sol
        -----------------------        
                1000
        """

        texto3 = """
Las estrellas denominadas \"gigantes\" tienen 40 veces mas masa que la del Sol con un diametro hasta 2 mil veces mayor.
A diferencia de las estrellas denominadaas \"enanas\" con menos maasa que la que la del Sol con un diametro 100 veces menor"
        """
        
        texto4 = """
Una caracteristica de nuestro universo es que este no tiene limites, carece(no tiene), de un inicio y un final.

En conclusion nuestro universo es mucho mas grande de lo que podemos imaginar.
        """


        # scroollbar 
            # declaracion de canvas
        self.canvas = tk.Canvas(self.barraTitulo, relief = tk.SUNKEN, width = 760 )        
        self.yScrooll = tk.Scrollbar(self,  orient = "vertical", command = self.canvas.yview)
        self.yScrooll.pack(side = tk.RIGHT, fill = "y")

            # contenido de el tema 
        # wraplength = 100 controla el ancho del laabel
            # titulo
        self.labelTitulo = tk.Label(self.canvas, text = titulo, bg = "red", font = ("Cascadia Code", 21), anchor = "n")
            # introduccion 
        self.labelintroduccion = tk.Label(self.canvas, text = introduccion, justify = tk.LEFT, font = ("Cascadia Code", 12, "bold"), wraplength = 460)
            # texto 2
        self.labeltexto2 = tk.Label(self.canvas, text = texto2, font = ("Cascadia Code", 12, "bold"), wraplength = 450, justify = tk.LEFT) 
            # texto 3
        self.labeltexto3 = tk.Label(self.canvas, text = texto3, font = ("Cascadia Code", 12, "bold"), wraplength = 450, justify = tk.LEFT)
            # texto 4 
        self.labeltexto4 = tk.Label(self.canvas, text = texto4, font = ("Cascadia Code", 12, "bold"), wraplength = 450, justify = tk.LEFT)

        # llamado de labeles 
        self.canvas.create_window(0,0, window = self.labelTitulo)
        self.canvas.create_window(10,70, window = self.labelintroduccion)
        self.canvas.create_window(340, 300, window = self.labeltexto2)
        self.canvas.create_window(10,488, window = self.labeltexto3)
        self.canvas.create_window(340, 700, window = self.labeltexto4)




            # declaracion de el scroollbar 
        self.canvas.config(yscrollcommand = self.yScrooll.set,
            scrollregion = self.canvas.bbox("all"))
        self.canvas.pack(fill= "both", expand = 1)
        #.... ....

        # resize imagenes de botones
        def resizeImagenes(nuevaImagen):
            botonImagen = Image.open(rf"imagenes/{nuevaImagen}")
            botonImagen = botonImagen.resize((50,50), Image.Resampling.LANCZOS)
            botonImagen = ImageTk.PhotoImage(botonImagen)
            tk.Label(self, image = botonImagen)
            return botonImagen


    def volver(self):
        self.parent.deiconify()
        self.destroy()
