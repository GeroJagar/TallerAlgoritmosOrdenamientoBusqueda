package com.analisis.algoritmos;
/**
 * Esta clase implementa el método de la sacudida o Shaker Sort
 * @author leon
 *
 */
public class Shaker {
	
	public static void main(String[] args) {

		ArchivoUtils.medirTiempo("archivo_10k.txt", "Shaker", arr -> shaker(arr));
		ArchivoUtils.medirTiempo("archivo_100k.txt", "Shaker", arr -> shaker(arr));
		ArchivoUtils.medirTiempo("archivo_1M.txt", "Shaker", arr -> shaker(arr));
	
		ArchivoUtils.exportarCSV("Shaker");
		ArchivoUtils.exportarJSON("Shaker");
	}
	/**
	 * El método que ordena mediante la sacudida
	 * @param arreglo El arreglo a ordenar.
	 * @return El arreglo ya ordenado.
	 * 
	 * Fuente: https://gist.github.com/leonlipe/488e3e6c67811ae2e34086e38ae96ee7
	 *  
	 */
    public static int[] shaker(int[] arreglo){
        int intercambios = 0, comparaciones = 0;
        int i, izq, der, k, aux;

        izq = 1;
        der = arreglo.length - 1;
        k = arreglo.length - 1;

        while (izq <= der) {

            for (i = der; i >= izq; i--) {
                comparaciones++;
                if (arreglo[i - 1] > arreglo[i]) {
                    intercambios++;
                    aux = arreglo[i - 1];
                    arreglo[i - 1] = arreglo[i];
                    arreglo[i] = aux;
                    k = i;
                }
            }

            izq = k + 1;

            for (i = izq; i <= der; i++) {
                comparaciones++;
                if (arreglo[i - 1] > arreglo[i]) {
                    intercambios++;
                    aux = arreglo[i - 1];
                    arreglo[i - 1] = arreglo[i];
                    arreglo[i] = aux;
                    k = i;
                }
            }

            der = k - 1;
        }

        System.out.println("Numero de intercambios: " + intercambios);
        System.out.println("Numero de comparaciones: " + comparaciones);

        return arreglo;
    }
}