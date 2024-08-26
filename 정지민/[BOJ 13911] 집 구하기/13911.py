'''
1. 다익스트라에서 가상노드 이용하기
    - 맥도날드가 여러개 있는 경우, <여러 개의 맥도날드 중, 각 집들에 가장 가까운 맥도날드 최단거리> 를 구해야 한다.
    - 여러 개의 맥도날드들에 대해 다익스트라를 매번 돌리면 시간초과.
    => '가상노드' 를 추가해서 이용하는 방법 사용
    - 모든 맥도날드들과 가중치 0 엣지로 연결된 가상노드(더미노드)를 추가한다.
    - 가상노드 사용 시, 맥도날드 노드가 1,5번이라 할때 
    '더미노드 > 1번노드 > 7번 집', '더미노드 > 5번노드 > 7번집' 두가지 케이스 중 더 최단거리로 distance[7] 업데이트가 가능하다.

2. 주의할 점
    : dijkstra 함수에서 최단거리를 찾을 때, 가상 노드를 이용한 경로를 찾아서는 안된다.
'''
import heapq
import sys

v,e = map(int, input().split())
graph = [[] for _ in range(v+3)]

for _ in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

mac, mac_cond = map(int, input().split())
macs = list(map(int, input().split()))

star, star_cond = map(int, input().split())
stars = list(map(int, input().split()))

def dijkstra(start):
    distance = [1e9] * (v+3)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        _dist, cur = heapq.heappop(q)

        if distance[cur] < _dist: continue

        for _next, _cost in graph[cur]:
            if _next == v+1 or _next == v+2: continue     # 가상 노드 이용 X
            cost = _dist + _cost
            if cost < distance[_next]:
                distance[_next] = cost
                heapq.heappush(q, (cost, _next))
    
    return distance

# 맥도날드 더미노드 (v+1) 추가 -> 모든 맥도날드 ~ 각각의 집들까지의 최단거리를 구함
for _mac in macs:
    graph[_mac].append((v+1, 0))
    graph[v+1].append((_mac, 0))

# 스타벅스 더미노드 (v+2) 추가 -> 모든 스타벅스 ~ 각각의 집들까지의 거리를 구함
for _star in stars:
    graph[_star].append((v+2, 0))
    graph[v+2].append((_star, 0))

mac_dist = dijkstra(v+1)
star_dist = dijkstra(v+2)

# 맥도날드 ~ 집 ~ 스타벅스 까지의 최단거리 합이 제일 작은 집 구하기 
# (단, 맥도날드 ~ 집, 집 ~ 스타벅스 까지의 거리가 세권을 만족해야 함)
answer = 1e9
for home in range(1, v+1):
    if home in macs or home in stars: continue
    if mac_dist[home] <= mac_cond and star_dist[home] <= star_cond:
        answer = min(answer, mac_dist[home] + star_dist[home])

if answer == 1e9:
    print(-1)
else:
    print(answer)