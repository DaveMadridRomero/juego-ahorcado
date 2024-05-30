#importar la biblioteca random para que la computadora seleccione una palabra de mi lista
import random

print("================================")
print("Bienvenido al juego del ahorcado")
print("================================")
#Declarar mi lista de palabras para el juego
lista_de_palabras = ["letra","casa","animal","jugador","auto","celular","dibujo","escuela"]
#La computadora selecciona una palabra de mi lista declarada y muestra la longitud de la palabra
palabra_generada = random.choice(lista_de_palabras)
posiciones = "_ " * len(palabra_generada)
#Definir las oportunidades que tiene el jugador
vidas = 6
#letra1 = str(input("Por favor introduce una letra: "))[:1]
#Bucles y condicional para introducir y detectar si las letras son correctas o no
while True:
    print(posiciones)
    letra = str(input("Por favor introduce una letra: "))[:1]
    #En caso de introducir una mayúscula el programa lo convierte en minúscula
    letra.lower 
    if letra in palabra_generada:
        #definir una iteración con la cantidad de caracteres que tiene la palabra elegida por la máquina
        for i in range(len(palabra_generada)):
            if palabra_generada[i] == letra:
                posiciones = posiciones[:i] + letra + posiciones[i+1]
                           
            

    

