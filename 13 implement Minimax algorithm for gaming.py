# Tic-Tac-Toe board represented as a list
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Function to print the Tic-Tac-Toe board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the current player has won
def is_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i*3 + j] == player for j in range(3)) or \
           all(board[j*3 + i] == player for j in range(3)):
            return True
    if all(board[i] == player for i in [0, 4, 8]) or \
       all(board[i] == player for i in [2, 4, 6]):
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Minimax algorithm
def minimax(depth, maximizing_player):
    if is_winner('X'):
        return -1
    elif is_winner('O'):
        return 1
    elif is_board_full():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using Minimax
def find_best_move():
    best_val = float('-inf')
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(0, False)
            board[i] = ' '

            if move_val > best_val:
                best_val = move_val
                best_move = i

    return best_move

# Main game loop
while True:
    print_board()

    # Player's move
    player_move = int(input("Enter your move (1-9): ")) - 1
    if board[player_move] == ' ':
        board[player_move] = 'X'
    else:
        print("Invalid move. Try again.")
        continue

    # Check if player wins
    if is_winner('X'):
        print_board()
        print("Congratulations! You win!")
        break

    # Check if the board is full
    if is_board_full():
        print_board()
        print("It's a tie!")
        break

    # AI's move
    ai_move = find_best_move()
    board[ai_move] = 'O'

    # Check if AI wins
    if is_winner('O'):
        print_board()
        print("You lose! Better luck next time.")
        break

    # Check if the board is full
    if is_board_full():
        print_board()
        print("It's a tie!")
        break
