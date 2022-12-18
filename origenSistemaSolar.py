#!/usr/bin/env python
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk

class OrigenSisSolar(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Geografia - Universo")
        self.geometry("1000x670+150+10")
        self.resizable(width = 0, height = 0)
        self.protocol("WM_DELETE_WINDOW", self.volver)
        self.ancho = 1000

        fuente = "Cascadia Code"
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

        titulo = " El origen del sistema Planetario"

        introduccion = """
El sistema solar se conforma del Sol como eje que forma parte de la Vía Láctea. Se ubica de los brazos espirales el cual este es conocido como el Brazo de Orión.
        """

        texto2 = """
El origen del sistema Solar
        """
        # imagen 

        texto3 = """
La hipótesis mas concretaa y fiable con la que sostienen los cientificos es la \"Hipotesis Nebular\".
        """
        
        texto4 = """
Sostiene que hace aproximadamente 4700 millones de años, el sistema solar, se formó a partir de una gran nube giratoria de gas y polvo conocida como nebulosa.
Los procesos de contraccion ocurridos por la fuerza de atraccion gravitatoria y otros procesos que originaron el Sol. Luego el enorme calor producido unió mas partículas, hasta que se formaron los planetas.
        """
        texto5 = """
La teoria Nebular consiste en cinco momentos:
1. Una enorme nube de gas y polvo cosmico comienza a contraerse por la gravedad.

        """
        texto6 = """



















2. A medidaa de que la nube se contrae aumenta su velocidad de rotación y la nube se hace plana.

        """

        texto7 = """



















3. La maasa acumulada en el centro genera la fusion de hidrógeno y forma el protosol(el antecesor del sol). La nube se fragmenta en remolinos formando centros de gravedad dando origen a los protoplanetas.
        """
        texto8 = """



















4. Los protoplanetas crecen al agregar mas materia hasta que los vientos solares dispersen la nube.

        """
        texto9 = """



















5. Finalmente los planetas son consolidados junto con sus satelites.
























Actualmente la hipótesis nebular es la mas aceptable.

        """

        # The galaxy NGC 1961 unfurls its gorgeous spiral arms in this newly released image from NASA’s Hubble Space Telescope.

        # scroollbar 
            # declaracion de canvas
        self.canvas = tk.Canvas(self.barraTitulo, relief = tk.SUNKEN, width = 760 )        
        self.yScrooll = tk.Scrollbar(self,  orient = "vertical", command = self.canvas.yview)
        self.yScrooll.pack(side = tk.RIGHT, fill = "y")

            # contenido de el tema 
        # wraplength = 100 controla el ancho del laabel
            # titulo
        self.labelTitulo = tk.Label(self.canvas, text = titulo, bg = "red", font = (f"{fuente}", 21), anchor = "n")
            # introduccion 
        self.labelintroduccion = tk.Label(self.canvas, text = introduccion, justify = tk.LEFT, font = (f"{fuente}", 12, "bold"), wraplength = 460)
            # texto 2
        self.labeltexto2 = tk.Label(self.canvas, text = texto2, font = (f"{fuente}", 12, "bold"), wraplength = 450, justify = tk.LEFT) 
            # texto 3
        self.labeltexto3 = tk.Label(self.canvas, text = texto3, font = (f"{fuente}", 12, "bold"), wraplength = 450, justify = tk.LEFT)
            # texto 4 
        self.labeltexto4 = tk.Label(self.canvas, text = texto4, font = (f"{fuente}", 12, "bold"), wraplength = 450, justify = tk.LEFT)
            # texto 5
        self.labeltexto5 = tk.Label(self.canvas, text = texto5, font = (f"{fuente}",12, "bold"), wraplength = 550, justify = tk.LEFT)
            # texto 6 
        self.labeltexto6 = tk.Label(self.canvas, text = texto6, font = (f"{fuente}",12, "bold"), wraplength = 550, justify = tk.LEFT)
            # texto 7 
        self.labeltexto7 = tk.Label(self.canvas, text = texto7, font = (f"{fuente}", 12, "bold"), wraplength = 550, justify = tk.LEFT)
            # texto 8
        self.labeltexto8 = tk.Label(self.canvas, text = texto8, font = (f"{fuente}", 12, "bold"), wraplength = 550, justify = tk.LEFT)
            # texto 9 
        self.labeltexto9 = tk.Label(self.canvas, text = texto9, font = (f"{fuente}", 12, "bold"), wraplength = 550, justify = tk.LEFT)



        # llamado de labeles 
        self.canvas.create_window(40,0, window = self.labelTitulo)
        self.canvas.create_window(10,100, window = self.labelintroduccion)
        self.canvas.create_window(-90, 300, window = self.labeltexto2)
        self.canvas.create_window(0,488, window = self.labeltexto3)
        self.canvas.create_window(0, 700, window = self.labeltexto4)
        self.canvas.create_window(0, 1000, window = self.labeltexto5)
        self.canvas.create_window(0,1600, window = self.labeltexto6)
        self.canvas.create_window(0,2300, window = self.labeltexto7)
        self.canvas.create_window(0,2900, window = self.labeltexto8)
        self.canvas.create_window(0,4000, window = self.labeltexto9)




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

        