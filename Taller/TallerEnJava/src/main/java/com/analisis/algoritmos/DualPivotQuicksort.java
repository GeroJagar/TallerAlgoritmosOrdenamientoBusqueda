package com.analisis.algoritmos;

public class DualPivotQuicksort {

    public static void main(String[] args) {

        ArchivoUtils.medirTiempo("archivo_10k.txt", "Dual-Pivot Quicksort",arr -> dualPivotQuickSort(arr, 0, arr.length - 1));
        ArchivoUtils.medirTiempo("archivo_100k.txt", "Dual-Pivot Quicksort", arr -> dualPivotQuickSort(arr, 0, arr.length - 1));
        ArchivoUtils.medirTiempo("archivo_1M.txt", "Dual-Pivot Quicksort", arr -> dualPivotQuickSort(arr, 0, arr.length - 1));

        ArchivoUtils.exportarCSV("Dual-Pivot Quicksort");
        ArchivoUtils.exportarJSON("Dual-Pivot Quicksort");
    }

     /*
    * Fuente: https://www.geeksforgeeks.org/dsa/dual-pivot-quicksort/
    */
    static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /*
    * Fuente: https://www.geeksforgeeks.org/dsa/dual-pivot-quicksort/
    */
    static void dualPivotQuickSort(int[] arr, int low, int high){
        if (low < high){
            
            // piv[] stores left pivot and right pivot.
            // piv[0] means left pivot and
            // piv[1] means right pivot
            int[] piv;
            piv = partition(arr, low, high);
            
            dualPivotQuickSort(arr, low, piv[0] - 1);
            dualPivotQuickSort(arr, piv[0] + 1, piv[1] - 1);
            dualPivotQuickSort(arr, piv[1] + 1, high);
        }
    }

    /*
    * Fuente: https://www.geeksforgeeks.org/dsa/dual-pivot-quicksort/
    */
    static int[] partition(int[] arr, int low, int high){
        if (arr[low] > arr[high])
            swap(arr, low, high);
            
        // p is the left pivot, and q 
        // is the right pivot.
        int j = low + 1;
        int g = high - 1, k = low + 1,
            p = arr[low], q = arr[high];
            
        while (k <= g){
            
            // If elements are less than the left pivot
            if (arr[k] < p){
                swap(arr, k, j);
                j++;
            }
            
            // If elements are greater than or equal
            // to the right pivot
            else if (arr[k] >= q){
                while (arr[g] > q && k < g)
                    g--;
                    
                swap(arr, k, g);
                g--;
                
                if (arr[k] < p){
                    swap(arr, k, j);
                    j++;
                }
            }
            k++;
        }
        j--;
        g++;
        
        // Bring pivots to their appropriate positions.
        swap(arr, low, j);
        swap(arr, high, g);

        // Returning the indices of the pivots
        // because we cannot return two elements
        // from a function, we do that using an array.
        return new int[] { j, g };
    }
    // This code is contributed by Gourish Sadhu

}