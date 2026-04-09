import os
import time
import json

class Resultado:
    def __init__(self, algoritmo, archivo, tiempo_ms):
        self.algoritmo = algoritmo
        self.archivo = archivo
        self.tiempo_ms = tiempo_ms

class ResultadoNs:
    def __init__(self, algoritmo, archivo, tiempo_ns):
        self.algoritmo = algoritmo
        self.archivo = archivo
        self.tiempo_ns = tiempo_ns

class ArchivoUtils:
    _resultados = []
    _resultados_ns = []

    @staticmethod
    def leer_archivo(nombre_archivo):
        lista = []
        # Asumiendo que los archivos están en una carpeta llamada 'textos'
        ruta = os.path.join("textos", nombre_archivo)
        
        try:
            with open(ruta, 'r') as f:
                for linea in f:
                    if linea.strip():
                        lista.append(int(linea.strip()))
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        
        return lista  # En Python las listas funcionan como arreglos dinámicos

    @staticmethod
    def medir_tiempo(archivo, algoritmo, metodo):
        print(f"\nProcesando: {archivo} | {algoritmo}")
        
        datos = ArchivoUtils.leer_archivo(archivo)
        
        inicio = time.perf_counter_ns()
        metodo(datos)
        fin = time.perf_counter_ns()
        
        tiempo_ms = (fin - inicio) / 1_000_000.0
        print(f"Tiempo (ms): {tiempo_ms}")
        
        ArchivoUtils._resultados.append(Resultado(algoritmo, archivo, tiempo_ms))

    @staticmethod
    def medir_tiempo_ns(archivo, algoritmo, metodo):
        print(f"\nProcesando: {archivo} | {algoritmo} (ns)")
        
        datos = ArchivoUtils.leer_archivo(archivo)
        
        inicio = time.perf_counter_ns()
        metodo(datos)
        fin = time.perf_counter_ns()
        
        tiempo_ns = fin - inicio
        print(f"Tiempo (ns): {tiempo_ns}")
        
        ArchivoUtils._resultados_ns.append(ResultadoNs(algoritmo, archivo, tiempo_ns))

    @staticmethod
    def crear_carpeta_algoritmo(algoritmo):
        ruta = os.path.join("src", "main", "resultados", algoritmo)
        if not os.path.exists(ruta):
            os.makedirs(ruta)
        return ruta

    @staticmethod
    def exportar_csv(algoritmo):
        ruta_carpeta = ArchivoUtils.crear_carpeta_algoritmo(algoritmo)
        ruta_archivo = os.path.join(ruta_carpeta, "resultados.csv")
        
        try:
            with open(ruta_archivo, 'w') as f:
                f.write("Algoritmo,Archivo,Tiempo(ms)\n")
                for r in ArchivoUtils._resultados:
                    if r.algoritmo == algoritmo:
                        f.write(f"{r.algoritmo},{r.archivo},{r.tiempo_ms}\n")
            print(f"CSV creado en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar CSV: {e}")

    @staticmethod
    def exportar_csv_ns(algoritmo):
        ruta_carpeta = ArchivoUtils.crear_carpeta_algoritmo(algoritmo)
        ruta_archivo = os.path.join(ruta_carpeta, "resultados_ns.csv")
        
        try:
            with open(ruta_archivo, 'w') as f:
                f.write("Algoritmo,Archivo,Tiempo(ns)\n")
                for r in ArchivoUtils._resultados_ns:
                    if r.algoritmo == algoritmo:
                        f.write(f"{r.algoritmo},{r.archivo},{r.tiempo_ns}\n")
            print(f"CSV (ns) creado en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar CSV: {e}")

    @staticmethod
    def exportar_json(algoritmo):
        ruta_carpeta = ArchivoUtils.crear_carpeta_algoritmo(algoritmo)
        ruta_archivo = os.path.join(ruta_carpeta, "resultados.json")
        
        filtrados = [
            {"algoritmo": r.algoritmo, "archivo": r.archivo, "tiempoMs": r.tiempo_ms}
            for r in ArchivoUtils._resultados if r.algoritmo == algoritmo
        ]
        
        try:
            with open(ruta_archivo, 'w') as f:
                json.dump(filtrados, f, indent=2)
            print(f"JSON creado en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar JSON: {e}")

    @staticmethod
    def exportar_json_ns(algoritmo):
        ruta_carpeta = ArchivoUtils.crear_carpeta_algoritmo(algoritmo)
        ruta_archivo = os.path.join(ruta_carpeta, "resultados_ns.json")
        
        filtrados = [
            {"algoritmo": r.algoritmo, "archivo": r.archivo, "tiempoNs": r.tiempo_ns}
            for r in ArchivoUtils._resultados_ns if r.algoritmo == algoritmo
        ]
        
        try:
            with open(ruta_archivo, 'w') as f:
                json.dump(filtrados, f, indent=2)
            print(f"JSON (ns) creado en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al exportar JSON: {e}")

    @staticmethod
    def agregar_resultado(algoritmo, archivo, tiempo_ms):
        ArchivoUtils._resultados.append(Resultado(algoritmo, archivo, tiempo_ms))

    @staticmethod
    def agregar_resultado_ns(algoritmo, archivo, tiempo_ns):
        ArchivoUtils._resultados_ns.append(ResultadoNs(algoritmo, archivo, tiempo_ns))

    @staticmethod
    def limpiar_resultados():
        ArchivoUtils._resultados.clear()
        ArchivoUtils._resultados_ns.clear()
