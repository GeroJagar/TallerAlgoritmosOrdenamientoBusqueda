# Suponiendo que tienes un módulo llamado archivo_utils
from archivo_utils import ArchivoUtils

def heapify(arr, n, i):
    """
    Mantiene la propiedad de Max-Heap en un subárbol con raíz en el índice i.
    Fuente: https://www.geeksforgeeks.org/dsa/heap-sort/
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Si el hijo izquierdo es más grande que la raíz
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Si el hijo derecho es más grande que el más grande hasta ahora
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Si el más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap elegante en Python

        # Heapify recursivo en el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Función principal para realizar Heap Sort.
    """
    n = len(arr)

    # Construir el heap (reorganizar el array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        # Mover la raíz actual al final
        arr[0], arr[i] = arr[i], arr[0]

        # Llamar a max heapify en el heap reducido
        heapify(arr, i, 0)

def main():
    # Ejecución de mediciones
    # Nota: En Python, pasamos la función directamente como argumento
    ArchivoUtils.medir_tiempo("archivo_10k.txt", "Heap Sort", heap_sort)
    ArchivoUtils.medir_tiempo("archivo_100k.txt", "Heap Sort", heap_sort)
    ArchivoUtils.medir_tiempo("archivo_1M.txt", "Heap Sort", heap_sort)
    
    # Exportación de resultados
    ArchivoUtils.exportar_csv("Heap Sort")
    ArchivoUtils.exportar_json("Heap Sort")

if __name__ == "__main__":
    main()
