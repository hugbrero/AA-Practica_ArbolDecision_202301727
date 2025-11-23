# Práctica 3 – Árbol de Decisión  
**Curso:** Análisis de Algoritmos  
**Universidad Da Vinci de Guatemala**  
**Estudiante:** Hugo Breganza aunque es prueba de cambio
**Carnet:** 202301727 
**Fecha:** Noviembre 2025  

---

## 🎯 Objetivo General
Construir y ejecutar un árbol de decisión simple en Python para clasificar números como “Alto” o “Bajo”, aplicando correctamente el flujo de trabajo Gitflow.

---

## 🎯 Objetivos Específicos
- Implementar un árbol con un solo nodo de decisión y 2 hojas.
- Leer un archivo con 1000 números y clasificarlos.
- Generar salidas claras en consola.
- Utilizar Gitflow (ramas feature, hotfix, PRs y merges).
- Documentar funciones con docstrings PEP-257.

---

## 🌳 Descripción del Árbol de Decisión
El árbol utilizado tiene:
- **Un único nodo de decisión** con el criterio:  
  `numero >= UMBRAL`
- **Dos hojas:**  
  - “Alto”  
  - “Bajo”  
- El umbral por defecto es **UMBRAL = 50**, configurable dentro del script.

---

## 🔧 Metodología
### Flujo del script:
1. Verificar si existe `data/numeros_1000.txt`.
2. Generarlo si no existe (1000 números aleatorios entre 1–100).
3. Cargar los números.
4. Clasificarlos con un árbol minimalista (if/else).
5. Imprimir:
   - 10 ejemplos
   - Conteo “Alto” / “Bajo”
   - Tiempo total

### Flujo Gitflow aplicado:
- Rama `feature/implementacion_arbol`
- Commits significativos
- PR hacia `develop`
- Hotfix con cambio de nombre en README
- Merge `develop` → `main`
- Tag final: **v1.0.0**

---

## 📌 Resultados
C:\[AA]Practica_ArbolDecision_202301727>python main.py
[INFO] Archivo encontrado: data\numeros_1000.txt

--- Ejemplos (primeros 10) ---
38 → Bajo
4 → Bajo
23 → Bajo
1 → Bajo
85 → Alto
10 → Bajo
7 → Bajo
35 → Bajo
4 → Bajo
15 → Bajo

--- Conteo total ---
Altos: 494
Bajos: 506

Tiempo total de ejecución: 0.0087 segundos

C:\[AA]Practica_ArbolDecision_202301727>


