from collections import deque
import traceback

def BFS(graph, node):
    result =[]
    visited=[]
    queue=deque([node])
    while queue:
        element = queue.popleft()
        if element not in visited:
            result.append(element)
            visited.append(element)
            for neighbour in graph[element]:
                if neighbour not in visited :
                    queue.extend(neighbour)
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

try:
    print(BFS(graph, '5'))
except Exception as e:
    traceback.print_exception(e)
