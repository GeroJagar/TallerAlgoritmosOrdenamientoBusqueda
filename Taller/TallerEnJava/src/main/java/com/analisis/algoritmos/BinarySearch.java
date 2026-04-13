package com.analisis.algoritmos;

public class BinarySearch {

    public static int generarNumeroAleatorio() {
        return (int)(Math.random() * 90000000) + 10000000;
    }

    /*
    * Fuente: https://www.geeksforgeeks.org/dsa/binary-search/
    */
    static int binarySearch(int arr[], int low, int high, int x) {
        if (high >= low) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == x)
                return mid;

            if (arr[mid] > x)
                return binarySearch(arr, low, mid - 1, x);

            return binarySearch(arr, mid + 1, high, x);
        }

        return -1;
    }

    public static void probarArchivo(String nombreArchivo, int numero, String algoritmo) {

        System.out.println("\nProcesando: " + nombreArchivo);

        int[] datos = ArchivoUtils.leerArchivo(nombreArchivo);

        DualPivotQuicksort.dualPivotQuickSort(datos, 0, datos.length - 1);

        int resultado = -1;

        int repeticiones = 100;

        for (int i = 0; i < 50; i++) {
            binarySearch(datos, 0, datos.length - 1, numero);
        }

        long inicio = System.nanoTime();

        for (int i = 0; i < repeticiones; i++) {
            resultado = binarySearch(datos, 0, datos.length - 1, numero);
        }

        long fin = System.nanoTime();

        long tiempoPromedioNs = (fin - inicio) / repeticiones;

        System.out.println("Tiempo promedio (ns): " + tiempoPromedioNs);

        if (resultado != -1) {
            System.out.println("Número encontrado en posición: " + resultado);
        } else {
            System.out.println("Número NO encontrado");
        }

        ArchivoUtils.agregarResultadoNs(algoritmo, nombreArchivo, tiempoPromedioNs);
    }

    public static void main(String[] args) {

        String algoritmo = "binarysearch";

        ArchivoUtils.limpiarResultados();

        int numeroBuscado = generarNumeroAleatorio();
        System.out.println("Número a buscar: " + numeroBuscado);

        probarArchivo("archivo_10k.txt", numeroBuscado, algoritmo);
        probarArchivo("archivo_100k.txt", numeroBuscado, algoritmo);
        probarArchivo("archivo_1M.txt", numeroBuscado, algoritmo);

        ArchivoUtils.exportarCSVNs(algoritmo);
        ArchivoUtils.exportarJSONNs(algoritmo);
    }
}
