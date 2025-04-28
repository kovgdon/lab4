def dfs_path(graph, start, end, path=None):
    """
    Обход графа в глубину с поиском пути от start до end и обработкой исключений.
    # Добавлен комментарий - проверка наличия вершин в графе
    # patch2 Добавлен комментарий Проверяем наличие вершин в графе
    """
    if start not in graph or end not in graph:
        raise ValueError("Начальная или конечная вершина не существует в графе.")

    if path is None:
        path = [start]
    if start == end:
        return path
    for neighbor in graph[start]:
        # patch2 - Добавлен комментарий: Проверяем, не посетили ли мы уже эту вершину
        if neighbor not in path:
            try:
                new_path = dfs_path(graph, neighbor, end, path + [neighbor])
                if new_path:
                    return new_path
            except ValueError:
                pass  # Пропускаем, если во время рекурсии возникла ошибка
    return None

# def dfs_path(graph, start, end, path=None):
#     """
#     Обход графа в глубину с поиском пути от start до end и обработкой исключений.
#     """
#     if start not in graph or end not in graph:
#         raise ValueError("Начальная или конечная вершина не существует в графе.")

#     if path is None:
#         path = [start]
#     if start == end:
#         return path
#     for neighbor in graph[start]:
#         if neighbor not in path:
#             try:
#                 new_path = dfs_path(graph, neighbor, end, path + [neighbor])
#                 if new_path:
#                     return new_path
#             except ValueError:
#                 pass  # Пропускаем, если во время рекурсии возникла ошибка
#     return None


# # Пример использования
# graph = {
#     1: {3},
#     2: {4},
#     3: {1},
#     4: {2}
# }
# start_node = 2
# end_node = 5  # Некорректная вершина

# try:
#     path = dfs_path(graph, start_node, end_node)

#     if path:
#         print(f"Путь от {start_node} до {end_node}: {path}")
#         print(f"Длина пути: {len(path) - 1}")  # Длина пути - количество ребер
#     else:
#         print(f"Путь от {start_node} до {end_node} не найден.")
# except ValueError as e:
#     print(f"Ошибка: {e}")

# def dfs_path_length(graph, start_node, end_node, path=None):
#     """
#     Выполняет обход графа в глубину и возвращает длину пути между start_node и end_node.

#     Args:
#         graph:  Словарь, представляющий граф.
#         start_node: Начальная вершина.
#         end_node: Конечная вершина.
#         path: Вспомогательный аргумент для хранения текущего пути.

#     Returns:
#         Длина пути от start_node до end_node (или -1, если путь не найден).
#     """
#     if path is None:
#         path = [start_node]

#     if start_node == end_node:
#         return len(path) - 1  # Длина пути = количество ребер

#     neighbors = graph.get(start_node, [])
#     for neighbor in neighbors:
#         if neighbor not in path:  # Чтобы избежать циклов
#             new_path = path + [neighbor]
#             length = dfs_path_length(graph, neighbor, end_node, new_path)
#             if length != -1:  # Путь найден
#                 return length

#     return -1  # Путь не найден

# # Пример использования:
# graph = {
#     4: [2],
#     1: [3],
#     2: [4]
# }
# start_node = 2
# end_node = 4
# length = dfs_path_length(graph, start_node, end_node)
# print("Path length:", length)

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
