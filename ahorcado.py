#importar un módulo random para que la computadora seleccione cualquier palabra de mi lista
#Importar getpass y stdiomask para poder ocultar las palabras ingresadas por los jugadores
import random
import getpass 
import stdiomask

print("Desarrollador: Dave Madrid Romero")
print("---------------------------------")
print("Bienvenido al juego del ahorcado")
print("---------------------------------")
lista_de_dificultad = "nada"
#Dar la opción de jugar dos modos, un jugador contra la máquina o dos jugadores con otra persona
modo = int(input("Pulsa el número 1 para el modo de un jugador o pulsa 2 para el modo 2 jugadores: "))
while modo <1 or modo >2:
    print("El número ingresado no es permitido, vuelve a elegir el número que corresponda al modo de juego ")
    modo = int(input("Pulsa el número 1 para el modo de un jugador o pulsa 2 para el modo 2 jugadores: "))
if modo == 1:
    #Defino mi propia función para la selección de dificultad del juego, la dificultad se define por la longitud de las palabras
    print("Has elegido el modo de un jugador")
    def dificultad (facil = 1, normal = 2, dificil = 3): 
        global lista_de_dificultad
        global nivel
        nivel = int(input("Elige la dificultado del juego : Fácil es 1, Normal es 2 y Dificil es 3: "))
        while nivel <1 or nivel >3:
           print("///////////////////////////////////////////////////////////////////////////////////")
           print("El número es incorrecto, vuelve a elegir un número correspondiente a la dificultad")
           print("///////////////////////////////////////////////////////////////////////////////////")
           nivel = int(input("Elige la dificultado del juego : Fácil es 1, Normal es 2 y Difícil es 3: "))
        if nivel == facil:
           print("Dificultad fácil seleccionada")
           lista_de_dificultad = ["amor","alto","azul","baño","vela","vaca"] 
        elif nivel == normal:
           print("Dificultad normal seleccionada")
           lista_de_dificultad = ["atacar","animal","conejo","camino","dibujo","letras","nombre"]
        elif nivel == dificil:
           print("Dificultad difícil seleccionada")
           lista_de_dificultad = ["extraordianario","resultado","palabras","jugadores","escritorio","programador","estructura","diagrama"]  
    dificultad()
    #Declarar mi lista de palabras para el juego
    lista_de_palabras = lista_de_dificultad
    #La computadora selecciona una palabra de mi lista declarada y muestra la longitud de la palabra
    palabra_generada = random.choice(lista_de_palabras)
    letras_introducidas = []
    posiciones = "-" * len(palabra_generada)
    print(posiciones)
    #Dejar en 0 las vidas, con cada fallo el contador aumentara 1.
    vidas = 0
    #Crear un bucle cuando las vidas son menores a 5
    while vidas < 5:
        # El jugador introduce su letra
        letra = input("Por favor introduce una letra: ")[:1]
        #La convierte en minuscula
        letra.lower
        # Si la letra ya fue introducida no se agrega
        if letra in letras_introducidas:
            print("Esa letra ya fue adivida, prueba con otra")
        # En este apartado si la letra es correcta se agregara a las posiciones reemplazando los guiones por la letra de la palabra correcta
        elif letra in palabra_generada:
            for i in range(len(palabra_generada)):
                if palabra_generada[i] == letra:
                    posiciones = posiciones[:i] + letra + posiciones[i+1:]
            print("¡Bien hecho! La palabra es:", posiciones)
            # Si ya no hay guiones estonces la palabra se completo y el jugador gana y se muestra la palabra
            if "-" not in posiciones:
                print("Felicidades, adivinaste la palabra:", posiciones)
                break
        else: 
            #En caso de fallar se le agregara 1 a su contador de vidas hasta llegar al máximo de 5
            vidas += 1
            print("Letra incorrecta, te quedan", 5-vidas, "vidas.")
            letras_introducidas.append(letra)
            if vidas == 1:
                print("  O")
            elif vidas == 2:
                print("  O")
                print("  |")
            elif vidas == 3:
                print("  O")
                print(" /|")
            elif vidas == 4:
                print("  O")
                print(" /|\\")
            elif vidas == 5:
                print("  O")
                print(" /|\\")
                print(" / \\")
                print("No adivinaste la palabra. La palabra correcta era", palabra_generada)
                break
