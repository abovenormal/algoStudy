#시간제한1초, 메모리제한512MB
#3<=n,m<=15, 1<=d<=10

import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n,m,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

locations = [i for i in range(m)]
def bfs(x,y):
    q = deque([(x,y,0)])
    dx = [0,-1,0]
    dy = [-1,0,1]
    visited = []
    while q:
        i,j,dist = q.popleft()
        visited.append((i,j))
        for k in range(3):
            ni, nj = i + dx[k], j + dy[k]
            if ni < 0 or ni > n-1 or nj < 0 or nj > m-1:
                continue
            if (ni,nj) not in visited and dist+1 <= d:
                q.append((ni,nj,dist+1))
                if _graph[ni][nj] == 1:
                    eliminated.add((ni, nj))
                    return True
    return False

maxcnt = 0
for x1,x2,x3 in combinations(locations, 3):
    cnt = 0
    _graph = copy.deepcopy(graph)
    for i in range(n):
        eliminated = set()
        bfs(n, x1)
        bfs(n, x2)
        bfs(n, x3)
        if eliminated:
            for x, y in list(eliminated):
                _graph[x][y] = 0
        cnt += len(list(eliminated))
        _graph = [[0 for _ in range(m)]] + _graph[:n-1]
    if cnt > maxcnt:
        maxcnt = cnt

print(maxcnt)


