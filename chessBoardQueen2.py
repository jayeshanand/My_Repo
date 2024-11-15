def generate_n_queens_formula(n):
    # Helper function to create the variable name D_i_j
    def var(i, j):
        return f"D{i}{j}"
    
    formula = []
    
    # 1. Ensure that there is exactly one queen in each row
    # (∧_{i=1 to n} ((∨_{j=1 to n} D_{i,j}) ∧ (∧_{j < k} (¬D_{i,j} ∨ ¬D_{i,k}))))
    row_conditions = []
    for i in range(1, n + 1):
        # At least one queen in each row
        at_least_one = f"({' | '.join(var(i, j) for j in range(1, n + 1))})"
        
        # At most one queen in each row (no two queens in the same row)
        at_most_one = [
            f"(!{var(i, j)} | !{var(i, k)})"
            for j in range(1, n + 1)
            for k in range(j + 1, n + 1)
        ]
        
        # Combine at_least_one and at_most_one conditions
        row_conditions.append(f"({at_least_one} & {' & '.join(at_most_one)})")
    formula.append(f"({' & '.join(row_conditions)})")
    
    # 2. Ensure that there is exactly one queen in each column
    # (∧_{j=1 to n} ((∨_{i=1 to n} D_{i,j}) ∧ (∧_{i < k} (¬D_{i,j} ∨ ¬D_{k,j}))))
    col_conditions = []
    for j in range(1, n + 1):
        # At least one queen in each column
        at_least_one = f"({' | '.join(var(i, j) for i in range(1, n + 1))})"
        
        # At most one queen in each column (no two queens in the same column)
        at_most_one = [
            f"(!{var(i, j)} | !{var(k, j)})"
            for i in range(1, n + 1)
            for k in range(i + 1, n + 1)
        ]
        
        # Combine at_least_one and at_most_one conditions
        col_conditions.append(f"({at_least_one} & {' & '.join(at_most_one)})")
    formula.append(f"({' & '.join(col_conditions)})")
    
    # 3. Ensure no two queens are on the same main diagonal (i - j)
    main_diag_conditions = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(i + 1, n + 1):
                for l in range(1, n + 1):
                    if (i - j) == (k - l):
                        main_diag_conditions.append(f"(!{var(i, j)} | !{var(k, l)})")
    if main_diag_conditions:
        formula.append(f"({' & '.join(main_diag_conditions)})")
    
    # 4. Ensure no two queens are on the same anti-diagonal (i + j)
    anti_diag_conditions = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(i + 1, n + 1):
                for l in range(1, n + 1):
                    if (i + j) == (k + l):
                        anti_diag_conditions.append(f"(!{var(i, j)} | !{var(k, l)})")
    if anti_diag_conditions:
        formula.append(f"({' & '.join(anti_diag_conditions)})")
    
    # Join all parts of the formula with ∧
    full_formula = f"({' & '.join(formula)})"
    return full_formula

# Input: n value from user
n = int(input("Enter the value of n for an (n x n) chessboard: "))

# Generate and print the formula
print("The formula for the", n, "Queens Problem:")
result = generate_n_queens_formula(n)
print(result)
