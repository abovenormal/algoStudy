#틀렸습니다..
#잘 모르겠습니다

import heapq

N, M, A, B = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))  # (next_node, cost)
    graph[b].append((a, cost))  # 무방향 그래프이므로 양쪽 다 추가

INF = int(1e9)
distance = [INF for _ in range(N + 1)]
distance[A] = 0  # 시작 노드의 거리를 0으로 설정

# 이전 노드를 저장하기 위한 리스트
previous = [[] for _ in range(N + 1)]

def dijkstra(start):
    q = [(0, start)]
    heapq.heapify(q)

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue

        for next_node, c in graph[node]:
            t_cost = cost + c
            if t_cost < distance[next_node]:
                distance[next_node] = t_cost
                heapq.heappush(q, (t_cost, next_node))
                previous[next_node] = [node]
            elif t_cost == distance[next_node]:
                previous[next_node].append(node)

def collect_nodes(node, visited_nodes):
    if node == A:
        visited_nodes.add(node)
        return
    for prev in previous[node]:
        visited_nodes.add(node)
        collect_nodes(prev, visited_nodes)

dijkstra(A)

# 최단 경로에 속한 모든 노드를 저장할 set
visited_nodes = set()
collect_nodes(B, visited_nodes)
result=list(visited_nodes)
result.sort()


# 최단 경로에 속한 모든 노드 출력
print(len(visited_nodes))
print(' '.join(map(str,result)))
