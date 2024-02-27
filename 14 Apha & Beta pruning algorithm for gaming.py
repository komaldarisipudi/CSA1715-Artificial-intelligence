class GameState:
    def __init__(self, value):
        self.value = value
        self.children = []

def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval_child = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_child)
            alpha = max(alpha, eval_child)
            if beta <= alpha:
                break  # Beta pruning
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval_child = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_child)
            beta = min(beta, eval_child)
            if beta <= alpha:
                break  # Alpha pruning
        return min_eval

# Example usage
if __name__ == "__main__":
    # Construct a sample game tree
    root = GameState(3)
    child1 = GameState(5)
    child2 = GameState(2)
    child3 = GameState(9)

    root.children = [child1, child2, child3]

    child1.children = [GameState(7), GameState(8)]
    child2.children = [GameState(1), GameState(4)]
    child3.children = [GameState(6), GameState(3)]

    # Set initial alpha and beta values
    alpha = float('-inf')
    beta = float('inf')

    # Call alpha-beta pruning function
    result = minimax_alpha_beta(root, 3, alpha, beta, True)

    print("Optimal value:", result)
