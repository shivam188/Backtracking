import time
global N
N = 4

board = [[0]*N for _ in range(N)]

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def valid(board, row, col):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    for i in range(N):
        for j in range(N):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True

def solve(board, queens = N):
    if queens == 0:
        return True

    for i in range(N):
        for j in range(N):
            if valid(board, i, j) and (board[i][j] != 1):
                board[i][j] = 1

                if solve(board, queens-1):
                    return True
                board[i][j] = 0

    return False

start = time.time()
solve(board)
stop = time.time()
print_board(board)
print("Time Taken : ", stop - start )

