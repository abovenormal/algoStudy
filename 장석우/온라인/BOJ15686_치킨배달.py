# 시간제한 1초, 메모리제한 512MB
# 2<=n<=50, 1<=m<=13
# bfs 시간복잡도 O(n*n + 간선개수) * m = 3000*m내외

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
chickens = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(len(line)):
        if line[j] == 2:
            chickens.append((i,j))

def bfs(i, j):
    q = deque([[i, j, 0]])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[i][j] = True
    while q:
        x, y, dist = q.popleft()
        if graph[x][y] == 1:
            dists[(i, j)].append((x, y, dist))
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            if not visited[nx][ny]:
                q.append([nx,ny,dist+1])
                visited[nx][ny] = True
    return

dists = {}
for chicken in chickens:
    i, j = chicken
    dists[chicken] = []
    bfs(i, j)
for key in dists.keys():
    dists[key].sort()

ans = []
for case in combinations(chickens, m):
    res = []
    for i, j in case:
        val = []
        for chick_dist in dists[(i,j)]:
            val.append(chick_dist[2])
        res.append(val)

    total = 0
    for j in range(len(res[0])):
        minvalue = float('inf')
        for i in range(len(res)):
            if res[i][j] < minvalue:
                minvalue = res[i][j]
        total+=minvalue
    ans.append(total)
print(min(ans))

