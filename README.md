## Datos del Desarrollador
Nombres y apellidos: Dave Alfonso Madrid Romero
Universidad Internacional del Ecuador (UIDE)
Materia: Lógica de programación 1-A

### Proyecto Juego del Ahorcado

## Objetivo del proyecto
El objetivo es crear o replicar el popular juego del ahorcado en un lenguaje de programación interpretado, en este caso python 3.

## Descripción del Proyecto
Este proyecto es una reinterpretación del mitico juego del ahorcado utilizandos librerías.`tkinter` y `PIL` o también llamado `Pillow`. 
El juego contiene modos de dificultad en base a la longitud de las palabras.
El juego también cuenta con un modo de dos jugadores para jugar con un amigo o con otra persona.

## Funciones del proyecto

- **Selección del modo de juego**: Al arrancar el programa, se muestra el menú con dos opciones principales: "Modo de 1 jugador" y "Modo de 2 jugadores". 
- **Modo de 1 jugador**: Primero los jugadores escriben su nombre para mostrarlo durante el juego, pueden seleccionar la dificultad deseada, `Fácil`, `Normal`, `Difícil` y dependiendo de la opción automáticamente el programa elige la palabra para poder jugar.
- **Modo de 2 jugadores**: Si seleccionan este modo ambos jugadores pueden ingresar los nombres para mostrarlo en el juego, cada uno puede ingresar su palabra para que el otro jugador la pueda adivinar, respetando el turno de cada jugador.
- **En caso de fallar las letras en cada modo**: Durante el juego se puede fallar, al momento de ingresar una letra no correspondiente a la palabra en ambos modos, lo cual genera una figura que avisa al jugador la cantidad de intentos que le quedan para poder adivinar o acertar.

## Fecha de creación y posiblemente de finalización
1 de Junio de 2024 hasta el 30 de Junio de 2024

## Instrucciones para Instalar o ejecutar el proyecto
1. Debes de tener las siguientes librerías para poder ejecutarlo `tkinter` en este caso ya viene por defecto en python, `PIL` o `Pillow` si no lo tienes, puedes instalarlo usando los siguientes comando:
_pip install pillow_
2. Clona este repositorio o descarga todos los archivos del programa.
3. Asegurate de que la carpeta imagen contenga todas las imagenes, deben ser 5 figuras del ahorcado y 2 figuras de botones, en el mismo directorio que el código principal.
4. Ejecuta el archivo ahorcado.py
