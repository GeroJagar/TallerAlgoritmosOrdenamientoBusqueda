import math
import time
import json
import csv
import os
import random

# --- Implementación del Algoritmo Jump Search ---

def jump_search(arr, x):
    """
    Algoritmo de búsqueda por saltos.
    Fuente: https://www.geeksforgeeks.org/dsa/jump-search/
    """
    n = len(arr)
    # Tamaño del bloque a saltar: raíz cuadrada de n
    step = int(math.floor(math.sqrt(n)))
    prev = 0

    # Encontrar el bloque donde el elemento está presente
    # Mientras el valor en el paso actual sea menor que x
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    # Búsqueda lineal en el bloque identificado
    while arr[prev] < x:
        prev += 1
        # Si llegamos al siguiente bloque o al final, no está
        if prev == min(step, n):
            return -1

    # Si se encuentra el elemento
    if arr[prev] == x:
        return prev

    return -1

# --- Funciones de Utilidad (Simulando ArchivoUtils) ---

def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return []
    with open(nombre_archivo, 'r') as f:
        return [int(linea.strip()) for linea in f if linea.strip()]

def generar_numero_aleatorio():
    return random.randint(10000000, 99999999)

resultados_registro = []

def probar_archivo(nombre_archivo, numero, algoritmo):
    print(f"\nProcesando: {nombre_archivo}")
    
    datos = leer_archivo(nombre_archivo)
    if not datos:
        return

    # Jump Search requiere un arreglo ordenado
    datos.sort()

    # Medición en nanosegundos (equivalente a System.nanoTime)
    inicio = time.perf_counter_ns()
    resultado = jump_search(datos, numero)
    fin = time.perf_counter_ns()

    tiempo_ns = fin - inicio
    print(f"Tiempo (ns): {tiempo_ns}")

    if resultado != -1:
        print(f"Número encontrado en posición: {resultado}")
    else:
        print("Número NO encontrado")

    resultados_registro.append({
        "algoritmo": algoritmo,
        "archivo": nombre_archivo,
        "tiempo_ns": tiempo_ns
    })

def exportar_datos(algoritmo):
    # CSV
    with open(f"{algoritmo}.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["algoritmo", "archivo", "tiempo_ns"])
        writer.writeheader()
        writer.writerows(resultados_registro)
    
    # JSON
    with open(f"{algoritmo}.json", 'w') as f:
        json.dump(resultados_registro, f, indent=4)
    print(f"\nResultados exportados a {algoritmo}.csv y {algoritmo}.json")

# --- Bloque Principal ---

if __name__ == "__main__":
    nombre_algoritmo = "jumpsearch"
    
    # Generar el número de 8 dígitos a buscar
    numero_buscado = generar_numero_aleatorio()
    print(f"Número a buscar: {numero_buscado}")

    # Pruebas con los diferentes archivos
    probar_archivo("archivo_10k.txt", numero_buscado, nombre_algoritmo)
    probar_archivo("archivo_100k.txt", numero_buscado, nombre_algoritmo)
    probar_archivo("archivo_1M.txt", numero_buscado, nombre_algoritmo)

    # Exportar resultados finales
    exportar_datos(nombre_algoritmo)
