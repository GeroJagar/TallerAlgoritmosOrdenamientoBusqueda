import time
import json
import csv
import os

# --- Implementación del Algoritmo Ternary Search ---

def find_min_index(arr):
    """
    Algoritmo de búsqueda ternaria para encontrar un índice mínimo.
    Fuente: https://www.geeksforgeeks.org/dsa/ternary-search/
    """
    low = 0
    high = len(arr) - 1
    min_index = -1

    while low <= high:
        # Divide el rango en tres partes
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        # Si ambos mid1 y mid2 apuntan a valores iguales, reduce el rango
        if arr[mid1] == arr[mid2]:
            low = mid1 + 1
            high = mid2 - 1
            min_index = mid1
        
        # Si arr[mid1] < arr[mid2], el mínimo está en la parte izquierda
        elif arr[mid1] < arr[mid2]:
            high = mid2 - 1
            min_index = mid1
            
        # Si arr[mid1] > arr[mid2], el mínimo está en la parte derecha
        else:
            low = mid1 + 1
            min_index = mid2
            
    return min_index

# --- Funciones de Utilidad ---

def leer_archivo(nombre_archivo):
    """Lee el archivo .txt y retorna una lista de enteros."""
    if not os.path.exists(nombre_archivo):
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return []
    with open(nombre_archivo, 'r') as f:
        return [int(linea.strip()) for linea in f if linea.strip()]

# Lista global para simular ArchivoUtils.agregarResultadoNs
resultados_registro = []

def probar_archivo(nombre_archivo, algoritmo):
    print(f"\nProcesando: {nombre_archivo}")
    
    datos = leer_archivo(nombre_archivo)
    if not datos:
        return

    # IMPORTANTE: Al igual que la binaria, la búsqueda ternaria 
    # en este contexto requiere datos ordenados.
    datos.sort()

    # Medición de tiempo en nanosegundos
    inicio = time.perf_counter_ns()
    resultado = find_min_index(datos)
    fin = time.perf_counter_ns()

    tiempo_ns = fin - inicio
    print(f"Tiempo (ns): {tiempo_ns}")
    print(f"Índice mínimo encontrado: {resultado}")

    # Guardar resultados para exportación
    resultados_registro.append({
        "algoritmo": algoritmo,
        "archivo": nombre_archivo,
        "tiempo_ns": tiempo_ns
    })

def exportar_datos(algoritmo):
    # Exportar CSV
    with open(f"{algoritmo}.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["algoritmo", "archivo", "tiempo_ns"])
        writer.writeheader()
        writer.writerows(resultados_registro)
    
    # Exportar JSON
    with open(f"{algoritmo}.json", 'w') as f:
        json.dump(resultados_registro, f, indent=4)
    print(f"\nResultados exportados a {algoritmo}.csv y {algoritmo}.json")

# --- Bloque Principal ---

if __name__ == "__main__":
    nombre_algoritmo = "ternarysearch"
    
    # Ejecutar pruebas para los tres tamaños de archivo
    probar_archivo("archivo_10k.txt", nombre_algoritmo)
    probar_archivo("archivo_100k.txt", nombre_algoritmo)
    probar_archivo("archivo_1M.txt", nombre_algoritmo)

    # Exportar
    exportar_datos(nombre_algoritmo)
