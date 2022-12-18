from PIL import Image
nombre = "download.jpg"

imagen = Image.open(rf"{nombre}")
imagen = imagen.convert("RGB")
imagen.save(rf"imagenes/sisSolar.jpg", quality = 100)	

