# MSQ
# Demo UI


        # buttons = [("C:/Users/migue/Pictures/car.png", self.car_function),

import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import datetime

# Crear una ventana de pantalla completa
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title = "Control Playa v 1.0 - build240301"

# Cargar iconos para los botones
icons = {
    "car": ImageTk.PhotoImage(Image.open("C:/Users/migue/Pictures/car.png")),
    "truck": ImageTk.PhotoImage(Image.open("C:/Users/migue/Pictures/car.png")),
    "motorcycle": ImageTk.PhotoImage(Image.open("C:/Users/migue/Pictures/car.png")),
    "bike": ImageTk.PhotoImage(Image.open("C:/Users/migue/Pictures/car.png")),
    "plane": ImageTk.PhotoImage(Image.open("C:/Users/migue/Pictures/car.png"))
}

# Crear botones con iconos
for i, (vehicle, icon) in enumerate(icons.items()):
    button = tk.Button(root, image=icon, command=lambda v=vehicle: print(f"{v} button clicked"))
    button.grid(row=0, column=i, padx=20, pady=20)

# Crear un campo de texto
input_text = tk.Entry(root, font=('Helvetica', 36, 'bold'), width=8)
input_text.grid(row=1, column=0, columnspan=5)

# Función para actualizar las etiquetas de tiempo y fecha
def update_time_date():
    now = datetime.datetime.now()
    time_label.config(text=now.strftime('%H:%M:%S'))
    date_label.config(text=now.strftime('%Y-%m-%d'))
    root.after(1000, update_time_date)

# Crear etiquetas para tiempo y fecha
time_label = tk.Label(root, font=('Helvetica', 36, 'bold'))
time_label.grid(row=2, column=0, columnspan=5)
date_label = tk.Label(root, font=('Helvetica', 36, 'bold'))
date_label.grid(row=3, column=0, columnspan=5)

# Iniciar el bucle de actualización de tiempo y fecha
update_time_date()


# Función para cerrar la aplicación
def exit_app():
    root.destroy()

# Crear un botón de salida
exit_button = tk.Button(root, text="Salir", font=('Helvetica', 36, 'bold'), command=exit_app)
exit_button.grid(row=4, column=0, columnspan=5)


# Ejecutar la aplicación
root.mainloop()
