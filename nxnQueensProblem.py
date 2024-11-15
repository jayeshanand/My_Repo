def nxn_queens_formula(n):
    # Helper function to create the variable name Dij, where Row index = i and Column index = j
    def var(i, j):
        return (f"D{i}{j}")
    
    formula = []
    
    # 1. Ensure that there is exactly one queen in each row
    # (∧{i=1 to n} ((∨{j=1 to n} D{i,j}) ∧ (∧{j=1 to n} ∧{k=j+1 to n} (¬D{i,j} ∨ ¬D{i,k}))))
    row_formula = []
    for i in range(1, n + 1):
      # At least one queen in each row
      at_least_one = []
      for j in range(1, n + 1):
        at_least_one.append(var(i, j)) # add a new element in the list
      at_least_one_formula = f"({' | '.join(at_least_one)})" # joins all the elements of the list with a '|' in between

      # At most one queen in each row (as there should be no two queens in the same row and at least one queen in a row)
      at_most_one = []
      for j in range(1, n+1):
        for k in range(j+1, n+1):
          at_most_one.append(f"(!{var(i, j)} | !{var(i, k)})")
      at_most_one_formula = f"({' & '.join(at_most_one)})"        
        
        # Combine at_least_one and at_most_one conditions
      row_formula.append(f"({at_least_one_formula} & {at_most_one_formula})")
    formula.append(f"({' & '.join(row_formula)})")
    
    # 2. Ensure that there is exactly one queen in each column
    # (∧{j=1 to n} ((∨{i=1 to n} D{i,j}) ∧ (∧{i = 1 to n} ∧{k = i+1 to n} (¬D{i,j} ∨ ¬D{k,j}))))
    col_formula = []
    for j in range(1, n + 1):
        # At least one queen in each column
        at_least_one = []
        for i in range(1, n+1):
          at_least_one.append(var(i, j))
        at_least_one_formula = f"({' | '.join(at_least_one)})"
        
        # At most one queen in each column (no two queens in the same column)
        at_most_one = []
        for i in range(1, n + 1):
          for k in range(i + 1, n + 1):
            at_most_one.append(f"(!{var(i, j)} | !{var(k, j)})")
        at_most_one_formula = f"({' & '.join(at_most_one)})"
            
        
        # Combine at_least_one and at_most_one conditions
        col_formula.append(f"({at_least_one_formula} & {at_most_one_formula})")
    formula.append(f"({' & '.join(col_formula)})")
    
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
    
    # Join all parts of the formula with &
    full_formula = f"({' & '.join(formula)})"
    return full_formula

# Input: n value from user
n = int(input("Enter the value of n for an (n x n) chessboard: "))

# Generate and print the formula
result = nxn_queens_formula(n)
print(f"The formula for the {n} Queens Problem:\n{result}")
