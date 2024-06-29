## Datos del Desarrollador
Nombres y apellidos: Dave Alfonso Madrid Romero 

Universidad Internacional del Ecuador (UIDE)

Materia: Lógica de programación 1-A

### Proyecto Juego del Ahorcado

## Objetivo del proyecto
El objetivo es crear o replicar el popular juego del ahorcado en un lenguaje de programación interpretado, en este caso python 3.

## Descripción del Proyecto
Este proyecto es una reinterpretación del mítico juego del ahorcado utilizando librerías.`tkinter` utilizado para la creación de la interfaz gráfica y `PIL` o también llamado `Pillow` para las imágenes. 
El juego contiene modos de dificultad en base a la longitud de las palabras.
El juego también cuenta con un modo de dos jugadores para jugar con un amigo o con otra persona.

## Funciones del proyecto

- **Selección del modo de juego**: Al arrancar el programa, se muestra un menú con dos opciones principales: "Modo de 1 jugador" y "Modo de 2 jugadores". 
- **Modo de 1 jugador**: Primero los jugadores escriben su nombre para mostrarlo durante el juego, pueden seleccionar la dificultad deseada, `Fácil`, `Normal`, `Difícil` y dependiendo de la opción automáticamente el programa elige la palabra para jugar.
- **Modo de 2 jugadores**: Ambos jugadores pueden ingresar sus nombres al inicio, y cada uno puede ingresar una palabra para que el otro jugador la adivine, respetando turnos.
- **En caso de fallar las letras en cada modo**: Durante el juego, al ingresar una letra que no corresponde a la palabra en ambos modos, se muestra una figura que indica la cantidad de intentos restantes para adivinar.
## Fecha de creación y posiblemente de finalización
1 de Junio de 2024 hasta el 30 de Junio de 2024

## Instrucciones para Instalar o ejecutar el proyecto
1. Debes de tener las siguientes librerías para poder ejecutarlo `tkinter` en este caso ya viene por defecto en python, `PIL` o `Pillow` si no lo tienes, puedes instalarlo usando los siguientes comando:
_pip install pillow_
2. Clona este repositorio o descarga todos los archivos del programa.
3. Asegúrate de que la carpeta "imagen" contenga todas las imágenes: deben ser 5 figuras del ahorcado y 2 figuras de botones, la carpeta imagen debe estar en el mismo directorio que el código principal, de igual manera el archivo `banco_palabras.py`.
4. Ejecuta el archivo `ahorcado.py`.