if modo == 2: 
    #Se pide los nombres de los jugadores para entender mejor
    nombre1 = input("Ingrese su nombre jugador 1: ")
    nombre2 = input("Ingrese su nombre Jugador 2: ")
    # El primer jugador ingresa su palabra
    PalabraJ1 = stdiomask.getpass(prompt= f"{nombre1} ingrese la palabra para que lo adivine el jugador {nombre2} ")
    PalabraJ1 = PalabraJ1.lower()
    # Se muestra las posiciones de la palabra del primer jugador
    letras_introducidas = []
    posiciones = "-" * len(PalabraJ1)
    print(posiciones)
    # Se empieza con 0 vidas
    vidas = 0
    while vidas <5:
        letra = input("Por favor introduce una letra: ")[:1]
        letra = letra.lower()
        if letra in letras_introducidas:
            print("Esa letra ya fue adivida, prueba con otra")
        elif letra in PalabraJ1:
            for i in range(len(PalabraJ1)):
                if PalabraJ1[i] == letra:
                    posiciones = posiciones[:i] + letra + posiciones[i+1:]
            print("¡Bien hecho!",nombre2, "la palabra es:", posiciones)
            if "-" not in posiciones:
                print("Felicidades ",nombre2, "adivinaste la palabra:", posiciones)
                break
        else: 
        #En caso de fallar se le agregara 1 a su contador de vidas hasta llegar al máximo de 5
            vidas += 1
            print("Letra incorrecta, te quedan", 5-vidas, "vidas.")
            letras_introducidas.append(letra)
            if vidas == 1:
                print("  O")
            elif vidas == 2:
                print("  O")
                print("  |")
            elif vidas == 3:
                print("  O")
                print(" /|")
            elif vidas == 4:
                print("  O")
                print(" /|\\")
            elif vidas == 5:
                print("  O")
                print(" /|\\")
                print(" / \\")
                print("No adivinaste la palabra ",nombre1, ".La palabra correcta era", PalabraJ1)
                break
    # El primer jugador ingresa su palabra
    PalabraJ2 = stdiomask.getpass(prompt= f"{nombre1} ingrese la palabra para que lo adivine el jugador {nombre2} ")
    PalabraJ2 = PalabraJ2.lower()
    # Se muestra las posiciones de la palabra del segundo jugador
    letras_introducidas = []
    posiciones = "-" * len(PalabraJ2)
    print(posiciones)
    # Se empieza con 0 vidas
    vidas = 0
    while vidas <5:
            letra = input("Por favor introduce una letra: ")[:1]
            letra = letra.lower()
            if letra in letras_introducidas:
                print("Esa letra ya fue adivida, prueba con otra")
            elif letra in PalabraJ2:
                for i in range(len(PalabraJ2)):
                    if PalabraJ2[i] == letra:
                        posiciones = posiciones[:i] + letra + posiciones[i+1:]
                print("¡Bien hecho!",nombre1, "la palabra es:", posiciones)
                if "-" not in posiciones:
                    print("Felicidades ", nombre1, "adivinaste la palabra:", posiciones)
                    break
            else: 
            #En caso de fallar se le agregara 1 a su contador de vidas hasta llegar al máximo de 5
                vidas += 1
                print("Letra incorrecta, te quedan", 5-vidas, "vidas.")
                letras_introducidas.append(letra)
                if vidas == 1:
                    print("  O")
                elif vidas == 2:
                    print("  O")
                    print("  |")
                elif vidas == 3:
                    print("  O")
                    print(" /|")
                elif vidas == 4:
                    print("  O")
                    print(" /|\\")
                elif vidas == 5:
                    print("  O")
                    print(" /|\\")
                    print(" / \\")
                    print("No adivinaste la palabra", nombre1, ".La palabra correcta era", PalabraJ2)
                    break


