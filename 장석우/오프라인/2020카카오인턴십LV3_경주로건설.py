# board는 3~25사이 정사각 배열

import copy

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

def solution(board):
    global dx, dy
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    _visited = [[float('inf')] * n for _ in range(n)]
    visited = copy.deepcopy(_visited)
    visited[0][0] = 0
    tmp1, tmp2 = float('inf'), float('inf')
    if board[0][1] == 0:
        dfs(0,0,1,visited,board)
        tmp1 = visited[n-1][n-1]
        print(visited)
        visited = copy.deepcopy(_visited)
        visited[0][0] = 0
    if board[1][0] == 0:
        dfs(0,0, -1, visited,board)
        tmp2 = visited[n-1][n-1]
        print(visited)
    answer = min(tmp1, tmp2)
    return answer


def dfs(i,j,dir,visited,board):
    cost = visited[i][j]
    for k in range(4):
        if k == 0 or k == 2:
            ndir = -1
        if k == 1 or k == 3:
            ndir = 1
        if i == 0 and j == 0 and dir != ndir:
            continue
        ni, nj = i + dx[k], j + dy[k]
        if ni<0 or ni>len(board)-1 or nj<0 or nj>len(board)-1:
            continue
        if board[ni][nj] == 1: continue
        if dir == ndir:
            ncost = cost + 100
        if dir != ndir:
            ncost = cost + 600
        if ncost < visited[ni][nj]:
            visited[ni][nj] = ncost
            dfs(ni,nj,ndir,visited,board)

print(solution(board))