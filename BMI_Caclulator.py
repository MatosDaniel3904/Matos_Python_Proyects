import customtkinter
from tkinter import messagebox

def calcular_imc(peso, altura):
    try:
        
        peso = float(peso)
        altura = float(altura) / 100  # Convertir cm a metros
        if altura == 0:
            return "Error: La altura no puede ser cero."
        imc = peso / (altura ** 2)
        return imc
    except ValueError:
        return "Error: Por favor, introduce números válidos."
    
def mostrar_resultado(imc):
    if isinstance(imc, str) and imc.startswith("Error"):
        messagebox.showerror("Error", imc)
    elif imc < 18.5:
        mensaje = "Bajo peso. Considera consultar a un profesional de la salud."
        titulo = "Resultado: Bajo Peso"
    elif 18.5 <= imc < 25:
        mensaje = "Peso saludable. ¡Sigue así!"
        titulo = "Resultado: Peso Saludable"
    elif 25 <= imc < 30:
        mensaje = "Sobrepeso. Podrías considerar cambios en tu estilo de vida."
        titulo = "Resultado: Sobrepeso"
    elif 30 <= imc < 35:
        mensaje = "Obesidad grado I. Se recomienda buscar asesoramiento médico."
        titulo = "Resultado: Obesidad Grado I"
    elif 35 <= imc < 40:
        mensaje = "Obesidad grado II. Es importante consultar a un médico."
        titulo = "Resultado: Obesidad Grado II"
    else:
        mensaje = "Obesidad grado III. Busca atención médica para evaluar tu salud."
        titulo = "Resultado: Obesidad Grado III"
    messagebox.showinfo(titulo, f"Tu IMC es: {imc:.2f}\n\n{mensaje}")
    
def app():
    app = customtkinter.CTk()
    app.title("Calculadora de IMC")

    peso_label = customtkinter.CTkLabel(app, text="Peso (kg):")
    peso_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    peso_entry = customtkinter.CTkEntry(app)
    peso_entry.grid(row=0, column=1, padx=10, pady=10)

    altura_label = customtkinter.CTkLabel(app, text="Altura (cm):")
    altura_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    altura_entry = customtkinter.CTkEntry(app)
    altura_entry.grid(row=1, column=1, padx=10, pady=10)

    def calcular_y_mostrar():
        peso = peso_entry.get()
        altura = altura_entry.get()
        resultado_imc = calcular_imc(peso, altura)
        mostrar_resultado(resultado_imc)

    calcular_button = customtkinter.CTkButton(app, text="Calcular IMC", command=calcular_y_mostrar)
    calcular_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    app.mainloop()

if __name__ == "__main__":
    app()
          
         
