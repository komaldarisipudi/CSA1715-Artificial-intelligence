def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_chars = set(''.join(words))
    if len(unique_chars) > 10:
        return "Invalid input: More than 10 unique characters"

    chars = ''.join(unique_chars)
    used_digits = set()

    def is_valid(mapping):
        return all(mapping[word[0]] != '0' for word in words) and \
               sum(int(''.join(mapping[c] for c in word)) for word in words[:-1]) == int(''.join(mapping[c] for c in words[-1]))

    def backtrack(mapping):
        if len(mapping) == len(unique_chars):
            if is_valid(mapping):
                return mapping
            return None

        char = chars[len(mapping)]
        for digit in '1234567890':
            if digit not in used_digits:
                used_digits.add(digit)
                mapping[char] = digit
                result = backtrack(mapping)
                if result:
                    return result
                mapping.pop(char)
                used_digits.remove(digit)

    mapping = {}
    result = backtrack(mapping)
    if result:
        return result
    else:
        return "No solution found"

# Example
puzzle = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(puzzle)
print(solution)
