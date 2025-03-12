# Seleciona los productos de la lista y calcula su precio 



class Pago_Virtual:
    
    def __init__(self,nombre,cédula,clave) :
        self.nombre = nombre
        self.cédula = cédula
        self.clave =  clave 
       



#Diccionario donde se encuentran los productos y sus repectivos precios
Productos =  {"harina": 3.20 ,"café": 3.55 ,"pan blanco": 3.75 ,"pan integral":4.00,"leche": 2.48,
              "azúcar": 6.54 ,"cereal" : 4.89 ,  "mantequilla" : 5.21, "jugo de durazno": 5.50,
              "jugo de manzana":5.50,"galletas":5.25,"huevos":4.21, "tostitos":5.10,"yogurt":5.00 , 
               "helado":6.50}

#Lista donde se guardarán los productos seleccionados
Carrito = []

# A través de pandas se importa el archivo donde están la lista de los productos y sus precios
import pandas as pd

Lista_de_productos = pd.read_csv("C:\\Users\\HP ELITEDESK\Desktop\\Register_POO\\Productos.csv")

# Función para mostrar que productos se han seleccionado y estan en la lista de compras (carrito)
def mostrar_carrito(Carrito):
    if not Carrito:
        print("\nAún no hay nada en el carrito")
    else:
        print("\nTu carrito:")
        for i, kart in enumerate(Carrito):
            print(f"{i +1}. {kart}")
            
print("\n!Bienvenido¡") 
print("\n Escoja los productos añadiendolos al carrito")   

# Bucle para mantenerse dentro del programa del mercadito    
while True:
    
    #Menú principal
    print("\n1. Añadir al carrito/ Ver productos")
    print("2. Mostrar carrito")
    print("3. Mostrar Total")
    print("4. Pagar")
    print("5. Cancelar y salir")
    opción = input("Seleccione una opción: ")
    
    # Método mendiante el cuál se añaden los productos a la lista de compras (carrito)
    if opción =="1":
     print("\nProductos disponibles:")
     print(Lista_de_productos)
     
     producto = input("Agregue un producto o volver: ").lower()
     
     if producto in Productos :
        Carrito.append(producto)
        print("\nProducto añadido")
     else: 
        print("Producto no encontrado ._.")
    
    # Función para mostrar la lista de compras (carrito)    
    elif opción == "2": 
        mostrar_carrito(Carrito)
       
    # Método para sumar los precios de todos los productos seleccionados  
    elif opción == "3":
     Total = round(sum(Productos[producto] for producto in Carrito))
     print(f"\nSu total a pagar es de: {Total}$")   
   
   # Opción de pagar o salir
    elif opción == "4" :
        
        print(f"\nSu total a pagar es: {Total}$")
        print("1. Pagar")
        print("2. Cancelar")
        pago = input("¿Desea pagar o cancelar?: ")
        
        
        if pago == "1" :
         nombre = input("\nDigame su nombre: ")
         cédula= input("\nDigame su cédula o DNI: ")
         clave = input("\nAhora, ingrese su clave: ")
         pago = Pago_Virtual(nombre,cédula,clave)

        
         print(f""" 
      
         Datos de Facturación: \n\n
         Nombre: {pago.nombre} \n
         Cédula: {pago.cédula}\n
         Lista : {Carrito}\n
         Total : {f"{Total} $"}
      
         """)
        
         print("\nPago realizado")
         print("\n!Gracias por su compra¡")
         break
         
        elif pago == "2" :
            print("\nOperación cancelada ")
            break
     
   
    elif opción == "5" :
        print("\nOperación cancelada ")
        break
   
    else:
        print("\nOpción inválida. Inténtelo de nuevo")    
 
        
while True :
    input("\nHasta luego. Vuelva Pronto")
    break

