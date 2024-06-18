''' 1트 => 6% 틀림.
[ 틀린 이유 ] ???
'''
# import sys
# k = int(input())
# for _ in range(k):
#     v, e = map(int, input().split())
#     edges = []
#     for _ in range(e):
#         edges.append(list(map(int, sys.stdin.readline().split())))
#     _set = [-1] * (v + 1)
#     flag = True
#     for v1, v2 in edges:
#         if _set[v1] == _set[v2]:
#             if _set[v1] == -1:          # 둘다 집합 초기화 안된 상태
#                 _set[v1], _set[v2] = False, True
#             else:                       # 둘은 같은 집합에 속하는 상태
#                 flag = False
#                 break
#         elif _set[v1] == -1 or _set[v2] == -1:
#             if _set[v1] == -1:
#                 _set[v1] = not _set[v2]
#             elif _set[v2] == -1:
#                 _set[v2] = not _set[v1]
#     if flag == True:
#         print("YES")
#     else:
#         print("NO")



''' 2트 => 답 참고.
1. bfs 돌리며 visited 배열에 해당 노드가 이분 집합 중 어디에 속하는지를 저장
    - 0: 미방문 / 1: 집합 A / -1: 집합 B
2. bfs 탐색 도중 인접 노드와 같은 집합에 속하는 노드가 존재한다면, False 를 리턴
3. 노드들이 동떨어져 있는 경우를 고려해주기 위해, 모든 노드들이 방문 처리될 때까지 bfs
'''
import sys
from collections import deque

k = int(input())

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = -1 * visited[cur]
            else:
                if visited[next] == visited[cur]:
                    return False
    return True

for _ in range(k):
    n,e = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    visited[0] = -1
    for _ in range(e):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    while 0 in visited:
        result = bfs(visited.index(0))
        if result == False: break

    if result == True: print("YES")
    else: print("NO")