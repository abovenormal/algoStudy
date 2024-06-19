# 시간제한 2초 => 4000만번 연산 가능
# 메모리제한 256MB => 데이터 개수 50,000,000개 이내
# 2 ≤ K ≤ 5
# 1 ≤ V ≤ 20,000
# 1 ≤ E ≤ 200,000

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())

def bfs(startnode, graph, visited, connected):
    q = deque([startnode])
    connected[startnode] = 1
    while q:
        node = q.popleft()
        for neighbour in graph[node]:
            if connected[neighbour] != connected[node]:
                connected[neighbour] = -1 * connected[node]
            else:
                return False
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = set()
    connected = [0 for _ in range(len(graph))]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    for vertex in range(1, v+1):
        if vertex not in visited:
            yn = bfs(vertex, graph, visited, connected)
            if not yn:
                print('NO')
                break
    if yn:
        print('YES')



