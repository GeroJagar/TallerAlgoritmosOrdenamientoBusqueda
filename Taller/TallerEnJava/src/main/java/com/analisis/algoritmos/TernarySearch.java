package com.analisis.algoritmos;

public class TernarySearch {

     public static void probarArchivo(String nombreArchivo, String algoritmo) {

        System.out.println("\nProcesando: " + nombreArchivo);

        // 🔹 Leer archivo
        int[] datos = ArchivoUtils.leerArchivo(nombreArchivo);

        DualPivotQuicksort.dualPivotQuickSort(datos, 0, datos.length - 1);

        // 🔹 Medir SOLO la búsqueda
        long inicio = System.nanoTime();

        int resultado = findMinIndex(datos);

        long fin = System.nanoTime();

        long tiempoNs = fin - inicio;

        System.out.println("Tiempo (ns): " + tiempoNs);
        System.out.println("Índice mínimo encontrado: " + resultado);

        ArchivoUtils.agregarResultadoNs(algoritmo, nombreArchivo, tiempoNs);
    }

    public static void main(String[] args) {

        String algoritmo = "ternarysearch";

        ArchivoUtils.limpiarResultados();

        probarArchivo("archivo_10k.txt", algoritmo);
        probarArchivo("archivo_100k.txt", algoritmo);
        probarArchivo("archivo_1M.txt", algoritmo);

        ArchivoUtils.exportarCSVNs(algoritmo);
        ArchivoUtils.exportarJSONNs(algoritmo);
    }


    /*
    * Fuente: https://www.geeksforgeeks.org/dsa/ternary-search/
     */
    public static int findMinIndex(int[] arr) {
        int low = 0, high = arr.length - 1;
        int minIndex = -1;

        while (low <= high) {

            // divide the range into three parts
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;

            // if both mid1 and mid2 point to equal 
            // values narrow the search
            if (arr[mid1] == arr[mid2]) {

                // Move towards the center
                low = mid1 + 1;
                high = mid2 - 1;

                // tentatively store mid1 as
                // potential minimum
                minIndex = mid1;
            }

            // if arr[mid1] < arr[mid2], the minimum lies in the
            // left part (including mid1)
            else if (arr[mid1] < arr[mid2]) {
                high = mid2 - 1;

                // update with better candidate
                minIndex = mid1;
            }

            // is arr[mid1] > arr[mid2], the minimum lies in the
            // right part (including mid2)
            else {
                low = mid1 + 1;

                // update with better candidate
                minIndex = mid2;
            }
        }
        return minIndex;
    }
}
