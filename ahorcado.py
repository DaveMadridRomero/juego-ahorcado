#importar la biblioteca random para que la computadora seleccione cualquier palabra de mi lista
import random
print("Desarrollador: Dave Madrid Romero")
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
letra1 = str(input("Por favor introduce una letra: "))[:1]
if letra1 in palabra_generada:
    


    
