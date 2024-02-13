from customtkinter import *
from PIL import Image
pfuentes = ['arial','verdana','comic sans']

v = CTk()
v.geometry("700x800")
v.title("Watermarks")
#v.resizable(0,0)

frameCargar = CTkFrame(v)
frameCargar.grid(row=0,column=0,padx=10)

CTkLabel(frameCargar,text="Seleccione una Imagen").grid(row=0,column=0,padx=20,pady=10)
bCargar = CTkButton(frameCargar,text="Subir archivo...")
bCargar.grid(row=0,column=1)


frameFuente = CTkFrame(v)
frameFuente.grid(row=0,column=1)
CTkLabel(frameFuente,text="Seleccione Una Fuente").grid(row=0,column=3,padx=30,pady=10)
comboFuentes = CTkComboBox(frameFuente,values=pfuentes)
comboFuentes.grid(row=0,column=4,padx=20)


frameRadio = CTkFrame(v)
frameRadio.grid(row=1,column=0)
rSelect = IntVar(value=0)
CTkRadioButton(frameRadio,text="Marca de Agua", variable=rSelect, value=1).grid(row=0,column=0,padx=10)
CTkRadioButton(frameRadio,text="Antirrobo", variable=rSelect, value=2).grid(row=0,column=1,padx=0)

frameFuenteSize = CTkFrame(v)
frameFuenteSize.grid(row=1,column=1,pady=10)
CTkLabel(frameFuenteSize,text="Tamaño de la Fuente").grid(row=0,column=0,pady=10,padx=20)
fSize = CTkEntry(frameFuenteSize)
fSize.grid(row=0,column=1)


frameImagen = CTkFrame(v)
frameImagen.grid(row=2,column=0,columnspan=2)


preview = CTkImage(light_image = Image.open('wmarks/original.png'),size=(300,500))
lPreview = CTkLabel(frameImagen,text="",image = preview).grid()


frameSlider = CTkFrame(v)
frameSlider.grid(row=3,column=0,pady=20,columnspan=2)
CTkLabel(frameSlider,text="Opacidad").grid(row=0,column=0)
sliderOpacidad = CTkSlider(frameSlider,from_=0, to=100)
sliderOpacidad.grid(row=0,column=1)




frameBotones = CTkFrame(v)
frameBotones.grid(row=5,column=0,pady=10,columnspan=2,sticky="ew")
frameBotones.columnconfigure(0,weight=1)

bVistaPrev = CTkButton(frameBotones,text="Vista Previa")
bVistaPrev.grid(row=0,column=0,pady=10,sticky="ew")


bGuardar = CTkButton(frameBotones,text="Guardar")
bGuardar.grid(row=1,column=0,pady=10,sticky="ew")


v.mainloop()