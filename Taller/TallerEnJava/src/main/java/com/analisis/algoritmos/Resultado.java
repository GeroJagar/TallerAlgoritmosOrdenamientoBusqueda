package com.analisis.algoritmos;

public class Resultado {
    public String algoritmo;
    public String archivo;
    public double tiempoMs;

    public Resultado(String algoritmo, String archivo, double tiempoMs) {
        this.algoritmo = algoritmo;
        this.archivo = archivo;
        this.tiempoMs = tiempoMs;
    }
}
