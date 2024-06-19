# 1<=n<=10,000 , 1<=m<=50000, 1<=s,e<=n
# 시간제한 1초, 메모리제한 1024MB
# 연산횟수는 2000만번으로 빠듯하나, 데이터개수는 250,000,000개 정도

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

s, e = map(int,input().split())

def bfs(s, e, graph):
    visited = [False for _ in range(n+1)]
    q = deque([[s, 0]])
    e_dist = []
    while q:
        node, dist = q.popleft()
        if node == e:
            e_dist.append(dist)
            if len(e_dist) > 2:
                visited[node] = True
            else:
                visited[node] = False
        else:
            visited[node] = True
        for nextnode in graph[node]:
            if not visited[nextnode]:
                q.append([nextnode,dist+1])

    return e_dist

e_dist = bfs(s, e, graph)
print(e_dist[0] + e_dist[1])