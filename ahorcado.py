#importar Librerias para el correcto funcionamiento del juego
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from banco_palabras import BANCO_FACIL
from banco_palabras import BANCO_NORMAL
from banco_palabras import BANCO_DIFICIL

#Definir constantes 
COLOR_FONDO = "white"
UN_JUGADOR = 1
DOS_JUGADORES = 2
TURNO_JUGADOR_1 = 1
TURNO_JUGADOR_2 = 2
FINALIZAR = 3
FACIL = 1
NORMAL = 2
DIFICIL = 3
PALABRAS_FACIL = BANCO_FACIL
PALABRAS_NORMAL = BANCO_NORMAL
PALABRAS_DIFICIL = BANCO_DIFICIL
INTENTOS_DEFINIDOS = 5

#Definir las variables
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

#Función para validar las letras que ingresa el usuario
def valida_letra(entry_letra_ingresado):
    if len(entry_letra_ingresado) == 1 and entry_letra_ingresado.isalpha():
        return True
    else:
        return False
#Función para validar la palabra que ingresa el usuario
def validar_palabra(entry_palabra_ingresada):
    if len(entry_palabra_ingresada) >= 1 and entry_palabra_ingresada.isalpha():
        return True
    else:
        return False
#Función para centrar la ventana al iniciar el juego
def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    ventana.geometry(f"{width}x{height}+{x}+{y}")
#Función para crear la ventana principal del juego
def crear_ventana_principal():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Juego del ahorcado")
    ventana_principal.geometry("800x600")
    ventana_principal.configure(bg=COLOR_FONDO)
    centrar_ventana(ventana_principal)
    #menu modo de juego
    menu_modo_juego()
    
    ventana_principal.mainloop()
#Función para limpiar la ventana cuando se eligen las opciones
def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()
#Función para limpiar partes especificas de la ventana cuando se eligen opciones  
def limpiar_frame_fallos():
    if frame_fallos and frame_fallos.winfo_exists():
        for widget in frame_fallos.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
        frame_fallos.destroy()

#Funciones para agregar imágenes a todos los botones del menú principal
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

def imagen_boton_continuar_juego():
    imagen_original = Image.open("Imagenes/boton_play.png")
    nueva_imagen = imagen_original.resize((370, 60))
    imagen = ImageTk.PhotoImage(nueva_imagen)
    return imagen

#Función para mostrar un ahorcado en el menú principal
def imagen_ahorcado():
    imagen_original = Image.open("Imagenes/hangman.png")
    nueva_imagen = imagen_original.resize((120, 140))
    imagen = ImageTk.PhotoImage(nueva_imagen)
    return imagen

