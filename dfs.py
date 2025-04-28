def dfs(graph, start_node):
    """
    Выполняет обход графа в глубину (DFS).

    Args:
        graph: Словарь, представляющий граф.  Ключи - вершины, значения - списки смежных вершин.
        start_node: Начальная вершина для обхода.

    Returns:
        Список вершин в порядке обхода.
    """
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()  # LIFO - последний вошел, первый вышел

        if node not in visited:
            visited.append(node)
            neighbors = graph.get(node, [])  # Получаем соседей. Если нет вершины, возвращаем пустой список
            stack.extend(neighbors)  # Добавляем соседей в стек

    return visited

# Пример использования:
graph = {
    1: [3],
    2: [4],
    4: [2]
}
start_node = 1
path = dfs(graph, start_node)
print("DFS Path:", path)