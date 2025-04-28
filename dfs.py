def dfs_path_length(graph, start_node, end_node, path=None):
    """
    Выполняет обход графа в глубину и возвращает длину пути между start_node и end_node.

    Args:
        graph:  Словарь, представляющий граф.
        start_node: Начальная вершина.
        end_node: Конечная вершина.
        path: Вспомогательный аргумент для хранения текущего пути.

    Returns:
        Длина пути от start_node до end_node (или -1, если путь не найден).
    """
    if path is None:
        path = [start_node]

    if start_node == end_node:
        return len(path) - 1  # Длина пути = количество ребер

    neighbors = graph.get(start_node, [])
    for neighbor in neighbors:
        if neighbor not in path:  # Чтобы избежать циклов
            new_path = path + [neighbor]
            length = dfs_path_length(graph, neighbor, end_node, new_path)
            if length != -1:  # Путь найден
                return length

    return -1  # Путь не найден

# Пример использования:
graph = {
    4: [2],
    1: [3],
    2: [4]
}
start_node = 2
end_node = 4
length = dfs_path_length(graph, start_node, end_node)
print("Path length:", length)

# def dfs(graph, start_node):
#     """
#     Выполняет обход графа в глубину (DFS).

#     Args:
#         graph: Словарь, представляющий граф.  Ключи - вершины, значения - списки смежных вершин.
#         start_node: Начальная вершина для обхода.

#     Returns:
#         Список вершин в порядке обхода.
#     """
#     visited = []
#     stack = [start_node]

#     while stack:
#         node = stack.pop()  # LIFO - последний вошел, первый вышел

#         if node not in visited:
#             visited.append(node)
#             neighbors = graph.get(node, [])  # Получаем соседей. Если нет вершины, возвращаем пустой список
#             stack.extend(neighbors)  # Добавляем соседей в стек

#     return visited

# # Пример использования:
# graph = {
#     1: [3],
#     2: [4],
#     4: [2]
# }
# start_node = 1
# path = dfs(graph, start_node)
# print("DFS Path:", path)