#Función para crear el menú principal del juego
def menu_modo_juego():
    limpiar_ventana()
    
    etiqueta = tk.Label(ventana_principal, text="Bienvenido al juego del ahorcado", font=("Times New Roman", 35), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady= 30)
    
    imagen_ahorcado_principal = imagen_ahorcado()
    imagen_label = tk.Label(ventana_principal, image = imagen_ahorcado_principal) 
    imagen_label.image = imagen_ahorcado_principal
    imagen_label.pack()
    
    etiqueta = tk.Label(ventana_principal, text="Modos de juego", font=("Times New Roman", 35), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady= 30)
    imagen = imagen_boton_menu_juego()
    
    boton_1 = tk.Button(ventana_principal, text="Un jugador", command=menu_seleccion_dificultad, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_1.pack(pady=15)
    boton_1.image = imagen

    boton_2 = tk.Button(ventana_principal, text="Dos jugadores", command=ventana_dos_jugadores,fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_2.pack(pady=15)
    boton_2.image = imagen
#Función para crear el menú al momento de seleccionar modo de 2 jugadores        
def ventana_dos_jugadores():
    limpiar_ventana()
    global modo_juego
    global entry_nombre_j1
    global entry_nombre_j2
    global turno_de_adivinar
    modo_juego = DOS_JUGADORES
    turno_de_adivinar = TURNO_JUGADOR_2
    etiqueta_j1 = tk.Label(ventana_principal, text="Ingrese su nombre jugador 1", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_j1.pack(pady=20)
    entry_nombre_j1= tk.Entry(ventana_principal, width=35,font=("Times New Roman", 25),bd=5,relief="ridge")
    entry_nombre_j1.pack(pady=15)
    
    etiqueta_j2= tk.Label(ventana_principal, text="Ingrese su nombre jugador 2", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_j2.pack(pady=10)
    entry_nombre_j2= tk.Entry(ventana_principal, width=35,font=("Times New Roman", 25),bd=5,relief="ridge")
    entry_nombre_j2.pack(pady=10)

    imagen = imagen_boton_jugar_juego()
    boton_jugar = tk.Button(ventana_principal, text="Comenzar", command=ventana_ingresar_palabra, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=150, height=60)
    boton_jugar.pack(pady=10)
    boton_jugar.imagen = imagen

#Función para crear el menú al momento de ingresar la palabra para ambos jugadores
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
    imagen = imagen_boton_jugar_juego()
    if turno_de_adivinar == TURNO_JUGADOR_2:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Ingrese su palabra {nombre_1.upper()} ", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        entry_palabra = tk.Entry(ventana_principal, width=35,font=("Times New Roman", 25),bd=5,relief="ridge",justify='center',show="*")
        entry_palabra.pack(pady=10)
        boton_jugar_1 = tk.Button(ventana_principal, text="Jugar", command=palabra_jugadores, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=150, height=60)
        boton_jugar_1.pack(pady=10)
        boton_jugar_1.image = imagen
    if turno_de_adivinar == TURNO_JUGADOR_1:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Ingrese su palabra {nombre_2.upper()} ", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        entry_palabra = tk.Entry(ventana_principal, width=35,font=("Times New Roman", 25),bd=5,relief="ridge",justify='center',show="*")
        entry_palabra.pack(pady=10)
        boton_jugar_2 = tk.Button(ventana_principal, text="Jugar", command=palabra_jugadores, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=150, height=60)
        boton_jugar_2.pack(pady=10)
        boton_jugar_2.image = imagen
    if turno_de_adivinar == FINALIZAR:
        etiqueta_palabra = tk.Label(ventana_principal, text=f"Juego terminado",font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_palabra.pack(pady=10)
        imagen = imagen_boton_menu_juego()
        boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
        boton_regresar.pack(pady=5)
        boton_regresar.image = imagen

#Función para obtener y guardar la palabra que los jugadores ingresaron   
def palabra_jugadores():
    global palabra_generada
    global entry_palabra
    palabra_generada = entry_palabra.get()
    palabra_valida = validar_palabra(palabra_generada)
    if palabra_valida:
        ventana_jugar_dos_jugadores()
    else:
        messagebox.showinfo("Resultado", "Debes ingresar al menos 1 carácter diferente de un número")
        entry_palabra.delete(0, tk.END)
        
#Función para crear la ventana donde adivinaran la letra ambos jugadores   
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

    etiqueta_titulo_juego = tk.Label(ventana_principal, text=f"El juego ya empezó, adivina la palabra {nombre}", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_titulo_juego.pack(pady=10)
    posiciones = "-" * len(palabra_generada)
    etiqueta_posiciones= tk.Label(ventana_principal, text=posiciones, font=("Times New Roman", 35), fg='black', bg=COLOR_FONDO)
    etiqueta_posiciones.pack(pady=10)
    
    entry_letra = tk.Entry(ventana_principal, width=25,font=("Times New Roman", 18),bd=5,justify = "center",relief="ridge")
    entry_letra.pack(pady=10)
    imagen = imagen_boton_jugar_juego()
    boton_probar = tk.Button(ventana_principal, text="Probar", command=verificar, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat", width=150, height=60)
    boton_probar.pack(pady=10)   
    boton_probar.image = imagen

#Función para crear la ventana de la selección de dificultad
def menu_seleccion_dificultad():
    limpiar_ventana()
    global modo_juego
    modo_juego = UN_JUGADOR
    etiqueta = tk.Label(ventana_principal, text="Modos de dificultad", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)

    imagen = imagen_boton_menu_juego()    
    boton_1 = tk.Button(ventana_principal, text="Fácil", command=jugar_facil, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_1.pack(pady=15)
    boton_1.image = imagen

    boton_2 = tk.Button(ventana_principal, text="Normal", command=jugar_normal, bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_2.pack(pady=15)
    boton_2.image = imagen
    
    boton_3 = tk.Button(ventana_principal, text="Difícil", command=jugar_dificil, bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_3.pack(pady=15)
    boton_3.image = imagen
    
    boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
    boton_regresar.pack(pady=15)
    boton_regresar.image = imagen
      
#Función para eligir las palabras de la dificultad fácil    
def jugar_facil():
    global dificultad
    dificultad = FACIL
    texto_dificultad = "fácil"
    ventana_nombre_jugador(texto_dificultad)
    
#Función para eligir las palabras de la dificultad normal        
def jugar_normal():
    global dificultad
    dificultad = NORMAL
    texto_dificultad = "normal"
    ventana_nombre_jugador(texto_dificultad)

#Función para eligir las palabras de la dificultad difícil
def jugar_dificil():
    global dificultad
    dificultad = DIFICIL
    texto_dificultad = "difícil"
    ventana_nombre_jugador(texto_dificultad)
#Función para crear la ventana donde ingresar el nombre del modo de un jugador
def ventana_nombre_jugador(dificultad):
    limpiar_ventana()
    etiqueta = tk.Label(ventana_principal, text=f"Seleccionaste la dificultad {dificultad}", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)
    
    etiqueta = tk.Label(ventana_principal, text="Ingresa tu nombre: ", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta.pack(pady=10)
    
    global entry_nombre
    entry_nombre = tk.Entry(ventana_principal, width=35,font=("Times New Roman", 25),bd=5,relief="ridge")
    entry_nombre.pack(pady=10)
    imagen = imagen_boton_jugar_juego()
    boton_enviar = tk.Button(ventana_principal, text="Jugar", command=ventana_jugar_modo_un_jugador, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=150, height=60)
    boton_enviar.pack(pady=10)
    boton_enviar.image = imagen
    
#Función para crear la ventana de juego de un jugador   
def ventana_jugar_modo_un_jugador():
    global nombre
    global entry_nombre
    nombre = entry_nombre.get()
    limpiar_ventana()

    etiqueta_titulo_juego = tk.Label(ventana_principal, text=f"El juego ya empezó {nombre.upper()}", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
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
    etiqueta_posiciones= tk.Label(ventana_principal, text=posiciones, font=("Times New Roman", 60), fg='black', bg=COLOR_FONDO)
    etiqueta_posiciones.pack(pady=10)
    
    global entry_letra
    entry_letra = tk.Entry(ventana_principal,justify = "center", width=25,font=("Times New Roman", 18),bd=5,relief="ridge")
    entry_letra.pack(pady=10)
    imagen = imagen_boton_jugar_juego()
    boton_probar = tk.Button(ventana_principal, text="Probar", command=verificar, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=150, height=60)
    boton_probar.pack(pady=10)
    boton_probar.image = imagen
        
#Función para verificar todo el proceso de las letras, si ya fue ingresada, si es correcta o incorrecta o si lo introducido es válido.   
def verificar():

    global turno_de_adivinar
    global entry_letra
    letra = entry_letra.get()
    valido = valida_letra(letra)
    if valido is True:
        global letras_ingresadas
        print("letras ingresadas")
        print(letras_ingresadas)
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
                    oportunidades = 0
                    letras_ingresadas = []
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

#Función para verificar todos los fallos y la generación de la figura del ahorcado        
def ventana_de_fallos():
    global oportunidades
    global turno_de_adivinar
    global letras_ingresadas
    limpiar_frame_fallos()
    global frame_fallos
    frame_fallos = tk.Frame(ventana_principal, bg=COLOR_FONDO)
    frame_fallos.pack(pady=10)
    
    if oportunidades < INTENTOS_DEFINIDOS:
        etiqueta_posiciones= tk.Label(frame_fallos, text=f"Te quedan, {INTENTOS_DEFINIDOS-oportunidades} oportunidades ", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
        etiqueta_posiciones.pack(pady=10)
        entry_letra.delete(0, tk.END)

    if oportunidades == 1:
        imagen_ahorcado = tk.PhotoImage(file="Imagenes/1.png")
    elif oportunidades == 2:
        imagen_ahorcado = tk.PhotoImage(file="Imagenes/2.png")
    elif oportunidades == 3:
        imagen_ahorcado = tk.PhotoImage(file="Imagenes/3.png")
    elif oportunidades == 4:
        imagen_ahorcado = tk.PhotoImage(file="Imagenes/4.png")
    elif oportunidades == 5:
        imagen_ahorcado = tk.PhotoImage(file="Imagenes/5.png")
        limpiar_ventana()
        frame_fallos = tk.Frame(ventana_principal, bg=COLOR_FONDO)
        frame_fallos.pack(pady=10)
        etiqueta_perdio_juego = tk.Label(frame_fallos, text=f"No adivinaste la palabra {nombre.upper()}.La palabra correcta era {palabra_generada.upper()}", font=("Times New Roman", 15), fg='black', bg=COLOR_FONDO)
        etiqueta_perdio_juego.pack(pady=10)
        if modo_juego == DOS_JUGADORES:
            if turno_de_adivinar == TURNO_JUGADOR_2:
                turno_de_adivinar = TURNO_JUGADOR_1
            else:
                turno_de_adivinar = FINALIZAR
            if turno_de_adivinar != FINALIZAR:
                imagen = imagen_boton_continuar_juego()
                boton_continuar = tk.Button(ventana_principal, text="Continua el siguiente jugador", command=ventana_ingresar_palabra, fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center",relief="flat",width=370, height=60)     
                boton_continuar.image = imagen
                boton_continuar.pack(pady=5)
            else:
                imagen = imagen_boton_menu_juego()
                boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego,fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
                boton_regresar.image = imagen
                boton_regresar.pack(pady=5)
        
        if modo_juego == UN_JUGADOR:
            imagen = imagen_boton_menu_juego()
            boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
            boton_regresar.image = imagen
            boton_regresar.pack(pady=5)
            
        oportunidades = 0
        letras_ingresadas = []

    imagen_label = tk.Label(frame_fallos, image = imagen_ahorcado) 
    imagen_label.config(width=150, height=250, borderwidth=0)  
    imagen_label.image = imagen_ahorcado
    imagen_label.pack()
    
#Función para cuando ya se adivine la palabra, tanto del modo de un jugador como el de dos jugadores
def ventana_adivino_palabra():
    limpiar_ventana()
    global oportunidades
    global letras_ingresadas
    global turno_de_adivinar

    etiqueta_ganador = tk.Label(ventana_principal, text=f"Felicidades {nombre.upper()}. Acertaste la palabra es {palabra_generada.upper()}", font=("Times New Roman", 24), fg='black', bg=COLOR_FONDO)
    etiqueta_ganador.pack(pady=10)
    
    if modo_juego == UN_JUGADOR:
        imagen = imagen_boton_menu_juego()
        boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20),image = imagen,cursor="hand2",compound="center",relief="flat",width=300, height=60)
        boton_regresar.pack(pady=5)
        boton_regresar.image = imagen
        
    else:
        if turno_de_adivinar == TURNO_JUGADOR_2:
            turno_de_adivinar = TURNO_JUGADOR_1
        else:
            turno_de_adivinar = FINALIZAR
        if turno_de_adivinar != FINALIZAR:
            imagen = imagen_boton_continuar_juego()
            boton_continuar = tk.Button(ventana_principal, text="Continua el siguiente jugador", command=ventana_ingresar_palabra,fg="#434141",bg=COLOR_FONDO,font=("Times New Roman", 20),image=imagen,cursor="hand2",compound="center", relief="flat",width=370, height=60)
            boton_continuar.pack(pady=5)
            boton_continuar.image = imagen
        else:
            imagen = imagen_boton_menu_juego()
            boton_regresar = tk.Button(ventana_principal, text="Regresar", command=menu_modo_juego, fg="black",bg=COLOR_FONDO,font=("Times New Roman", 20), image = imagen, cursor="hand2", compound="center", relief="flat", width=300, height=60)
            boton_regresar.pack(pady = 5)
            boton_regresar.image = imagen
            
    oportunidades = 0
    letras_ingresadas = []
    
#inicio del programa
crear_ventana_principal()

    
                
                
    
                
    
    
    
