import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(start_state, goal_state, get_neighbors, heuristic):
    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state, cost in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            neighbor_node = Node(neighbor_state, current_node, current_node.cost + cost, heuristic(neighbor_state, goal_state))

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

# Example heuristic function (Manhattan distance)
def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

# Example function to get neighbors (up, down, left, right)
def get_neighbors(state):
    x, y = state
    neighbors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 5 and 0 <= new_y < 5:  # Adjust the boundaries according to your problem
            neighbors.append(((new_x, new_y), 1))  # Cost of moving to a neighbor is 1
    return neighbors

# Test the A* algorithm
if __name__ == "__main__":
    start_state = (0, 0)
    goal_state = (4, 4)
    path = astar_search(start_state, goal_state, get_neighbors, manhattan_distance)
    if path:
        print("Shortest path found:", path)
    else:
        print("No path found.")
