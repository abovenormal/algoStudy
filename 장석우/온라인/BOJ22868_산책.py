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

def bfs(s, e, graph, visited):
    q = deque([[s, 0, [s]]])
    while q:
        node, dist, route = q.popleft()
        print(node, dist, route)
        visited[node] = True
        if node == e:
            return dist, route
        for nextnode in graph[node]:
            if not visited[nextnode]:
                nextroute = route.copy()
                nextroute.append(nextnode)
                q.append([nextnode,dist+1,nextroute])

visited = [False for _ in range(n+1)]
se_dist, se_route = bfs(s, e, graph, visited)
visited = [False for _ in range(n+1)]
for i in se_route[1:-1]:
    visited[i] = True
es_dist, es_route = bfs(e, s, graph, visited)

print(se_route, se_dist + es_dist)