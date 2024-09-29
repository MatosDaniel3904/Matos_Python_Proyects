import tkinter as tk

def registrar_persona():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    id = entry_id.get()
    pais = entry_pais.get()
    profesion = entry_profesion.get()

    # Aquí puedes agregar la lógica para guardar los datos, por ejemplo, en un archivo o base de datos
    print("\n\nDatos registrados:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Número ID:", id)
    print("País:", pais)
    print("Profesión:", profesion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Personas")

# Crear los labels y entradas de texto
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_id = tk.Label(ventana, text="Número ID:")
label_id.pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

label_pais = tk.Label(ventana, text="Pais:")
label_pais.pack()
entry_pais = tk.Entry(ventana)
entry_pais.pack()

label_profesion = tk.Label(ventana, text="Profesión:")
label_profesion.pack()
entry_profesion = tk.Entry(ventana)
entry_profesion.pack()


# Crear el botón de registro
boton_registrar = tk.Button(ventana, text="Registrar", command=registrar_persona)
boton_registrar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
