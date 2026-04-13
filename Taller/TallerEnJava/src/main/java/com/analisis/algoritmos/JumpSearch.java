package com.analisis.algoritmos;

public class JumpSearch {

public static void probarArchivo(String nombreArchivo, int numero, String algoritmo) {

    System.out.println("\nProcesando: " + nombreArchivo);

    int[] datos = ArchivoUtils.leerArchivo(nombreArchivo);

    DualPivotQuicksort.dualPivotQuickSort(datos, 0, datos.length - 1);

    int resultado = -1;

    int repeticiones = 100;

    for (int i = 0; i < 50; i++) {
        jumpSearch(datos, numero);
    }

    long inicio = System.nanoTime();

    for (int i = 0; i < repeticiones; i++) {
        resultado = jumpSearch(datos, numero);
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

        String algoritmo = "jumpsearch";

        ArchivoUtils.limpiarResultados();

        int numeroBuscado = BinarySearch.generarNumeroAleatorio();
        System.out.println("Número a buscar: " + numeroBuscado);

        probarArchivo("archivo_10k.txt", numeroBuscado, algoritmo);
        probarArchivo("archivo_100k.txt", numeroBuscado, algoritmo);
        probarArchivo("archivo_1M.txt", numeroBuscado, algoritmo);

        ArchivoUtils.exportarCSVNs(algoritmo);
        ArchivoUtils.exportarJSONNs(algoritmo);
    }
    
    /*
    * Fuente: https://www.geeksforgeeks.org/dsa/jump-search/
     */
    public static int jumpSearch(int[] arr, int x){
        int n = arr.length;

        // Finding block size to be jumped
        int step = (int)Math.floor(Math.sqrt(n));

        // Finding the block where element is
        // present (if it is present)
        int prev = 0;
        for (int minStep = Math.min(step, n)-1; arr[minStep] < x; minStep = Math.min(step, n)-1){
            prev = step;
            step += (int)Math.floor(Math.sqrt(n));
            if (prev >= n)
                return -1;
        }

        // Doing a linear search for x in block
        // beginning with prev.
        while (arr[prev] < x){
            prev++;

            // If we reached next block or end of
            // array, element is not present.
            if (prev == Math.min(step, n))
                return -1;
        }

        // If element is found
        if (arr[prev] == x)
            return prev;

        return -1;
    }
}
