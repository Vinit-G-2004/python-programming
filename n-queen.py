def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False  
    return True
def solve_n_queens(n):
    def backtrack(row):
        nonlocal min_cost
        if row == n:
            min_cost += 1
            return       
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = True
                backtrack(row + 1)
                board[row][col] = False
    board = [[False] * n for _ in range(n)]
    min_cost = 0
    backtrack(0)
    return min_cost
n = 8  # Board size
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens problem:", solutions)
