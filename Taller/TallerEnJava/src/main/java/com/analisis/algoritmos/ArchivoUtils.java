package com.analisis.algoritmos;

import java.io.*;
import java.util.*;
import java.util.function.Consumer;

public class ArchivoUtils {

    private static List<Resultado> resultados = new ArrayList<>();
    private static List<ResultadoNs> resultadosNs = new ArrayList<>();

    public static int[] leerArchivo(String nombreArchivo) {
        List<Integer> lista = new ArrayList<>();

        try (InputStream is = ArchivoUtils.class.getResourceAsStream("/textos/" + nombreArchivo);
             BufferedReader br = new BufferedReader(new InputStreamReader(is))) {

            if (is == null) {
                throw new RuntimeException("No se encontró el archivo: " + nombreArchivo);
            }

            String linea;
            while ((linea = br.readLine()) != null) {
                lista.add(Integer.parseInt(linea));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        int[] arreglo = new int[lista.size()];
        for (int i = 0; i < lista.size(); i++) {
            arreglo[i] = lista.get(i);
        }

        return arreglo;
    }

    public static void medirTiempo(String archivo, String algoritmo, Consumer<int[]> metodo) {
        System.out.println("\nProcesando: " + archivo + " | " + algoritmo);

        int[] datos = leerArchivo(archivo);

        long inicio = System.nanoTime();

        metodo.accept(datos);

        long fin = System.nanoTime();

        double tiempoMs = (fin - inicio) / 1_000_000.0;

        System.out.println("Tiempo (ms): " + tiempoMs);

        resultados.add(new Resultado(algoritmo, archivo, tiempoMs));
    }

    //Medir tiempo en nanosegundos para métodos de ordenamiento
    public static void medirTiempoNs(String archivo, String algoritmo, Consumer<int[]> metodo) {
        System.out.println("\nProcesando: " + archivo + " | " + algoritmo + " (ns)");

        int[] datos = leerArchivo(archivo);

        long inicio = System.nanoTime();

        metodo.accept(datos);

        long fin = System.nanoTime();

        long tiempoNs = fin - inicio;

        System.out.println("Tiempo (ns): " + tiempoNs);

        resultadosNs.add(new ResultadoNs(algoritmo, archivo, tiempoNs));
    }

    public static File crearCarpetaAlgoritmo(String algoritmo) {
        String ruta = "src/main/resultados/" + algoritmo;
        File carpeta = new File(ruta);

        if (!carpeta.exists()) {
            carpeta.mkdirs();
        }

        return carpeta;
    }

    public static void exportarCSV(String algoritmo) {
        File carpeta = crearCarpetaAlgoritmo(algoritmo);
        File archivo = new File(carpeta, "resultados.csv");

        try (PrintWriter pw = new PrintWriter(archivo)) {

            pw.println("Algoritmo,Archivo,Tiempo(ms)");

            for (Resultado r : resultados) {
                if (r.algoritmo.equals(algoritmo)) {
                    pw.println(r.algoritmo + "," + r.archivo + "," + r.tiempoMs);
                }
            }

            System.out.println("CSV creado en: " + archivo.getPath());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //Exportar CSV en Nanosegundos para métodos de busqueda
    public static void exportarCSVNs(String algoritmo) {
        File carpeta = crearCarpetaAlgoritmo(algoritmo);
        File archivo = new File(carpeta, "resultados_ns.csv");

        try (PrintWriter pw = new PrintWriter(archivo)) {

            pw.println("Algoritmo,Archivo,Tiempo(ns)");

            for (ResultadoNs r : resultadosNs) {
                if (r.algoritmo.equals(algoritmo)) {
                    pw.println(r.algoritmo + "," + r.archivo + "," + r.tiempoNs);
                }
            }

            System.out.println("CSV (ns) creado en: " + archivo.getPath());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void exportarJSON(String algoritmo) {
        File carpeta = crearCarpetaAlgoritmo(algoritmo);
        File archivo = new File(carpeta, "resultados.json");

        try (PrintWriter pw = new PrintWriter(archivo)) {

            pw.println("[");

            List<Resultado> filtrados = new ArrayList<>();
            for (Resultado r : resultados) {
                if (r.algoritmo.equals(algoritmo)) {
                    filtrados.add(r);
                }
            }

            for (int i = 0; i < filtrados.size(); i++) {
                Resultado r = filtrados.get(i);

                pw.print("  {");
                pw.print("\"algoritmo\": \"" + r.algoritmo + "\", ");
                pw.print("\"archivo\": \"" + r.archivo + "\", ");
                pw.print("\"tiempoMs\": " + r.tiempoMs);
                pw.print("}");

                if (i < filtrados.size() - 1) {
                    pw.println(",");
                } else {
                    pw.println();
                }
            }

            pw.println("]");

            System.out.println("JSON creado en: " + archivo.getPath());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //Exportar JSON en nanosegundos para métodos de ordenamiento.
    public static void exportarJSONNs(String algoritmo) {
        File carpeta = crearCarpetaAlgoritmo(algoritmo);
        File archivo = new File(carpeta, "resultados_ns.json");

        try (PrintWriter pw = new PrintWriter(archivo)) {

            pw.println("[");

            List<ResultadoNs> filtrados = new ArrayList<>();
            for (ResultadoNs r : resultadosNs) {
                if (r.algoritmo.equals(algoritmo)) {
                    filtrados.add(r);
                }
            }

            for (int i = 0; i < filtrados.size(); i++) {
                ResultadoNs r = filtrados.get(i);

                pw.print("  {");
                pw.print("\"algoritmo\": \"" + r.algoritmo + "\", ");
                pw.print("\"archivo\": \"" + r.archivo + "\", ");
                pw.print("\"tiempoNs\": " + r.tiempoNs);
                pw.print("}");

                if (i < filtrados.size() - 1) {
                    pw.println(",");
                } else {
                    pw.println();
                }
            }

            pw.println("]");

            System.out.println("JSON (ns) creado en: " + archivo.getPath());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void agregarResultado(String algoritmo, String archivo, double tiempoMs) {
        resultados.add(new Resultado(algoritmo, archivo, tiempoMs));
    }

    public static void agregarResultadoNs(String algoritmo, String archivo, long tiempoNs) {
        resultadosNs.add(new ResultadoNs(algoritmo, archivo, tiempoNs));
    }

    public static void limpiarResultados() {
        resultados.clear();
        resultadosNs.clear();
    }
}