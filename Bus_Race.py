import os 
import random
import time 

GREN ="\033[32m"
END = "\033[0m"

while True :
 def buses(n1,n2):
    print(115*"-")
    print ( (n1*" ") + "_______________     "               + ((100-n1)* " " )+ "|" )
    print ( (n1*" ") + "|__|__|__|__|__|       "               + ((97-n1)* " " )+  "|" )
    print ( (n1*" ") + "|      BUS 1   |  )     "             + ((96-n1)* " " )+ "|" )
    print ( (n1*" ") + "|¬¬¬¬@¬¬¬¬¬¬¬¬@¬¬|)      "          + ((95-n1)* " " )+ "|" )
    print(115*"-")
    print ( (n2*" ") + "_______________     "               + ((100-n2)* " " )+ "|" )
    print ( (n2*" ") + "|__|__|__|__|__|       "               + ((97-n2)* " " )+ "|" )
    print ( (n2*" ") + "|      BUS 2   |  )     "             + ((96-n2)* " " )+ "|" )
    print ( (n2*" ") + "|¬¬¬¬@¬¬¬¬¬¬¬¬@¬¬|)      "          + ((95-n2)* " " )+ "|" )
    print(115*"-")
    return "Let the race begins!!!!"

 a = 0
 b = 0 

 presentation = """<<<<<<<<<< BUSES RACE >>>>>>>>>>
                               BUS 1 VS BUS 2"""
                
 print(presentation)
 time.sleep(3)
 os.system("cls")

 while( a < 97 and b < 97):
    c = random.randint(1,2)
    if c ==1 :
        a+=1
    if c == 2 :
        b+=1
    os.system("cls")
    print(buses(a,b))        
    time.sleep(0.07)
    
 if a == 97:
    wins = "BUS 1"
    
 if b == 97:
   wins = "BUS 2"
    
 print(f"{GREN}{wins} has won the race {END}")
 
 pregunta= input("¿Volver a correr? (si/no): ")
 
 if pregunta.lower() == "no":
     break


        
while True:
    input("\nFinished!!!")
    break
