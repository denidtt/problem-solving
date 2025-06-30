from collections import deque


def bfs(arr, node):
    queue = deque(node)
    visited = []
    result = []
    while queue:
        print(f" Queue Before : {queue}")
        element=queue.popleft()
        print(f"popped {element} , Queue now : {queue}")
        if element not in visited:
            visited.append(element)
            print(visited)
            result.append(element)
        for neighbour in arr[element]:
            print()
            if neighbour not in visited:
                print(f" Queue Before extension: {queue}")
                queue.extend(neighbour)
                print(f"Queue adter extension: {queue}")
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}



print(bfs(graph,'A'))