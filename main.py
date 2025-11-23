"""
main.py
Práctica 3 – Árbol de Decisión Simple
Autor: Hugo Breganza 202301727
Curso: Análisis de Algoritmos

Este script:
1. Verifica o genera un archivo con 1000 números (1–100).
2. Clasifica cada número como "Alto" o "Bajo" según un umbral.
3. Imprime 10 ejemplos, conteos y tiempo total de ejecución.
"""

import os
import random
import time
from pathlib import Path


UMBRAL = 50  # valor por defecto


def verificar_o_generar_archivo(ruta_archivo):
    """
    Verifica si existe el archivo de números. Si no existe, lo genera
    automáticamente con 1000 enteros aleatorios entre 1 y 100.

    Args:
        ruta_archivo (Path): ruta donde debe estar o generarse el archivo.

    Returns:
        None
    """
    if ruta_archivo.exists():
        print("[INFO] Archivo encontrado:", ruta_archivo)
        return

    print("[INFO] Archivo no encontrado... generando numeros_1000.txt")
    ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

    semilla = random.randint(1, 999999)
    random.seed(semilla)

    with open(ruta_archivo, "w") as f:
        for _ in range(1000):
            f.write(str(random.randint(1, 100)) + "\n")

    print(f"[INFO] Archivo creado con semilla: {semilla}")


def cargar_numeros(ruta_archivo):
    """
    Carga los números desde un archivo TXT.

    Args:
        ruta_archivo (Path): ruta del archivo.

    Returns:
        list[int]: lista de 1000 números enteros.
    """
    with open(ruta_archivo, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def clasificar_numero(n):
    """
    Clasifica un número usando el árbol de decisión de un nodo.

    Args:
        n (int): número a clasificar.

    Returns:
        str: "Alto" o "Bajo".
    """
    return "Alto" if n >= UMBRAL else "Bajo"


def main():
    """
    Flujo principal del programa.
    """
    inicio = time.time()

    ruta_archivo = Path("data/numeros_1000.txt")
    verificar_o_generar_archivo(ruta_archivo)

    numeros = cargar_numeros(ruta_archivo)
    clasificaciones = [clasificar_numero(n) for n in numeros]

    # Ejemplos
    print("\n--- Ejemplos (primeros 10) ---")
    for n, c in list(zip(numeros, clasificaciones))[:10]:
        print(f"{n} → {c}")

    # Conteos
    altos = clasificaciones.count("Alto")
    bajos = clasificaciones.count("Bajo")

    print("\n--- Conteo total ---")
    print("Altos:", altos)
    print("Bajos:", bajos)

    fin = time.time()
    print("\nTiempo total de ejecución:", round(fin - inicio, 4), "segundos")


if __name__ == "__main__":
    main()
