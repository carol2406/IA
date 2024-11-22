from collections import deque
import heapq

# Algoritmo de Busca em Largura (BFS)
def bfs(graph, costs, start, goal):
    queue = deque([[start]])  # Fila inicial contendo o nó de partida
    visited = set()  # Conjunto para rastrear os nós visitados

    while queue:
        path = queue.popleft()  # Remove o primeiro caminho da fila
        node = path[-1]  # Último nó do caminho

        if node == goal:  # Verifica se encontrou o objetivo
            cost = sum(costs[path[i]][path[i + 1]] for i in range(len(path) - 1))
            return path, cost

        if node not in visited:  # Se o nó ainda não foi visitado
            visited.add(node)

            for neighbor in graph.get(node, []):  # Adiciona vizinhos não visitados à fila
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None, float('inf')  # Retorna None se não houver caminho

# Algoritmo de Busca em Profundidade (DFS)
def dfs(graph, costs, start, goal, path=None, visited=None):
    if path is None:
        path = [start]  # Inicializa o caminho com o nó de partida
    if visited is None:
        visited = set()  # Conjunto para rastrear os nós visitados

    node = path[-1]  # Último nó no caminho

    if node == goal:  # Verifica se encontrou o objetivo
        cost = sum(costs[path[i]][path[i + 1]] for i in range(len(path) - 1))
        return path, cost

    visited.add(node)  # Marca o nó como visitado

    for neighbor in graph.get(node, []):
        if neighbor not in visited:  # Explora somente vizinhos não visitados
            new_path = list(path)
            new_path.append(neighbor)
            result = dfs(graph, costs, start, goal, new_path, visited)
            if result[0]:  # Retorna o caminho encontrado
                return result

    return None, float('inf')  # Retorna None se não houver caminho

# Algoritmo de Busca Bidirecional
def bidirectional_search(graph, costs, start, goal):
    if start == goal:
        return [start], 0

    queue_start = deque([[start]])
    queue_goal = deque([[goal]])
    visited_start = set([start])
    visited_goal = set([goal])

    parents_start = {start: None}
    parents_goal = {goal: None}

    while queue_start and queue_goal:
        # Expande a busca a partir do início
        if queue_start:
            path_start = queue_start.popleft()
            node_start = path_start[-1]

            for neighbor in graph.get(node_start, []):
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    parents_start[neighbor] = node_start
                    queue_start.append(path_start + [neighbor])

                    if neighbor in visited_goal:
                        path = merge_paths(parents_start, parents_goal, neighbor)
                        cost = calculate_cost(path, costs)
                        return path, cost

        # Expande a busca a partir do objetivo
        if queue_goal:
            path_goal = queue_goal.popleft()
            node_goal = path_goal[-1]

            for neighbor in graph.get(node_goal, []):
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    parents_goal[neighbor] = node_goal
                    queue_goal.append(path_goal + [neighbor])

                    if neighbor in visited_start:
                        path = merge_paths(parents_start, parents_goal, neighbor)
                        cost = calculate_cost(path, costs)
                        return path, cost

    return None, float('inf')  # Retorna None se não houver caminho

# Função auxiliar para unir os caminhos das duas buscas
def merge_paths(parents_start, parents_goal, intersection):
    path_start = []
    node = intersection

    while node:
        path_start.append(node)
        node = parents_start[node]
    path_start.reverse()

    path_goal = []
    node = parents_goal[intersection]
    while node:
        path_goal.append(node)
        node = parents_goal[node]

    return path_start + path_goal

# Função para calcular o custo total de um caminho
def calculate_cost(path, costs):
    return sum(costs[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Algoritmo de Busca Gulosa
def greedy_search(graph, costs, heuristics, start, goal):
    # Fila de prioridade baseada no custo estimado (heurística)
    open_list = []
    heapq.heappush(open_list, (0, [start]))  # (custo estimado, caminho)
    visited = set()  # Conjunto para rastrear os nós visitados

    while open_list:
        current_cost, path = heapq.heappop(open_list)  # Remove o caminho com o menor custo estimado
        node = path[-1]  # Último nó do caminho

        if node == goal:  # Verifica se encontrou o objetivo
            cost = sum(costs[path[i]][path[i + 1]] for i in range(len(path) - 1))
            return path, cost

        if node not in visited:  # Se o nó ainda não foi visitado
            visited.add(node)

            # Adiciona os vizinhos à fila de prioridade com base na heurística
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heuristic_cost = current_cost + costs[path[-1]].get(neighbor, float('inf')) + heuristics.get(neighbor, 0)
                    heapq.heappush(open_list, (heuristic_cost, new_path))

    return None, float('inf')  # Retorna None se não houver caminho

# Exemplo de grafo, custos e heurísticas
graph = {
    "Cuiabá": ["Brasília", "Belo Horizonte"],
    "Brasília": ["Cuiabá", "Rio de Janeiro"],
    "Belo Horizonte": ["Cuiabá", "São Paulo"],
    "São Paulo": ["Curitiba", "Belo Horizonte", "Rio de Janeiro"],
    "Curitiba": ["São Paulo", "Florianópolis"],
    "Florianópolis": ["Curitiba"]
}

costs = {
    "Cuiabá": {"Brasília": 873, "Belo Horizonte": 1210},
    "Brasília": {"Cuiabá": 873, "Rio de Janeiro": 1148},
    "Belo Horizonte": {"Cuiabá": 1210, "São Paulo": 586},
    "São Paulo": {"Curitiba": 408, "Belo Horizonte": 586, "Rio de Janeiro": 429},
    "Curitiba": {"São Paulo": 408, "Florianópolis": 300},
    "Florianópolis": {"Curitiba": 300}
}

# Exemplo de heurísticas para a busca gulosa (distância estimada ao objetivo)
heuristics = {
    "Cuiabá": 2000,
    "Brasília": 1500,
    "Belo Horizonte": 1000,
    "São Paulo": 500,
    "Curitiba": 300,
    "Florianópolis": 0
}

# Exemplo de uso com BFS
start_city = "Cuiabá"
goal_city = "Florianópolis"

bfs_path, bfs_cost = bfs(graph, costs, start_city, goal_city)
print(f"BFS: Caminho = {' -> '.join(bfs_path) if bfs_path else 'Nenhum caminho encontrado'}, Custo = {bfs_cost}")

# Exemplo de uso com DFS
dfs_path, dfs_cost = dfs(graph, costs, start_city, goal_city)
print(f"DFS: Caminho = {' -> '.join(dfs_path) if dfs_path else 'Nenhum caminho encontrado'}, Custo = {dfs_cost}")

# Exemplo de uso com Busca Bidirecional
bidirectional_path, bidirectional_cost = bidirectional_search(graph, costs, start_city, goal_city)
print(f"Bidirecional: Caminho = {' -> '.join(bidirectional_path) if bidirectional_path else 'Nenhum caminho encontrado'}, Custo = {bidirectional_cost}")

# Exemplo de uso com Busca Gulosa
greedy_path, greedy_cost = greedy_search(graph, costs, heuristics, start_city, goal_city)
print(f"Gulosa: Caminho = {' -> '.join(greedy_path) if greedy_path else 'Nenhum caminho encontrado'}, Custo = {greedy_cost}")