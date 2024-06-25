#importar un módulo random para que la computadora seleccione cualquier palabra de mi lista

import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

COLOR_FONDO = "white"

UN_JUGADOR = 1
DOS_JUGADORES = 2

TURNO_JUGADOR_1 = 1
TURNO_JUGADOR_2 = 2
FINALIZAR = 3

FACIL = 1
NORMAL = 2
DIFICIL = 3

PALABRAS_FACIL = ["amor","alto","azul","baño","vela","vaca"]
PALABRAS_NORMAL = ["atacar","animal","conejo","camino","dibujo","letras","nombre"]
PALABRAS_DIFICIL = ["extraordianario","resultado","palabras","jugadores","escritorio","programador","estructura","diagrama"]  

INTENTOS_DEFINIDOS = 5

nombre = ""
nombre_1 = ""
nombre_2 = ""
dificultad = 0
palabra_generada = ""
posiciones = ""
lista_de_palabras= []
turno_de_adivinar = 0
modo_juego = 0
ventana_principal = None
entry_nombre = None
entry_nombre_j1 = None
entry_nombre_j2 = None
entry_palabra = None 
entry_letra = None
oportunidades = 0
letras_ingresadas = []
etiqueta_posiciones = None
frame_fallos = None

def valida_letra(entry_letra_ingresado):
    if len(entry_letra_ingresado) == 1 and entry_letra_ingresado.isalpha():
        return True
    else:
        return False


