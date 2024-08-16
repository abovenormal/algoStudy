# n, m ~ 500
# 정확성, 효율성 점수 있음

def solution(land):
    n = len(land)
    m = len(land[0])
    petroleum = []
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue
            tmp = bfs(i, j, land, visited)
            if tmp:
                petroleum.append(tmp)
    print(petroleum)
    answer = 0
    cnt = 0
    for j in range(m):
        for p in petroleum:
            flag = False
            for x, y in p:
                if j == y:
                    flag = True
                    break
            if flag:
                cnt += len(p)
        answer = max(answer, cnt)
        cnt = 0

    return answer

def bfs(i,j,graph,visited):
    from collections import deque
    n = len(graph)
    m = len(graph[0])
    q = deque([(i,j)])
    arr = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        if graph[x][y] == 0: continue
        else:
            arr.append((x, y))
            visited[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if graph[nx][ny] == 0 : continue
                if not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

    return arr


land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))