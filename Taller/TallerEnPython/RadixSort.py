import time
import json
import csv

# --- Implementación del Algoritmo Radix Sort ---

def get_max(arr, n):
    """Obtiene el valor máximo en el arreglo."""
    mx = arr[0]
    for i in range(1, n):
        if arr[i] > mx:
            mx = arr[i]
    return mx

def count_sort(arr, n, exp):
    """
    Realiza un Counting Sort basado en el dígito 
    representado por exp (1, 10, 100, etc.)
    """
    output = [0] * n  # Arreglo de salida
    count = [0] * 10  # Inicializar conteo para dígitos (0-9)

    # Almacenar el conteo de ocurrencias en count[]
    for i in range(0, n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Cambiar count[i] para que contenga la posición real
    # de este dígito en el arreglo output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida (recorriendo en reversa para estabilidad)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiar el arreglo de salida a arr[]
    for i in range(0, n):
        arr[i] = output[i]

def radix_sort(arr, n):
    """
    Función principal de Radix Sort.
    """
    # Encontrar el máximo para saber el número de dígitos
    m = get_max(arr, n)

    # Hacer counting sort para cada dígito.
    # exp es 10^i donde i es el número del dígito actual.
    exp = 1
    while m // exp > 0:
        count_sort(arr, n, exp)
        exp *= 10

# --- Simulación de ArchivoUtils ---

class ArchivoUtils:
    resultados = []

    @staticmethod
    def medir_tiempo(nombre_archivo, nombre_algoritmo, func, datos):
        print(f"Ejecutando {nombre_algoritmo} para {nombre_archivo}...")
        inicio = time.time()
        # Llamamos a radix_sort pasando el arreglo y su longitud
        func(datos, len(datos))
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
    
    # Simulación de carga de datos
    datos_10k = [random.randint(0, 50000) for _ in range(10000)]
    datos_100k = [random.randint(0, 50000) for _ in range(100000)]
    datos_1M = [random.randint(0, 50000) for _ in range(1000000)]

    # Pruebas
    ArchivoUtils.medir_tiempo("archivo_10k.txt", "Radix Sort", radix_sort, datos_10k)
    ArchivoUtils.medir_tiempo("archivo_100k.txt", "Radix Sort", radix_sort, datos_100k)
    ArchivoUtils.medir_tiempo("archivo_1M.txt", "Radix Sort", radix_sort, datos_1M)
    
    # Exportación
    ArchivoUtils.exportar_csv("Radix Sort")
    ArchivoUtils.exportar_json("Radix Sort")
