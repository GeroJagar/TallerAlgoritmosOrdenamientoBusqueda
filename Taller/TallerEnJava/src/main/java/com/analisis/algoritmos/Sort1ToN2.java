package com.analisis.algoritmos;
// Java program to sort an array of size n where elements are
// in range from 0 to n^2 – 1.
public class Sort1ToN2
{
    // A function to do counting sort of arr[] according to
    // the digit represented by exp.



    //T(n)countSort = 5 + 3(T(n)for) + T(n)for3 + T(n)for4 = 5 + 2(3n+2) + 3n-1 + 4n+6 = 13n+14
    void countSort(int arr[], int n, int exp)      // 3 param       3  
    {
        int output[] = new int[n]; // output array  //1 var         1       
        int i, count[] = new int[n] ;               //1 var         1
        for (i=0; i < n; i++)                       //i=0           1   T(n) for = 3n+2
                                                    //i++           n
                                                    //i < n         n+1
           count[i] = 0;                            //1 var         n

        // Store count of occurrences in count[]
        for (i = 0; i < n; i++)                     //i=0       1       T(n) for2 = 3n+2
                                                    //i<n       n+1
                                                    //i++       n
            count[ (arr[i]/exp)%n ]++;              //1 var     n

        // Change count[i] so that count[i] now contains actual
        // position of this digit in output[]
        for (i = 1; i < n; i++)                     //i=1       1           T(n) for3 = 3n-1
                                                    //i<n       n+1-1= n
                                                    //i++       n-1
            count[i] += count[i - 1];               //1var      n-1

        // Build the output array
        for (i = n - 1; i >= 0; i--)                            //i=n-1         1       T(n) for 4 = 4n+6
        {                                                       //i>=0          n+2
                                                                //i--           n+1
            output[count[ (arr[i]/exp)%n] - 1] = arr[i];        //1var          n+1
            count[(arr[i]/exp)%n]--;                            //1var          n+1
        }

        // Copy the output array to arr[], so that arr[] now
        // contains sorted numbers according to current digit
        for (i = 0; i < n; i++)         //i=0           1       T(n) for 5 = 3n+2
                                        //i<n           n+1
                                        //i++           n
            arr[i] = output[i];         //1var          n
    }


    // The main function to that sorts arr[] of size n using Radix Sort
    //T(n)sort = 2 + 2(T(n)countSort) = 2 + 2(13n+14) = 26n+30
    void sort(int arr[], int n)                                 //2 var
    {
        // Do counting sort for first digit in base n. Note that
        // instead of passing digit number, exp (n^0 = 1) is passed.
        countSort(arr, n, 1);                              //T(n)countSort = 13n+14

        // Do counting sort for second digit in base n. Note that
        // instead of passing digit number, exp (n^1 = n) is passed.
        countSort(arr, n, n);                                  //T(n)countSort = 13n+14
    }

    // A utility function to print an array
    //T(n)printArr = 2 + 3n+2 = 3n+4
    void printArr(int arr[], int n)                             //2 var
    {
        for (int i = 0; i < n; i++)         //i=0       1      T(n)for = 3n+2 
                                            //i<n       n+1
                                            //i++       n
            System.out.print(arr[i]+" ");   //1ins      n
    }

    // Driver program to test above functions
    //T(n)main = 6 + 2(3n+4) + 26n+30 = 32n + 4
    public static void main(String args[])          //1 var         1
    {
        Sort1ToN2 ob = new Sort1ToN2();             //1var          1

        // Since array size is 7, elements should be from 0 to 48
        int arr[] = {40, 12, 45, 32, 33, 1, 22};    //1var          1
        int n = arr.length;                         //1var          1
        System.out.println("Given array");          //1ins          1
        ob.printArr(arr, n);                        //T(n)printArr  3n+4

        ob.sort(arr, n);                            //T(n)sort      26n+30
        System.out.println("\nSorted array");       //1ins          1
        ob.printArr(arr, n);                        //T(n)printArr  3n+4
    }
}
/*This code is contributed by Rajat Mishra */
