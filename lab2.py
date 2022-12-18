#!/usr/bin/env python
import tkinter as tk
from PIL import Image, ImageTk
import geografia.sol as sol
import geografia.universo as universo
import geografia.galaxia as galaxia
import geografia.viaLactea as viaLactea
import sistemaSolar as sistemaSolar

class pag2(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Pagina 2")
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
        self.barraTitulo.config(width = self.ancho, height = "80", bd = 9)
        self.barraTitulo.pack(side = tk.LEFT, fill = "both", expand = 0)



        # boton de volver 
            # llamada de imagen de boton
        self.imagenBoton = Image.open(rf"imagenes/botonHome1.png")
        self.imagenBoton = self.imagenBoton.resize((40,40), Image.Resampling.LANCZOS)
        self.imagenBoton = ImageTk.PhotoImage(self.imagenBoton)
        self.labelBoton = tk.Label(image = self.imagenBoton)
            # declaracion de boton
        tk.Button(self.barraSuperior, text="Inicio", command=self.volver, compound = tk.LEFT, image = self.imagenBoton, font = ("Bauhaus 93", 21, "bold")).place(x = 10, y =0)
        self.parent.withdraw()

                # contenedor de temas 
        self.labelTema = tk.Label(self.barraTitulo, width = 110, height = 35)


        # resize imagenes de botones
        def resizeImagenes(nuevaImagen):
            botonImagen = Image.open(rf"imagenes/{nuevaImagen}")
            botonImagen = botonImagen.resize((50,50), Image.Resampling.LANCZOS)
            botonImagen = ImageTk.PhotoImage(botonImagen)
            tk.Label(self, image = botonImagen)
            return botonImagen

        # variables
        x = 10
        y = 10

        # funcion - sol
        def funcion1():
            sol.ElSol(self.parent)
            self.destroy()

        self.imagenBoton1 = resizeImagenes("../imagenes/sol.png")
        self.boton1 = tk.Button(self.labelTema, text = "El Sol", compound = tk.TOP ,
            command = funcion1,image = self.imagenBoton1, font = (21), bd = 4) 
        self.boton1.place(x = x, y = y)
        self.labelTema.pack()

        # funcion - universo 
        def funcion2():
            universo.Universo(self.parent)
            self.destroy()

        self.imagenBoton2 = resizeImagenes("../imagenes/universo.jpg")
        self.boton2 = tk.Button(self.labelTema, text = "Univero", compound = tk.TOP,
            command = funcion2, image = self.imagenBoton2,font = (21), bd = 4 )
        self.boton2.place(x = x* 8, y = y)
        self.labelTema.pack()

        # funcion - galaxia 
        def funcion3():
            galaxia.Galaxia(self.parent)
            self.destroy()

        self.imagenBoton3 = resizeImagenes("../imagenes/galaxia.jpg")
        self.boton3 = tk.Button(self.labelTema, text = "galaxias", compound = tk.TOP,
            command = funcion3, image = self.imagenBoton3, font = (21), bd = 4) 
        self.boton3.place(x = x * 15, y = y )
        self.labelTema.pack()

        def funcion4():
            viaLactea.ViaLactea(self.parent)
            self.destroy()

        self.imagenBoton4 = resizeImagenes("../imagenes/vialactea.jpg")
        self.boton4 = tk.Button(self.labelTema, text = "Via Lactea", compound = tk.TOP,
            command = funcion4, image = self.imagenBoton4, font = (21), bd = 4) 
        self.boton4.place(x = x * 25, y = y)
        self.labelTema.pack()


        def funcion5():
            sistemaSolar.SistemaSolar(self.parent)
            self.destroy()

        self.imagenBoton5 = resizeImagenes("../imagenes/sisSolar.jpg")
        self.boton5 = tk.Button(self.labelTema, text = "El Sistema\nSolar", compound = tk.TOP,
            command = funcion5, image = self.imagenBoton5, font = (21), bd = 4)
        self.boton5.place(x = x * 35, y = y)
        self.labelTema.pack()

    def volver(self):
        self.parent.deiconify()
        self.destroy()
