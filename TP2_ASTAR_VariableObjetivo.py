
from queue import PriorityQueue

graph = {'B': ['B1', 'B-1'], 'B1': ['B2'], 'B2': ['B3'], 'B3': ['B4'], 'B4': ['B5'], 'B5': ['B6'], 'B-1': ['B-2'], 'B-2': ['B-3'], 'B-3': ['B-4'], 'B-4': ['B-5'], 'B-5': ['B-6']}
heuristic = {'B': 6, 'B1': 5, 'B2': 4, 'B3': 3, 'B4': 2, 'B5': 1, 'B6': 1, 'B-1': 10, 'B-2': 11, 'B-3': 12, 'B-4': 13, 'B-5': 14, 'B-6': 15, 'A': 0}

def astar_prototype(start, goal_position):
    graph_copy = graph.copy()
    graph_copy[goal_position] = ['A']
    graph_copy['A'] = []
    open_set = PriorityQueue()
    open_set.put((heuristic.get(start, 999), 0, start, [start]))
    visited = set()

    print("Explorando nodos (f(n) = g + h):")
    while not open_set.empty():
        f, g, current, path = open_set.get()
        print(f" -> {current} (g={g}, h={heuristic.get(current,999)}, f={f})")
        if current == 'A':
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph_copy.get(current, []):
            if neighbor not in visited:
                g_new = g + 1
                f_new = g_new + heuristic.get(neighbor, 999)
                open_set.put((f_new, g_new, neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    print("=== A* - Objetivo en ubicación variable ===")
    start = 'B'
    goal_position = input("¿En qué nodo se encuentra A (ej: B2, B-1)? ")
    result = astar_prototype(start, goal_position)
    print("Resultado A*:", result)
    input("Presione Enter para cerrar...")
