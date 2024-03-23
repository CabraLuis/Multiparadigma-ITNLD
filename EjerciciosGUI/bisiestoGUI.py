from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
form = ttk.Frame(root, padding = 10)
form.grid()


def CalcularBisiesto(year):
    esBisiesto = False
    if year % 4 == 0:
        esBisiesto = True
        if year % 100 == 0:
            esBisiesto = False
            if year % 400 == 0:
                esBisiesto = True
    messagebox.showinfo(title = "Resultado", message = "El año es bisiesto" if esBisiesto else "El año no  es bisiesto")
    
root.title("Año Bisiesto")

label = ttk.Label(form, text = "Ingrese el año")
entry = ttk.Entry(form)
button = ttk.Button(form, text = "¿Es bisiesto?", command = lambda : CalcularBisiesto(int(entry.get())))

label.grid(column = 0, row = 0)
entry.grid(column = 1, row = 0)
button.grid(column = 0, row = 1)

root.mainloop()

