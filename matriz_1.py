'''
## Enunciado 1: Suma de dos matrices
Elabore un programa en Python que reciba dos matrices de igual tamaño (número de
filas y columnas) ingresadas por el usuario, y calcule la matriz resultante de
sumar elemento a elemento ambas matrices. El programa debe imprimir la matriz
resultante con un formato ordenado (filas y columnas alineadas).
**Consideraciones:**
- Solicite primero el número de filas y columnas.
- Valide que ambas matrices tengan las mismas dimensiones antes de sumarlas.
- Muestre un mensaje de error si las dimensiones no coinciden.
'''

def leer_matriz(nombre):
    filas = int(input(f"Filas de {nombre}: "))
    columnas = int(input(f"Columnas de {nombre}: "))

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"  {nombre}[{i}][{j}]: ")))
        matriz.append(fila)

    return matriz, filas, columnas


def imprimir_matriz(matriz, filas, columnas):
    # Ancho = largo del número más largo, para alinear columnas
    ancho = 0
    for i in range(filas):
        for j in range(columnas):
            largo = len(str(matriz[i][j]))
            if largo > ancho:
                ancho = largo

    for i in range(filas):
        linea = ""
        for j in range(columnas):
            texto = str(matriz[i][j])
            # Agrega espacios a la izquierda hasta llegar al ancho + 2
            while len(texto) < ancho + 2:
                texto = " " + texto
            linea += texto
        print(linea)


A, filas_a, columnas_a = leer_matriz("A")
B, filas_b, columnas_b = leer_matriz("B")

if filas_a != filas_b or columnas_a != columnas_b:
    print("Error: las matrices deben tener las mismas dimensiones.")
else:
    suma = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(A[i][j] + B[i][j])
        suma.append(fila)

    print("Matriz resultante:")
    imprimir_matriz(suma, filas_a, columnas_a)

'''
Cómo funciona:

leer_matriz devuelve la matriz y sus dimensiones, así se pueden comparar después. Pedirlas antes de leer los elementos también evita que el usuario llene una matriz entera para descubrir luego el error. [Cierto]
En imprimir_matriz, ancho es el largo del número más largo. rjust(ancho + 2) rellena con espacios a la izquierda para que todas las columnas queden alineadas a la derecha. [Cierto]
'''