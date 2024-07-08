# 시간제한 2초, 메모리제한 512MB
# n, m ~50
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [input()[:-1] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(graph)
def bfs(i, j):
    cnt = 1
    q = deque([(i,j,cnt)])
    visited = set()
    visited.add((i,j))
    cntlist = []
    while q:
        x, y, cnt = q.popleft()
        num = int(graph[x][y])
        cntlist.append(cnt)
        for i in range(4):
            nx, ny = x + dx[i] * num, y + dy[i] * num
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            elif graph[nx][ny] == 'H': continue
            elif (nx, ny) in visited:
                return -1
            else:
                q.append((nx, ny, cnt+1))
                visited.add((nx,ny))
    return max(cntlist)

res = bfs(0, 0)
print(res)