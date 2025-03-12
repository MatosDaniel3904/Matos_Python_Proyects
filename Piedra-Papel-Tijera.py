import random

opciones = ["piedra", "papel", "tijera"]


while True:
    
    usuario = input("Elige: Piedra, Papel o Tijera: ").lower()
    computadora = random.choice(opciones)
    print("Computadora elige:",computadora)
    
    if usuario == computadora:
        print("¡Empate!")
    
    elif usuario == "piedra" and computadora == "tijera" or \
        usuario == "tijera" and computadora == "papel" or \
        usuario == "papel" and computadora == "piedra" :
            print ("¡Ganaste!")
    
    else:
        print("Perdiste ._.")     
    
    jugar_de_nuevo = input("¿Queres jugar otra vez? (si/no): ").lower()
    
    if jugar_de_nuevo != "si" :
        break
