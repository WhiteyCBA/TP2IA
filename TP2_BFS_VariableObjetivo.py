
from queue import Queue

graph = {'B': ['B1', 'B-1'], 'B1': ['B2'], 'B2': ['B3'], 'B3': ['B4'], 'B4': ['B5'], 'B5': ['B6'], 'B-1': ['B-2'], 'B-2': ['B-3'], 'B-3': ['B-4'], 'B-4': ['B-5'], 'B-5': ['B-6']}

def bfs_prototype(start, goal_position):
    graph_copy = graph.copy()
    graph_copy[goal_position] = ['A']
    graph_copy['A'] = []
    visited = set()
    queue = Queue()
    queue.put((start, [start]))

    print("Visitando nodos:")
    while not queue.empty():
        current, path = queue.get()
        print(f" -> {current}")
        if current == 'A':
            return path
        visited.add(current)
        for neighbor in graph_copy.get(current, []):
            if neighbor not in visited:
                queue.put((neighbor, path + [neighbor]))
    return None

if __name__ == "__main__":
    print("=== BFS - Objetivo en ubicación variable ===")
    start = 'B'
    goal_position = input("¿En qué nodo se encuentra A (ej: B2, B-1)? ")
    result = bfs_prototype(start, goal_position)
    print("Resultado BFS:", result)
    input("Presione Enter para cerrar...")
