class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found
        unassigned_variables = [var for var in self.variables if var not in assignment]
        current_variable = unassigned_variables[0]

        for value in self.domains[current_variable]:
            if self.is_consistent(current_variable, value, assignment):
                assignment[current_variable] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[current_variable]

        return None  # No solution found

def main():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {var: ['R', 'G', 'B'] for var in variables}  # Possible colors: Red, Green, Blue

    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    map_coloring_csp = MapColoringCSP(variables, domains, constraints)
    solution = map_coloring_csp.backtracking_search()

    if solution:
        print("Solution found:")
        for variable, color in solution.items():
            print(f"{variable}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
