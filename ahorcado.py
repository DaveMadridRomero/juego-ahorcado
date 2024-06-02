#importar un módulo random para que la computadora seleccione cualquier palabra de mi lista
import random
print("Desarrollador: Dave Madrid Romero")
print("---------------------------------")
print("Bienvenido al juego del ahorcado")
print("---------------------------------")
#Declarar mi lista de palabras para el juego
lista_de_palabras = ["letra","casa","animal","jugador","auto","celular","dibujo","escuela"]
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
            print("No adivinaste la palabra. La palabra era", palabra_generada)
            break
    




    
