import tkinter as tk
import random

def generar_numero():
  numero_aleatorio = random.randint(1, 100)  # Genera un número entre 1 y 100
  label_resultado.config(text=(f"\nEl número ganador es: {numero_aleatorio}"))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionador de  números por sorteo")

# Crear un botón
boton = tk.Button(ventana, text="Sortear número", command=generar_numero)
boton.pack()

# Crear un label para mostrar el resultado
label_resultado = tk.Label(ventana)
label_resultado.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
