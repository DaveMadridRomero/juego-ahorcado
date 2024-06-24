import tkinter as tk
from tkinter import messagebox

ventana_principal = None
entry_nombre = None
          
def crear_ventana_principal():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Juego del ahorcado")
    ventana_principal.geometry("640x480")
    ventana_principal.configure(bg='lightblue')
    
    #menu modo de juego
    menu_modo_juego()
    ventana_principal.mainloop()
    

def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()
  

# Funciones de los botones
def modo_1_jugador():
    messagebox.showinfo("modo_1_jugador", "¡Botón 1 presionado!")

def modo_2_jugadores():
    messagebox.showinfo("modo_2_jugadores", "¡Botón 2 presionado!")


def menu_modo_juego():
    limpiar_ventana()
    etiqueta = tk.Label(ventana_principal, text="¡Bienvenido al juego del ahorcado!", font=("Helvetica", 24), bg='lightblue')
    etiqueta.pack(pady=20)
    
    frame = tk.Frame(ventana_principal, bg='lightblue')
    frame.pack(pady=20)
    
    etiqueta = tk.Label(frame, text="Modo de juego", font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)

    # Botón 1
    boton_1 = tk.Button(frame, text="Un jugador", command=menu_seleccion_dificultad, font=("Helvetica", 14), width=15)
    boton_1.pack(pady=5)

    # Botón 2
    boton_2 = tk.Button(frame, text="Dos jugadores", command=modo_2_jugadores, font=("Helvetica", 14), width=15)
    boton_2.pack(pady=5)
    
    

def menu_seleccion_dificultad():
    limpiar_ventana()
    frame = tk.Frame(ventana_principal, bg='lightblue')
    frame.pack(pady=20)  
    
    etiqueta = tk.Label(frame, text="Modos de dificultad", font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)

    # Botón 1
    boton_1 = tk.Button(frame, text="Fácil", command=jugar_facil, font=("Helvetica", 14), width=15)
    boton_1.pack(pady=5)

    # Botón 2
    boton_2 = tk.Button(frame, text="Normal", command=modo_2_jugadores, font=("Helvetica", 14), width=15)
    boton_2.pack(pady=5)
    
    boton_3 = tk.Button(frame, text="Difícil", command=modo_1_jugador, font=("Helvetica", 14), width=15)
    boton_3.pack(pady=5)
    
    boton_regresar = tk.Button(frame, text="Regresar", command=menu_modo_juego, font=("Helvetica", 14), width=15)
    boton_regresar.pack(pady=5)
      
    
def jugar_facil():
    limpiar_ventana()
    
    frame = tk.Frame(ventana_principal, bg='lightblue')
    frame.pack(pady=20)
    
    etiqueta = tk.Label(frame, text="Seleccionaste la dificultad fácil", font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)
    
    etiqueta = tk.Label(frame, text="Ingresa tu nombre: ", font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)
    
    global entry_nombre
    entry_nombre = tk.Entry(frame, width=30, font=("Helvetica", 14))
    entry_nombre.pack(pady=10)
    
    boton_enviar = tk.Button(frame, text="Jugar", command=jugar, font=("Helvetica", 15))
    boton_enviar.pack(pady=10)
    
    
    
def jugar():
    nombre = entry_nombre.get()
    print(nombre)
    limpiar_ventana()
    
    frame = tk.Frame(ventana_principal, bg='lightblue')
    frame.pack(pady=20)
    
    etiqueta = tk.Label(frame, text="El juego ya empezó", font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)
    
    etiqueta = tk.Label(frame, text=palabra, font=("Helvetica", 24), fg='black')
    etiqueta.pack(pady=10)
    
    
    
    
    
    
    
    
    
        

    
    

    
    
    
