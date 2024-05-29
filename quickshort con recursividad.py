import random
import time
from colorama import Fore, Style, init

# Inicializar colorama
init()

def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indice_particion = particion(arreglo, izquierda, derecha)
        if izquierda < indice_particion:
            quicksort(arreglo, izquierda, indice_particion)
        if indice_particion + 1 < derecha:
            quicksort(arreglo, indice_particion + 1, derecha)

def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]
    while True:
        if arreglo[izquierda] < pivote:
            izquierda += 1
        elif arreglo[derecha] > pivote:
            derecha -= 1
        elif izquierda >= derecha:
            return derecha
        else:
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            izquierda += 1
            derecha -= 1

def generar_arreglo_aleatorio(tamano, rango_min=0, rango_max=100):
    return [random.randint(rango_min, rango_max) for _ in range(tamano)]

def ejecutar_pruebas(valores_L, tamaños_N, L_index=0, N_index=0, resultados=None):
    if resultados is None:
        resultados = []

    if L_index >= len(valores_L):
        return resultados

    L = valores_L[L_index]
    N = tamaños_N[N_index]

    tiempos_ejecucion = []
    vectores_originales = []
    vectores_ordenados = []

    def realizar_pruebas(prueba=0):
        if prueba >= 5:
            tiempo_promedio = sum(tiempos_ejecucion) / len(tiempos_ejecucion)
            resultados.append((L, N, tiempo_promedio, vectores_originales, vectores_ordenados))
            print(f"Prueba con L={L}, N={N} - Tiempo promedio: {tiempo_promedio:.6f} segundos")
            
            if N_index + 1 < len(tamaños_N):
                return ejecutar_pruebas(valores_L, tamaños_N, L_index, N_index + 1, resultados)
            else:
                return ejecutar_pruebas(valores_L, tamaños_N, L_index + 1, 0, resultados)

        arreglo = generar_arreglo_aleatorio(N)
        vectores_originales.append(arreglo[:])  # Guardar el vector original
        copia_arreglo = arreglo[:]
        inicio = time.time()
        quicksort(copia_arreglo, 0, len(copia_arreglo) - 1)
        fin = time.time()
        tiempos_ejecucion.append(fin - inicio)
        vectores_ordenados.append(copia_arreglo[:])  # Guardar el vector ordenado

        return realizar_pruebas(prueba + 1)

    return realizar_pruebas()

# Configuración de los valores de L y N
valores_L = [10]
tamaños_N = [100, 200, 300, 400, 500]

# Ejecutar las pruebas
resultados_pruebas = ejecutar_pruebas(valores_L, tamaños_N)

def imprimir_resultados(resultados, index=0):
    if index >= len(resultados):
        return
    L, N, tiempo, vectores_originales, vectores_ordenados = resultados[index]
    print(f"L={L}:")
    print(f"  Para tamaño N={N}:")
    imprimir_vectores(vectores_originales, vectores_ordenados, 0)
    print(Fore.RED + f"  Tiempo promedio: {tiempo:.6f} segundos" + Style.RESET_ALL + "\n")
    imprimir_resultados(resultados, index + 1)

def imprimir_vectores(vectores_originales, vectores_ordenados, index):
    if index >= len(vectores_originales):
        return
    print(f"    Vector original {index + 1}: {vectores_originales[index]}")
    print(f"    Vector ordenado {index + 1}: {vectores_ordenados[index]}")
    imprimir_vectores(vectores_originales, vectores_ordenados, index + 1)

# Imprimir resultados finales de manera organizada
print("\nResultados finales:")
imprimir_resultados(resultados_pruebas)

