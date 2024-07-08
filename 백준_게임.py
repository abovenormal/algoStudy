# RecursionError 다시 풀기..

def max_moves(board, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1] * M for _ in range(N)]
    dp = [[0] * M for _ in range(N)]

    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M or board[x][y] == 'H':
            return 0
        if visited[x][y] == 1:
            return -1
        if dp[x][y] != 0:
            return dp[x][y]

        visited[x][y] = 1
        max_move = 0
        move_distance = int(board[x][y])
        for dx, dy in directions:
            nx, ny = x + dx * move_distance, y + dy * move_distance
            result = dfs(nx, ny)
            if result == -1:
                return -1
            max_move = max(max_move, result + 1)

        visited[x][y] = 0
        dp[x][y] = max_move
        return max_move

    result = dfs(0, 0)
    return result if result != -1 else -1

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
print(max_moves(board, N, M))
