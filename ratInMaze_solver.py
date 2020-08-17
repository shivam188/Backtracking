global N
N = 5

maze = [
    [1,0,1,0,0],
    [1,1,1,1,1],
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,1,1,0,1]
]

solution = [[0]*N for _ in range(N)]

def print_maze(solution):
    for i in range(N):
        for j in range(N):
            print(solution[i][j], end=" ")
        print()

def solve(row, col):
    if (row == N-1 and col == N-1):
        solution[row][col] = 1
        return True

    if (row >= 0 and col >= 0 and row < N and col < N and solution[row][col] == 0
    and maze[row][col] == 1):
        solution[row][col] = 1

        if solve(row+1, col):
            return True
        if solve(row, col+1):
            return True
        if solve(row-1, col):
            return True
        if solve(row, col-1):
            return True

        solution[row][col] = 0
        return False
    return False


solve(0, 0)
print_maze(solution)
