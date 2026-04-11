import json
import csv
import time

# --- Simulación de ArchivoUtils (Para que el código funcione) ---
class ArchivoUtils:
    resultados = []

    @staticmethod
    def medir_tiempo(nombre_archivo, algoritmo, func, arr):
        print(f"Procesando {nombre_archivo}...")
        inicio = time.time()
        func(arr, 0, len(arr) - 1)
        fin = time.time()
        duracion = (fin - inicio) * 1000  # Convertir a milisegundos
        
        ArchivoUtils.resultados.append({
            "archivo": nombre_archivo,
            "algoritmo": algoritmo,
            "tiempo_ms": duracion
        })
        print(f"Tiempo: {duracion:.2f} ms")

    @staticmethod
    def exportar_csv(nombre_algoritmo):
        filename = f"{nombre_algoritmo.replace(' ', '_')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["archivo", "algoritmo", "tiempo_ms"])
            writer.writeheader()
            writer.writerows(ArchivoUtils.resultados)
        print(f"Exportado a {filename}")

    @staticmethod
    def exportar_json(nombre_algoritmo):
        filename = f"{nombre_algoritmo.replace(' ', '_')}.json"
        with open(filename, 'w') as f:
            json.dump(ArchivoUtils.resultados, f, indent=4)
        print(f"Exportado a {filename}")


# --- Implementación del Dual-Pivot Quicksort ---

def swap(arr, i, j):
    """Intercambia dos elementos en la lista."""
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    """
    Particiona el arreglo usando dos pivotes.
    Retorna los índices finales de ambos pivotes.
    """
    if arr[low] > arr[high]:
        swap(arr, low, high)
        
    # p es el pivote izquierdo, q es el derecho
    j = low + 1
    g = high - 1
    k = low + 1
    p = arr[low]
    q = arr[high]
    
    while k <= g:
        # Si el elemento es menor que el pivote izquierdo
        if arr[k] < p:
            swap(arr, k, j)
            j += 1
        
        # Si el elemento es mayor o igual al pivote derecho
        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1
            
            swap(arr, k, g)
            g -= 1
            
            if arr[k] < p:
                swap(arr, k, j)
                j += 1
        k += 1
    
    j -= 1
    g += 1
    
    # Coloca los pivotes en sus posiciones correctas
    swap(arr, low, j)
    swap(arr, high, g)
    
    return j, g

def dual_pivot_quick_sort(arr, low, high):
    """Algoritmo principal recursivo."""
    if low < high:
        # piv[0] es el pivote izquierdo, piv[1] el derecho
        lp, rp = partition(arr, low, high)
        
        dual_pivot_quick_sort(arr, low, lp - 1)
        dual_pivot_quick_sort(arr, lp + 1, rp - 1)
        dual_pivot_quick_sort(arr, rp + 1, high)

# --- Método Main (Ejecución) ---

if __name__ == "__main__":
    # Generar datos de prueba (en lugar de leer archivos reales para este ejemplo)
    import random
    arr_10k = [random.randint(0, 10000) for _ in range(10000)]
    arr_100k = [random.randint(0, 100000) for _ in range(100000)]
    
    # Simulación de las llamadas originales
    ArchivoUtils.medir_tiempo("archivo_10k.txt", "Dual-Pivot Quicksort", dual_pivot_quick_sort, arr_10k)
    ArchivoUtils.medir_tiempo("archivo_100k.txt", "Dual-Pivot Quicksort", dual_pivot_quick_sort, arr_100k)
    
    # Nota: Para 1M en Python, podrías exceder el límite de recursión.
    # Se puede ajustar con: import sys; sys.setrecursionlimit(2000)
    
    ArchivoUtils.exportar_csv("Dual-Pivot Quicksort")
    ArchivoUtils.exportar_json("Dual-Pivot Quicksort")
