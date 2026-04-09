from archivo_utils import ArchivoUtils  # Asumiendo que guardaste el código anterior como archivo_utils.py

class Shaker:
    """
    Esta clase implementa el método de la sacudida o Shaker Sort.
    Autor original Java: leon
    """

    @staticmethod
    def shaker(arreglo):
        """
        El método que ordena mediante la sacudida.
        :param arreglo: La lista a ordenar.
        :return: La lista ya ordenada.
        """
        intercambios = 0
        comparaciones = 0
        n = len(arreglo)
        
        izq = 1
        der = n - 1
        k = n - 1

        while izq <= der:
            # Fase 1: Derecha a izquierda (mueve el menor al principio)
            for i in range(der, izq - 1, -1):
                comparaciones += 1
                if arreglo[i - 1] > arreglo[i]:
                    intercambios += 1
                    arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1] # Swap elegante de Python
                    k = i
            
            izq = k + 1

            # Fase 2: Izquierda a derecha (mueve el mayor al final)
            for i in range(izq, der + 1):
                comparaciones += 1
                if arreglo[i - 1] > arreglo[i]:
                    intercambios += 1
                    arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1]
                    k = i
            
            der = k - 1

        print(f"Número de intercambios: {intercambios}")
        print(f"Número de comparaciones: {comparaciones}")
        return arreglo

def main():
    # En Python, para pasar una función como parámetro (como el lambda en Java),
    # simplemente pasamos el nombre del método.
    
    ArchivoUtils.medir_tiempo("archivo_10k.txt", "Shaker", Shaker.shaker)
    ArchivoUtils.medir_tiempo("archivo_100k.txt", "Shaker", Shaker.shaker)
    # Cuidado: 1M en Shaker Sort (O(n²)) puede tardar mucho en Python
    # ArchivoUtils.medir_tiempo("archivo_1M.txt", "Shaker", Shaker.shaker)

    ArchivoUtils.exportar_csv("Shaker")
    ArchivoUtils.exportar_json("Shaker")

if __name__ == "__main__":
    main()
