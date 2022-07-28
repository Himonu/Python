#el .py abre siempre con consola
#el .pyw abre sin consola, solo la ventana en grafica

from tkinter import *

root = Tk()

root.title("Prueba grafica 1")

#resizable se usa para "bloquear" a los lados o arriba y abajo, el primero es los laterales y el segundo verticalmente
root.resizable(1,1)

#bitmap es para darle la imagen a que desees en icono siempre que coloques en el la direccion del icono
root.iconbitmap("alucard.ico")

#geometry funciona dando las dimensiones de tamaño que desees
#La raiz se adapta al tamaño del frame

#root.geometry("400x350")

#tiene multiples funciones config
#el usar bg seria para dar un color de fondo
root.config(bg="red")

root.config(cursor="hand2")

#creacion de un frame
miFrame = Frame()

#para empaquetar se usa pack
miFrame.pack(fill="both", expand="True")

miFrame.config(bg="blue")

miFrame.config(width="400", height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

#esto es necesario siempre al final
root.mainloop()