def centrar_windows(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    ventana.geometry(f"{width}x{height}+{x}+{y}")
        
def crear_ventana_principal():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Juego del ahorcado")
    ventana_principal.geometry("800x600")
    ventana_principal.configure(bg='white')
    centrar_windows(ventana_principal)
    fondo_ventana_principal()
    #menu modo de juego
    menu_modo_juego()
    
    ventana_principal.mainloop()
    
def fondo_ventana_principal():
    """imagen = tk.PhotoImage(file="Imagenes/fondo_principal.png")
    label1 = tk.Label(ventana_principal, image = imagen)
    label1.image = imagen
    label1.place(x = 0,y = 0)"""

def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()
    fondo_ventana_principal()
  
def limpiar_frame_fallos():
    if frame_fallos and frame_fallos.winfo_exists():
        for widget in frame_fallos.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
        frame_fallos.destroy()

def imagen_boton_menu_juego():
    imagen_original = Image.open("Imagenes/boton_modo_juego.png")
    nueva_imagen = imagen_original.resize((300, 60))
    imagen = ImageTk.PhotoImage(nueva_imagen)
    return imagen

def imagen_boton_jugar_juego():
    imagen_original = Image.open("Imagenes/boton_play.png")
    nueva_imagen = imagen_original.resize((150, 60))
    imagen = ImageTk.PhotoImage(nueva_imagen)
    return imagen


def menu_modo_juego():
    limpiar_ventana()

    etiqueta = tk.Label(ventana_principal, text="Modo de juego", font=("Calibri", 35), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady= 50)
    imagen = imagen_boton_menu_juego()
    # Botón 1
    boton_1 = tk.Button(ventana_principal, text="Un jugador", command=menu_seleccion_dificultad,
                fg="black",
                bg=COLOR_FONDO,
                font=("Calibri", 20),
                image = imagen,
                cursor="hand2",
                compound="center",
                relief="flat",
                width=300, height=60)


    boton_1.pack(pady=15)
    boton_1.image = imagen

    # Botón 2
    boton_2 = tk.Button(ventana_principal, text="Dos jugadores", command=ventana_dos_jugadores,
                        fg="black",
                        bg=COLOR_FONDO,
                        font=("Calibri", 20),
                        image=imagen,
                        cursor="hand2",
                        compound="center",
                        relief="flat",
                        width=300, height=60)
    boton_2.pack(pady=15)
    boton_2.image = imagen
    
    
def ventana_dos_jugadores():
    limpiar_ventana()
    global modo_juego
    global entry_nombre_j1
    global entry_nombre_j2
    global turno_de_adivinar
    modo_juego = DOS_JUGADORES
    turno_de_adivinar = TURNO_JUGADOR_2
    etiqueta_j1 = tk.Label(ventana_principal, text="Ingrese su nombre jugador 1", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_j1.pack(pady=20)
    entry_nombre_j1= tk.Entry(ventana_principal, width=35,
              font=("Calibri", 25),
              bd=5,
              relief="ridge")
    entry_nombre_j1.pack(pady=15)
    
    etiqueta_j2= tk.Label(ventana_principal, text="Ingrese su nombre jugador 2", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_j2.pack(pady=10)
    entry_nombre_j2= tk.Entry(ventana_principal, width=35,
              font=("Calibri", 25),
              bd=5,
              relief="ridge")
    entry_nombre_j2.pack(pady=10)

    imagen = imagen_boton_jugar_juego()
    boton_jugar = tk.Button(ventana_principal, text="Jugar", command=ventana_ingresar_palabra, fg="#434141",
                            bg=COLOR_FONDO,
                            font=("Calibri", 20),
                            image=imagen,
                            cursor="hand2",
                            compound="center",
                            relief="flat",
                            width=150, height=60)
    boton_jugar.pack(pady=10)
    boton_jugar.imagen = imagen

def ventana_ingresar_palabra():
    global nombre_1
    global nombre_2
    global entry_nombre_j1
    global entry_palabra
    global turno_de_adivinar
    if entry_nombre_j1.winfo_exists():
        nombre_1 = entry_nombre_j1.get()
    if entry_nombre_j2.winfo_exists():
        nombre_2 = entry_nombre_j2.get()
    limpiar_ventana()
    print(nombre_1)
    print(nombre_2)
    if turno_de_adivinar == TURNO_JUGADOR_2:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Ingrese su palabra {nombre_1.upper()} ", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        entry_palabra = tk.Entry(ventana_principal, width=35,
              font=("Calibri", 25),
              bd=5,
              relief="ridge",
              justify='center',
              show="*")
        entry_palabra.pack(pady=10)
        boton_jugar_1 = tk.Button(ventana_principal, text="Jugar", command=palabra_jugadores, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
        boton_jugar_1.pack(pady=10)
    if turno_de_adivinar == TURNO_JUGADOR_1:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Ingrese su palabra {nombre_2.upper()} ", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        entry_palabra = tk.Entry(ventana_principal, width=35,
              font=("Calibri", 25),
              bd=5,
              relief="ridge",
              justify='center',
              show="*")
        entry_palabra.pack(pady=10)
        boton_jugar_2 = tk.Button(ventana_principal, text="Jugar", command=palabra_jugadores, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
        boton_jugar_2.pack(pady=10)
    if turno_de_adivinar == FINALIZAR:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Juego terminado",font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
        boton_regresar.pack(pady=5)


    

def palabra_jugadores():
    global palabra_generada
    global entry_palabra
    palabra_generada = entry_palabra.get()
    print(palabra_generada)
    ventana_jugar_dos_jugadores()
    
    
def ventana_jugar_dos_jugadores():
    limpiar_ventana()
    global palabra_generada
    global posiciones
    global etiqueta_posiciones
    global entry_letra
    global nombre
    global nombre_1
    global nombre_2

    if turno_de_adivinar == TURNO_JUGADOR_2:
        nombre = nombre_2
    if turno_de_adivinar == TURNO_JUGADOR_1:
        nombre = nombre_1


    etiqueta_titulo_juego = tk.Label(ventana_principal, text=f"El juego ya empezó, adivina la palabra {nombre}", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_titulo_juego.pack(pady=10)
    posiciones = "-" * len(palabra_generada)
    etiqueta_posiciones= tk.Label(ventana_principal, text=posiciones, font=("Helvetica", 35), fg='black', bg=COLOR_FONDO)
    etiqueta_posiciones.pack(pady=10)
    
    entry_letra = tk.Entry(ventana_principal, width=25,
              font=("Calibri", 18),
              bd=5,
              justify = "center",
              relief="ridge")
    entry_letra.pack(pady=10)
    
    boton_probar = tk.Button(ventana_principal, text="Probar", command=verificar, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 15),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=15)
    boton_probar.pack(pady=10)   
    

    
    
    

    
    
    
    
    

    
    

    



    
def menu_seleccion_dificultad():
    limpiar_ventana()
    global modo_juego
    modo_juego = UN_JUGADOR
    etiqueta = tk.Label(ventana_principal, text="Modos de dificultad", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)

    imagen = imagen_boton_menu_juego()
    # Botón 1
    boton_1 = tk.Button(ventana_principal, text="Fácil", command=jugar_facil, fg="black",
                bg=COLOR_FONDO,
                font=("Calibri", 20),
                image = imagen,
                cursor="hand2",
                compound="center",
                relief="flat",
                width=300, height=60)
    boton_1.pack(pady=15)
    boton_1.image = imagen

    # Botón 2
    boton_2 = tk.Button(ventana_principal, text="Normal", command=jugar_normal, bg=COLOR_FONDO,
                font=("Calibri", 20),
                image = imagen,
                cursor="hand2",
                compound="center",
                relief="flat",
                width=300, height=60)
    boton_2.pack(pady=15)
    boton_2.image = imagen
    
    boton_3 = tk.Button(ventana_principal, text="Difícil", command=jugar_dificil, bg=COLOR_FONDO,
                font=("Calibri", 20),
                image = imagen,
                cursor="hand2",
                compound="center",
                relief="flat",
                width=300, height=60)
    boton_3.pack(pady=15)
    boton_3.image = imagen
    
    boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, bg=COLOR_FONDO,
                font=("Calibri", 20),
                image = imagen,
                cursor="hand2",
                compound="center",
                relief="flat",
                width=300, height=60)
    boton_regresar.pack(pady=15)
    boton_regresar.image = imagen
      
    
def jugar_facil():
    global dificultad
    dificultad = FACIL
    texto_dificultad = "fácil"
    ventana_nombre_jugador(texto_dificultad)
    
def jugar_normal():
    global dificultad
    dificultad = NORMAL
    texto_dificultad = "normal"
    ventana_nombre_jugador(texto_dificultad)
    
def jugar_dificil():
    global dificultad
    dificultad = DIFICIL
    texto_dificultad = "difícil"
    ventana_nombre_jugador(texto_dificultad)
    
def ventana_nombre_jugador(dificultad):
    limpiar_ventana()
    etiqueta = tk.Label(ventana_principal, text=f"Seleccionaste la dificultad {dificultad}", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)
    
    etiqueta = tk.Label(ventana_principal, text="Ingresa tu nombre: ", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)
    
    global entry_nombre
    entry_nombre = tk.Entry(ventana_principal, width=35,
              font=("Calibri", 25),
              bd=5,
              relief="ridge")
    entry_nombre.pack(pady=10)
    
    boton_enviar = tk.Button(ventana_principal, text="Jugar", command=ventana_jugar_modo_un_jugador, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
    boton_enviar.pack(pady=10)
    
    
def ventana_jugar_modo_un_jugador():
    global nombre
    global entry_nombre
    nombre = entry_nombre.get()
    limpiar_ventana()

    etiqueta_titulo_juego = tk.Label(ventana_principal, text=f"El juego ya empezó {nombre.upper()}", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_titulo_juego.pack(pady=10)
    lista_palabras = []
    if dificultad == FACIL:
        lista_palabras = PALABRAS_FACIL
    if dificultad == NORMAL:
        lista_palabras = PALABRAS_NORMAL
    if dificultad == DIFICIL:
        lista_palabras = PALABRAS_DIFICIL
    global palabra_generada
    palabra_generada = random.choice(lista_palabras)
    global posiciones
    posiciones = "-" * len(palabra_generada)
    global etiqueta_posiciones
    etiqueta_posiciones= tk.Label(ventana_principal, text=posiciones, font=("Calibri", 60), fg='black', bg=COLOR_FONDO)
    etiqueta_posiciones.pack(pady=10)
    
    global entry_letra
    entry_letra = tk.Entry(ventana_principal,justify = "center", width=25,
              font=("Calibri", 18),
              bd=5,
              relief="ridge")
    entry_letra.pack(pady=10)

    boton_probar = tk.Button(ventana_principal, text="Probar", command=verificar, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 15),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=15)
    boton_probar.pack(pady=10)
        
    
def verificar():

    global turno_de_adivinar
    global entry_letra
    letra = entry_letra.get()
    valido = valida_letra(letra)
    if valido is True:
        global letras_ingresadas
        global oportunidades
        if oportunidades < INTENTOS_DEFINIDOS:
            letra = letra.lower()
            if letra in letras_ingresadas:
                messagebox.showinfo("Resultado","Esa letra ya fue ingresada, prueba con otra")
                entry_letra.delete(0, tk.END)

            elif letra in palabra_generada.lower():
                for i in range(len(palabra_generada)):
                    if palabra_generada[i].lower() == letra:
                        global posiciones
                        posiciones = posiciones[:i] + letra + posiciones[i+1:]
                messagebox.showinfo("Resultado", f"¡Bien hecho! {nombre} la letra es correcta")
                etiqueta_posiciones.config(text=posiciones)

                #print(f"¡Bien hecho! [{nombre}] la palabra es: {posiciones}")
                if "-" not in posiciones:
                    ventana_adivino_palabra()
                else:
                    entry_letra.delete(0, tk.END)

                    
            else:            
                oportunidades += 1
                messagebox.showinfo("Resultado", f"¡Fallaste! {nombre} la letra es incorrecta!")
                ventana_de_fallos()
                letras_ingresadas.append(letra)

      
    else:
        messagebox.showinfo("Resultado", "Debes ingresar SOLO 1 carácter diferente de un número")
        entry_letra.delete(0, tk.END)

        
def ventana_de_fallos():
    global oportunidades
    global turno_de_adivinar
    global letras_ingresadas
    limpiar_frame_fallos()
    global frame_fallos
    frame_fallos = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_fallos.pack(pady=10)
    
    if oportunidades < INTENTOS_DEFINIDOS:
        etiqueta_posiciones= tk.Label(frame_fallos, text=f"Te quedan, {INTENTOS_DEFINIDOS-oportunidades} oportunidades ", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_posiciones.pack(pady=10)
        entry_letra.delete(0, tk.END)


    if oportunidades == 1:
        imagen = tk.PhotoImage(file="Imagenes/1.png")
    elif oportunidades == 2:
        imagen = tk.PhotoImage(file="Imagenes/2.png")
    elif oportunidades == 3:
        imagen = tk.PhotoImage(file="Imagenes/3.png")
    elif oportunidades == 4:
        imagen = tk.PhotoImage(file="Imagenes/4.png")
    elif oportunidades == 5:
        imagen = tk.PhotoImage(file="Imagenes/5.png")
        limpiar_ventana()
        frame_fallos = tk.Frame(ventana_principal, bg=COLOR_FONDO)
        frame_fallos.pack(pady=10)
        etiqueta_perdio_juego = tk.Label(frame_fallos, text=f"No adivinaste la palabra {nombre.upper()}.La palabra correcta era {palabra_generada.upper()}", font=("Helvetica", 15), fg='black', bg=COLOR_FONDO)
        etiqueta_perdio_juego.pack(pady=10)
        if modo_juego == DOS_JUGADORES:
            if turno_de_adivinar == TURNO_JUGADOR_2:
                turno_de_adivinar = TURNO_JUGADOR_1
            else:
                turno_de_adivinar = FINALIZAR
            if turno_de_adivinar != FINALIZAR:
                boton_continuar = tk.Button(ventana_principal, text="Continua el siguiente jugador", command=ventana_ingresar_palabra, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
                boton_continuar.pack(pady=5)
            else:
                boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego,fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
                boton_regresar.pack(pady=5)
        
        if modo_juego == UN_JUGADOR:
            boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
            boton_regresar.pack(pady=5)
        
        
        oportunidades = 0
        letras_ingresadas = []

    imagen_label = tk.Label(frame_fallos, image = imagen) 
    imagen_label.config(width=150, height=250, borderwidth=0)  
    imagen_label.image = imagen
    imagen_label.pack()
     

def ventana_adivino_palabra():
    limpiar_ventana()
    global oportunidades
    global letras_ingresadas
    global turno_de_adivinar

    etiqueta_ganador = tk.Label(ventana_principal, text=f"Felicidades {nombre.upper()}. Acertaste la palabra es {palabra_generada.upper()}", font=("Helvetica", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_ganador.pack(pady=10)
    
    if modo_juego == UN_JUGADOR:
        boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
        boton_regresar.pack(pady=5) 
    else:
        if turno_de_adivinar == TURNO_JUGADOR_2:
            turno_de_adivinar = TURNO_JUGADOR_1
        else:
            turno_de_adivinar = FINALIZAR
        if turno_de_adivinar != FINALIZAR:
            boton_continuar = tk.Button(ventana_principal, text="Continua el siguiente jugador", command=ventana_ingresar_palabra, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 25),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
            boton_continuar.pack(pady=5)
        else:
            boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="#434141",
                bg="#82FF59",
                font=("Calibri", 20),
                relief = "groove",
                borderwidth= 3,
                cursor = "hand2",
                width=25)
            boton_regresar.pack(pady=5)


    oportunidades = 0
    letras_ingresadas = []



    
    


    
                
                
    
                
    
    
    
"""
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
    oportunidades = 0
    letras_ingresadas = []
    posiciones = "-" * len(Palabra)
    print(posiciones)
    while oportunidades < INTENTOS_DEFINIDOS:
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
            oportunidades += 1
            print("Letra incorrecta, te quedan", INTENTOS_DEFINIDOS-oportunidades, "oportunidades.")
            letras_ingresadas.append(letra)
            if oportunidades == 1:
                print("  O")
            elif oportunidades == 2:
                print("  O")
                print("  |")
            elif oportunidades == 3:
                print("  O")
                print(" /|")
            elif oportunidades == 4:
                print("  O")
                print(" /|\\")
            elif oportunidades == 5:
                print("  O")
                print(" /|\\")
                print(" / \\")
                print(f"No adivinaste la palabra [{nombre}].La palabra correcta era {Palabra}")
                break

"""

crear_ventana_principal()


"""
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
    
    
    
"""