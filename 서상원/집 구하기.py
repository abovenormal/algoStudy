#34%에서 계속 틀립니다..

import heapq

N, E = map(int, input().split())
graph = [[] for _ in range(N + 3)]

for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

M, m_cost = map(int, input().split())
m_node = list(map(int, input().split()))
S, s_cost = map(int, input().split())
s_node = list(map(int, input().split()))

INF = int(1e9)
# N+1번은 맥도날드 가상노드
# N+2번은 스타벅스 가상노드
m_distance = [INF for _ in range(N + 3)]  # 맥도날드 , 스타벅스의 가상의 노드들 1개씩 추가
s_distance = [INF for _ in range(N + 3)]  # 맥도날드 , 스타벅스의 가상의 노드들 1개씩 추가

# 맥도날도 가상의 노드들로 이어주기
for m in m_node:
    graph[m].append((N + 1, 0))
    graph[N + 1].append((m, 0))
# 스타벅스 가상의 노드들로 이어주기
for m in s_node:
    graph[m].append((N + 2, 0))
    graph[N + 2].append((m, 0))
# 가상의 노드들 추가
m_node += [N + 1]
s_node += [N + 2]


def dijkstra(node, distance):
    distance[node] = 0
    q = []
    heapq.heappush(q, (0, node))

    while q:
        cost, node = heapq.heappop(q)
        if cost > distance[node]:
            continue

        for next, n_cost in graph[node]:
            t_cost = cost + n_cost
            if t_cost < distance[next]:
                distance[next] = t_cost  # 갱신
                heapq.heappush(q, (t_cost, next))


dijkstra(N + 1, m_distance)
dijkstra(N + 2, s_distance)

q = []
for node in range(1, N + 1):  # 모든 노드 탐색
    if node in m_node or node in s_node:
        continue

    if m_distance[node] <= m_cost and s_distance[node] <= s_cost:
        heapq.heappush(q, (m_distance[node] + s_distance[node], node))


if not q:
    print(-1)
else:
    cost, node = heapq.heappop(q)
    print(cost)
