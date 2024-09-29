class Personaje :
    def __init__(self,nombre,ataque,defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        
    def __repr__(self):
        return f"{self.nombre} (Ataque: {self.ataque}, Defensa: {self.defensa})"
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj
        nueva_ataque = round(((self.ataque + otro_pj.ataque)/2)**1.35)
        nuevo_defensa =round(((self.defensa + otro_pj.defensa)/2)**1.35)
        return Personaje(nuevo_nombre,nueva_ataque,nuevo_defensa)
    
def mostrar_personajes(personajes):
        if not personajes:
            print("\nAún no ha creado ningún personaje")
        else:
            print("\nPesonajes disponibles:")
            for i, personaje in enumerate(personajes):
                print(f"{i +1}. {personaje}")    
            
             
def crear_personaje():  
        nombre = input("Ingrese el nombre del personaje: ")
        ataque = float(input("ingrese el ataque del personaje: "))   
        defensa = float(input("ingrese la defensa del personaje: "))
        return Personaje(nombre,ataque,defensa)
    
def fusionar_personajes(personaje_1,personaje_2):
    merged_name = personaje_1.nombre[:len(personaje_1.nombre)//2] + personaje_2.nombre[len(personaje_1.nombre)//2 :]
    merged_attack = personaje_1.ataque + personaje_2.ataque
    merged_defense = personaje_1.defensa + personaje_2.defensa
    personaje_fus = Personaje(merged_name, merged_attack, merged_defense)
    return personaje_fus
      
    
personajes = []
    
 
    
while True:
        print("\n1 Crear personaje")
        print("2 Fusionar personaje")
        print("3 Mostrar personaje")
        print("4 salir")
        opción = input("\nSeleccione una opción: ")
        
        if opción == "1":
            personaje_nuevo = crear_personaje()
            personajes.append(personaje_nuevo)
            print("\n¡Personaje creado exitosamente!")
            
        elif opción == "2":
            if len(personajes) <2 :
                print("\nDebe tener al menos dos personajes para fusionar")
            
            else:
                mostrar_personajes(personajes)
                num_pj1 = int(input("\nIngrese el número del primer personaje: "))
                num_pj2 = int(input("\nIngrese el número del segundo personaje: "))
                
                if 1 <= num_pj1 <= len(personajes) and 1 <= num_pj2 <= len(personajes)and num_pj1 != num_pj2:
                    personaje_1= personajes[num_pj1-1]
                    personaje_2= personajes[num_pj2-1]
                    personaje_fusionado = fusionar_personajes(personaje_1,personaje_2)
                    personajes.append(personaje_fusionado)
                    print(f"\n¡Fusión exitosa! El nuevo personaje es {personaje_fusionado}" )
                else:
                    print("\nSelección inválida. asegúrese de elegir personajes válidos")
                    
        elif opción == "3":
         mostrar_personajes(personajes)
         
        elif opción == "4":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\n Opción inválida. Por favor, seleccione una opción válida.")
            

            
while True:
    input("Juego Terminado")    
    break
                   
