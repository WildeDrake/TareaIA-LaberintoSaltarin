# Tarea IA - Laberito Saltarin

Un laberinto saltarín se define como una grilla de m por n de números saltarines, una celda
inicial (en un círculo arriba), y una celda de destino (marcada “0”). En base al número
saltarín de cada celda, un movimiento corresponde a moverse esa cantidad exacta de
celdas ya sea de forma horizontal o vertical, en línea recta. No está permitido moverse de
manera diagonal ni cambiar de dirección a medio camino. Sólo se permiten movimientos en
que el número de celdas a mover no sobrepasa alguno de los límites del laberinto. El
objetivo del laberinto saltarín es encontrar el camino más corto, es decir, la menor cantidad
de movimientos desde la celda inicial hasta la celda de destino.

En esta implementación, dado que buscamos encontrar la mejor solución, es decir, el camino más 
corto entre la celda inicial y la celda de destino, se implementaron dos algoritmos de búsqueda,
DFS y BFS. En el caso de DFS, se implementó de modo que se recorran todas las posibles rutas,
puesto que no podemos saber en qué momento encontramos la solución óptima, al contrario que en
BFS, que, al ser un recorrido en anchura, la primera solución encontrada será óptima.


## Ejecutar con:
python main.py --filename FILENAME --m M --n N --modo MODO
- FILENAME: Un string para el argumento filename. Es el nombre del archivo de texto que contiene el
laberinto. El archivo debe estar en la carpeta `Laberinto`.
- M: Un entero para el argumento m. Es el número de filas del laberinto.
- N: Un entero para el argumento n. Es el número de columnas del laberinto.
- MODO: Un entero para el argumento modo. Es el modo de ejecución del programa.
  - 0: El usuario podra jugar con las teclas de flecha o wasd.
  - 1: Se ejecutará el laberinto, pero será resuelto por DFS.
  - 2: Se ejecutará el laberinto, pero será resuelto por BFS.
  - 3: No ejecuta el laberinto, pero compara a ámbos métodos.

Si se ejecuta el programa con el argumento *filename* no se podran utilizar los argumentos *m*, *n*
y viceversa, además, si utilizamos *m* y *n*, el laberinto es creado totalmente aleatorio.


## Requerimientos:
- Python 3.8.2
- Pygame 2.5.2