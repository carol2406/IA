from collections import deque

def is_valid(x, y):
    # Defina a função de validação aqui, por exemplo, para uma grade 10x10
    return 0 <= x < 10 and 0 <= y < 10

def bfs(start, goal):
    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

                if neighbor == goal:
                    path = []
                    temp = goal
                    while temp is not None:
                        path.append(temp)
                        temp = visited[temp]
                    path.reverse()
                    return path
    return []

def dfs(start, goal):
    if start == goal:
        return [start]

    stack = [start]
    visited = {start: None}

    while stack:
        current = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited:
                visited[neighbor] = current
                stack.append(neighbor)

                if neighbor == goal:
                    path = []
                    temp = goal
                    while temp is not None:
                        path.append(temp)
                        temp = visited[temp]
                    path.reverse()
                    return path
    return []

def greedy_search(start, goal):
    from heapq import heappop, heappush

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distância de Manhattan

    if start == goal:
        return [start]

    queue = [(0, start)]
    visited = {start: None}

    while queue:
        _, current = heappop(queue)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited:
                visited[neighbor] = current
                heappush(queue, (heuristic(neighbor, goal), neighbor))

                if neighbor == goal:
                    path = []
                    temp = goal
                    while temp is not None:
                        path.append(temp)
                        temp = visited[temp]
                    path.reverse()
                    return path
    return []

def a_star(start, goal):
    from heapq import heappop, heappush

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distância de Manhattan

    if start == goal:
        return [start]

    queue = [(0, start)]
    g_costs = {start: 0}
    visited = {start: None}

    while queue:
        _, current = heappop(queue)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor[0], neighbor[1]):
                new_cost = g_costs[current] + 1
                if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                    g_costs[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heappush(queue, (priority, neighbor))
                    visited[neighbor] = current

                    if neighbor == goal:
                        path = []
                        temp = goal
                        while temp is not None:
                            path.append(temp)
                            temp = visited[temp]
                        path.reverse()
                        return path
    return []

def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        current_start = queue_start.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_start[0] + dx, current_start[1] + dy)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited_start:
                visited_start[neighbor] = current_start
                queue_start.append(neighbor)

                if neighbor in visited_goal:
                    path_start = []
                    path_goal = []

                    temp = neighbor
                    while temp != start:
                        path_start.append(temp)
                        temp = visited_start[temp]
                    path_start.append(start)
                    path_start.reverse()

                    temp = visited_goal[neighbor]
                    while temp != goal:
                        path_goal.append(temp)
                        temp = visited_goal[temp]
                    path_goal.append(goal)

                    return path_start + path_goal[::-1]

        current_goal = queue_goal.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_goal[0] + dx, current_goal[1] + dy)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited_goal:
                visited_goal[neighbor] = current_goal
                queue_goal.append(neighbor)

                if neighbor in visited_start:
                    path_start = []
                    path_goal = []

                    temp = neighbor
                    while temp != start:
                        path_start.append(temp)
                        temp = visited_start[temp]
                    path_start.append(start)
                    path_start.reverse()

                    temp = visited_goal[neighbor]
                    while temp != goal:
                        path_goal.append(temp)
                        temp = visited_goal[temp]
                    path_goal.append(goal)

                    return path_start + path_goal[::-1]

    return []

# Testando os algoritmos
start = (0, 0)
goal = (3, 3)

print("Busca em Largura (BFS):", bfs(start, goal))
print("Busca em Profundidade (DFS):", dfs(start, goal))
print("Busca Bidirecional:", bidirectional_search(start, goal))
print("Busca Gulosa (Greedy):", greedy_search(start, goal))
print("Busca A*:", a_star(start, goal))
