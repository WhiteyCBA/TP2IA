#Simulación de Búsqueda para Alineación de Block de Motor

Este proyecto contiene dos algoritmos que simulan cómo un robot podría buscar la posición exacta de alineación del block de un motor, utilizando estrategias de búsqueda automatizada.

##Descripción

Se desarrollaron dos enfoques distintos de búsqueda:

- **Búsqueda en Anchura (BFS):** recorre todos los nodos nivel por nivel, explorando ambos lados del eje horizontal.
- **Búsqueda Heurística (A\*):** utiliza una heurística para priorizar el camino más prometedor, optimizando la búsqueda si el objetivo está en la rama correcta.

Ambos algoritmos permiten simular el caso en el que el block (posición `A`) puede estar ubicado en distintas posiciones del eje, como `B-1`, `B2`, `B3`, etc.

---

##Contenido del Repositorio

| Archivo                          | Descripción                                           |
|----------------------------------|--------------------------------------------------------|
| `TP2_BFS_VariableObjetivo.py`   | Implementación de búsqueda en anchura con posición dinámica del objetivo. |
| `TP2_ASTAR_VariableObjetivo.py` | Implementación de A\* con heurística y ubicación dinámica del objetivo.    |

---

##Cómo ejecutar

### Requisitos:
- Python 3.x (ninguna librería externa requerida)

### Ejecución:
```bash
python TP2_BFS_VariableObjetivo.py
```
o
```bash
python TP2_ASTAR_VariableObjetivo.py
```

Luego se te pedirá que ingreses en qué nodo está el objetivo `A`. Por ejemplo:

```
¿En qué nodo se encuentra A (ej: B3, B-1)? B2
```

---

##Ejemplo de comparación

| Caso                 | Camino BFS                   | Pasos BFS | Camino A\*                   | Pasos A\* |
|----------------------|-------------------------------|-----------|-------------------------------|-----------|
| A en `B-1`           | `['B', 'B-1', 'A']`           | 5         | `['B', 'B-1', 'A']`           | 9         |
| A en `B3`            | `['B', 'B1', 'B2', 'B3', 'A']`| 8         | `['B', 'B1', 'B2', 'B3', 'A']`| 5         |

---

##Autor

Iván Bustamante  
Trabajo práctico para la materia de Inteligencia Artificial - Módulo 2  
2025
