import tkinter as tk


class ContenedorLabel(tk.Toplevel):
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
        self.labelTema.pack()

        # resize imagenes de botones
        def resizeImagenes(nuevaImagen):
            botonImagen = Image.open(rf"imagenes/{nuevaImagen}")
            botonImagen = botonImagen.resize((50,50), Image.Resampling.LANCZOS)
            botonImagen = ImageTk.PhotoImage(botonImagen)
            tk.Label(self, image = botonImagen)
            return botonImagen
