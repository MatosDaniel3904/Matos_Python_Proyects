import tkinter as tk
import random

def generate_number():
  random_number = random.randint(1, 100)  # Genera un número entre 1 y 100
  label_result.config(text=(f"\nEl número ganador es: {random_number}"))

# Crear la ventana principal
window = tk.Tk()
window.title("Random Number Selector")

# Crear un botón
button = tk.Button(ventana, text="Sortear número", command=generate_number)
button.pack()

# Crear un label para mostrar el resultado
label_result = tk.Label(ventana)
label_result.pack()

# Iniciar el bucle principal de la aplicación
window.mainloop()
