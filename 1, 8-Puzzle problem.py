import heapq
import itertools

class PuzzleState:
    def __init__(self, puzzle, g=0, h=0, parent=None, move=""):
        self.puzzle = puzzle
        self.g = g
        self.h = h
        self.parent = parent
        self.move = move

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.puzzle])

def get_blank_position(puzzle):
    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j

def get_manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                x, y = divmod(puzzle[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_possible_moves(puzzle):
    moves = []
    blank_row, blank_col = get_blank_position(puzzle)
    for dr, dc, move in [(1, 0, 'DOWN'), (-1, 0, 'UP'), (0, 1, 'RIGHT'), (0, -1, 'LEFT')]:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [list(row) for row in puzzle]
            new_puzzle[blank_row][blank_col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[blank_row][blank_col]
            moves.append((new_puzzle, move))
    return moves

def reconstruct_path(node):
    path = []
    while node:
        path.append((node.move, node.puzzle))
        node = node.parent
    return path[::-1]

def solve_puzzle(initial_state):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, initial_state)
    
    while open_set:
        current_state = heapq.heappop(open_set)
        
        if current_state.puzzle == goal_state:
            return reconstruct_path(current_state)
        
        closed_set.add(current_state)
        
        for next_puzzle, move in get_possible_moves(current_state.puzzle):
            next_state = PuzzleState(next_puzzle, current_state.g + 1, get_manhattan_distance(next_puzzle), current_state, move)
            
            if next_state in closed_set:
                continue
            
            if next_state not in open_set:
                heapq.heappush(open_set, next_state)
    
    return None

initial_state = PuzzleState([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution = solve_puzzle(initial_state)

if solution:
    for step, puzzle in solution:
        print(f"Move: {step}")
        print(puzzle)
        print()
else:
    print("No solution found.")
