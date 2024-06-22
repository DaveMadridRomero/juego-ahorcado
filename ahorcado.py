#importar un módulo random para que la computadora seleccione cualquier palabra de mi lista
#Importar getpass y stdiomask para poder ocultar las palabras ingresadas por los jugadores
import random
import getpass 
import stdiomask


UN_JUGADOR = 1
DOS_JUGADORES = 2

FACIL = 1
NORMAL = 2
DIFICIL = 3

PALABRAS_FACIL = ["amor","alto","azul","baño","vela","vaca"]
PALABRAS_NORMAL = ["atacar","animal","conejo","camino","dibujo","letras","nombre"]
PALABRAS_DIFICIL = ["extraordianario","resultado","palabras","jugadores","escritorio","programador","estructura","diagrama"]  

INTENTOS_DEFINIDOS = 5

lista_de_palabras= []

def seleccionar_dificultad(): 
    #Variables en global
    global lista_de_palabras
    nivel = 0
    while True:
        nivel = int(input("Elige la dificultad del juego : \n1)Fácil\n2)Normal\n3)Difícil\n\nIngrese dificultad: "))
        if nivel == FACIL:
            print("Dificultad fácil seleccionada")
            lista_de_palabras = PALABRAS_FACIL
            break
        elif nivel == NORMAL:
            print("Dificultad normal seleccionada")
            lista_de_palabras = PALABRAS_NORMAL
            break
        elif nivel == DIFICIL:
            print("Dificultad difícil seleccionada")
            lista_de_palabras = PALABRAS_DIFICIL
            break
        else:
            print("La opción es incorrecta, vuelve a elegir la opción correspondiente a la dificultad")

def obtener_palabra(nombre):
    palabra_ingresada = stdiomask.getpass(prompt= f"[{nombre}] ingresa la palabra para que la adivine el otro jugador: ")
    palabra_ingresada = palabra_ingresada.lower()
    return palabra_ingresada
    
        
def proceso_interno(Palabra, nombre):
    intentos = 0
    letras_ingresadas = []
    posiciones = "-" * len(Palabra)
    print(posiciones)
    while intentos < INTENTOS_DEFINIDOS:
        letra = input("Por favor ingresa una letra: ")[:1]
        letra = letra.lower()
        if letra in letras_ingresadas:
            print("Esa letra ya fue ingresada, prueba con otra")
        elif letra in Palabra:
            for i in range(len(Palabra)):
                if Palabra[i] == letra:
                    posiciones = posiciones[:i] + letra + posiciones[i+1:]
            print(f"¡Bien hecho! [{nombre}] la palabra es: {posiciones}")
            if "-" not in posiciones:
                print(f"Felicidades [{nombre}] adivinaste la palabra: {posiciones.upper()}")
                break
        else: 
        #En caso de fallar se le agregara 1 a su contador de vidas hasta llegar al máximo de 5
            intentos += 1
            print("Letra incorrecta, te quedan", INTENTOS_DEFINIDOS-intentos, "intentos.")
            letras_ingresadas.append(letra)
            if intentos == 1:
                print("  O")
            elif intentos == 2:
                print("  O")
                print("  |")
            elif intentos == 3:
                print("  O")
                print(" /|")
            elif intentos == 4:
                print("  O")
                print(" /|\\")
            elif intentos == 5:
                print("  O")
                print(" /|\\")
                print(" / \\")
                print(f"No adivinaste la palabra [{nombre}].La palabra correcta era {Palabra}")
                break


print("Desarrollador: Dave Madrid Romero")
print("---------------------------------")
print("Bienvenido al juego del ahorcado")
print("---------------------------------")


#Dar la opción de jugar dos modos, un jugador contra la máquina o dos jugadores con otra persona
#modo = int(input("1)Modo 1 jugador \n2)Modo 2 jugadores \n\nEscoja una opción: "))
while True:
    modo = int(input("1) Modo 1 jugador \n2) Modo 2 jugadores \n\nEscoja una opción: "))
    if modo == UN_JUGADOR or modo == DOS_JUGADORES:
        break
    else:
        print("El modo de juego no es permitido, vuelve a elegir el número que corresponda al modo de juego ")
      
if modo == UN_JUGADOR:
    print("Has elegido el modo de un jugador")
    seleccionar_dificultad()
    palabra_generada = random.choice(lista_de_palabras)
    nombre = input("Ingrese su nombre jugador: ")
    proceso_interno(palabra_generada, nombre)

    
if modo == DOS_JUGADORES: 
    print("Seleccionaste el modo de dos jugadores")
    nombre_1 = input("Ingrese su nombre jugador 1: ")
    nombre_2 = input("Ingrese su nombre Jugador 2: ")
    
    palabra_j1 = obtener_palabra(nombre_1)
    
    proceso_interno(palabra_j1, nombre_2)
    
    palabra_j2 = obtener_palabra(nombre_2)

    proceso_interno(palabra_j2, nombre_1)
    
    
    
