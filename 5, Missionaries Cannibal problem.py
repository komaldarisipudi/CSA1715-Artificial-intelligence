from queue import Queue

def is_valid_state(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3 or (m != 0 and m < c) or (m != 3 and m > c):
        return False
    return True

def successors(state):
    m, c, b = state
    children = []
    for new_m in range(4):
        for new_c in range(4):
            if 1 <= new_m + new_c <= 2:
                new_state = (m + (-1)*b * new_m, c + (-1)*b * new_c, 1 - b)
                if is_valid_state(new_state):
                    children.append(new_state)
    return children

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    frontier = Queue()
    frontier.put([start])
    while not frontier.empty():
        path = frontier.get()
        current_state = path[-1]
        if current_state == goal:
            return path
        for child in successors(current_state):
            if child not in path:
                new_path = list(path)
                new_path.append(child)
                frontier.put(new_path)

solution = bfs()
for i, state in enumerate(solution):
    print(f"Step {i}: {state}")
