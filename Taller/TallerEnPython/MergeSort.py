import time
import json
import csv

# --- Implementación del Algoritmo Merge Sort ---

def merge(arr, l, m, r):
    """
    Mezcla dos subarreglos de arr[].
    Primer subarreglo es arr[l..m]
    Segundo subarreglo es arr[m+1..r]
    """
    n1 = m - l + 1
    n2 = r - m

    # Crear arreglos temporales
    # En Python, el slicing facilita esto, pero para mantener la fidelidad:
    L = [0] * n1
    R = [0] * n2

    # Copiar datos a los arreglos temporales
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Índices iniciales de los subarreglos y del arreglo mezclado
    i = 0  # Índice inicial del primer subarreglo
    j = 0  # Índice inicial del segundo subarreglo
    k = l  # Índice inicial del arreglo mezclado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar elementos restantes de L[] si quedan
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar elementos restantes de R[] si quedan
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    """
    Función principal que ordena arr[l..r] usando merge()
    """
    if l < r:
        # Equivalente a int m = l + (r - l) / 2;
        m = l + (r - l) // 2

        # Ordenar primera y segunda mitad
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        # Mezclar las mitades ordenadas
        merge(arr, l, m, r)

# --- Simulación de ArchivoUtils ---

class ArchivoUtils:
    resultados = []

    @staticmethod
    def medir_tiempo(nombre_archivo, nombre_algoritmo, func, datos):
        print(f"Ejecutando {nombre_algoritmo} para {nombre_archivo}...")
        inicio = time.time()
        # Llamamos a la función (merge_sort requiere l y r)
        func(datos, 0, len(datos) - 1)
        fin = time.time()
        
        tiempo_ms = (fin - inicio) * 1000
        ArchivoUtils.resultados.append({
            "archivo": nombre_archivo,
            "algoritmo": nombre_algoritmo,
            "tiempo_ms": tiempo_ms
        })
        print(f"Completado en: {tiempo_ms:.2f} ms")

    @staticmethod
    def exportar_csv(nombre_algoritmo):
        filename = f"{nombre_algoritmo.replace(' ', '_')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["archivo", "algoritmo", "tiempo_ms"])
            writer.writeheader()
            writer.writerows(ArchivoUtils.resultados)
        print(f"Resultados exportados a {filename}")

    @staticmethod
    def exportar_json(nombre_algoritmo):
        filename = f"{nombre_algoritmo.replace(' ', '_')}.json"
        with open(filename, 'w') as f:
            json.dump(ArchivoUtils.resultados, f, indent=4)
        print(f"Resultados exportados a {filename}")

# --- Ejecución Principal ---

if __name__ == "__main__":
    import random
    import sys
    
    # Aumentar límite de recursión para 1M si es necesario
    sys.setrecursionlimit(2000)

    # Simulación de datos
    datos_10k = [random.randint(0, 10000) for _ in range(10000)]
    datos_100k = [random.randint(0, 100000) for _ in range(100000)]

    # Pruebas
    ArchivoUtils.medir_tiempo("archivo_10k.txt", "Merge Sort", merge_sort, datos_10k)
    ArchivoUtils.medir_tiempo("archivo_100k.txt", "Merge Sort", merge_sort, datos_100k)
    
    # Exportación
    ArchivoUtils.exportar_csv("Merge Sort")
    ArchivoUtils.exportar_json("Merge Sort")
