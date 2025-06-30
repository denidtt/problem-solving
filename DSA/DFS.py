def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        result.append(node)
        for child in graph[node]:
            dfs_recursive(graph, child,visited)
    # print(result)
    return result


def dfs_iterative(graph, node):
    stack = [node]
    visited = []
    result = []
    while stack:
        element = stack.pop()
        if element not in visited:
            result.append(element)
            visited.append(element)
            for child in graph[element]:
                stack.extend(reversed(graph[element]))

    return result


result = []
tree = {
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
graph = {
    '5': ['3', '7'], '3': ['2', '4'], '7': ['8'], '2': [], '4': ['8'], '8': []
}

# ['A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'L', 'M', 'G', 'N', 'O']

print(dfs_recursive(tree, 'A'))
