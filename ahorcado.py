import random

print("================================")
print("Bienvenido al juego del ahorcado")
print("================================")
#Declarar mi lista de palabras para el juego
lista_de_palabras = ["letra","casa","animal","jugador","auto","celular","dibujo","escuela"]
#La computadora selecciona una palabra de mi lista declarada y mostrar la longitud de la palabra
palabra_generada = random.choice(lista_de_palabras)
cadena = "_ " * len(palabra_generada)
#Definir las oportunidades que tiene el jugador
vidas = 6
#El jugador introduce su letra
#letra1 = str(input("Por favor introduce una letra: "))[:1]
#Bucles y condicional para introducir y detectar si las letras son correctas o no
while True:
    print(cadena)
    letra1 = str(input("Por favor introduce una letra: "))[:1]
    

    

