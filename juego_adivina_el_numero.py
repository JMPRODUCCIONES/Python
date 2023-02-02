from random import randint
intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Ingrese su nombre:")

print('Bueno {nombre} he pensado un número entre 1 y 100\n Tienes solo ocho intentos para adivinar cuál crees que es el número')

while intentos < 8:
    estimado = int(input("Cual es el numero?:"))
    intentos += 1
    
    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va del 1 al 100")
    
    if estimado < numero_secreto:
        print("Mi numero es mas alto")   
    elif estimado  > numero_secreto:
        print("El numero es mas bajo")      
    else:
        print(f"Felicitaciones{nombre}!Has adivinado en {intentos} intentos")   
    break
     
     
if estimado != numero_secreto:
      print(f"Lo siento se han agotado los intentos")