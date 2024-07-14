''' 1트 => 정확성 79.5 점 (테케 3,4,5,6,7 실패)
1. 방문시간이 작은 노드부터 방문하기 위해 우선순위 큐를 사용한다.
    - cur == end 로 도착지점에 도착하면 바로 리턴하기 때문에, 우선순위 큐 필요!
2. 그래프 방향이 바뀜에 따라 (a -> b 방문) != (b -> a 방문) 이기 때문에 이 둘을 구분하기 위해 2차원 visited 배열 사용
    - visited[a][b] : a -> b 로 이동 시 최단시간 저장
    - a -> b 로 이동 시, 기존 visited[a][b] 에 저장된 최단시간보다 짧은 시간으로 이동할 수 있을 때만 visited 를 갱신 후 큐에 삽입
3. ori_graph, reverse_graph 두개를 둬서 그래프 방향에 따라 달라지는 경로 저장

[ 반례 ]
5, 1, 5, [[1, 2, 1], [2, 3, 1], [3, 2, 1], [3, 5, 1], [1, 5, 10]], [2, 3]
- 정답: 5 / 결과: 3

[ 틀린이유 ]
- 정답 경로: 1 -> 2 -> 3 -> 2 -> 3 -> 5
  결과 경로: 1 -> 2 -> 3 -> 5

 - 2 -> 3 으로 오면, 3 이 함정이라 5 로 바로 넘어갈 수 없다.
   현재 코드에서 cur == 함정, before == 함정 인 경우 ori_graph 를 따라가게 해놔서 틀림.
'''
# import heapq

# def bfs(start, end, n, traps, ori_graph, reverse_graph):
#     q = []
#     heapq.heappush(q, (0, start, start))
#     visited = [[-1]*(n+1) for _ in range(n+1)]

#     while q:
#         time, cur, before = heapq.heappop(q)

#         if cur == end:
#             return time

#         # cur 이 함정인 경우
#         if cur in traps:
#             if before not in traps:
#                 for _next, _cost in reverse_graph[cur]:
#                     if visited[cur][_next] != -1 and visited[cur][_next] <= cur + _cost:
#                         continue
#                     visited[cur][_next] = cur + _cost
#                     heapq.heappush(q, (time + _cost, _next, cur))
#             else:
#                 for _next, _cost in ori_graph[cur]:
#                     if visited[cur][_next] != -1 and visited[cur][_next] <= cur + _cost:
#                         continue
#                     visited[cur][_next] = cur + _cost
#                     heapq.heappush(q, (time + _cost, _next, cur))
#         else:
#             # cur 이 함정이 아닌 경우
#             for _next, _cost in ori_graph[cur]:
#                 if visited[cur][_next] != -1 and visited[cur][_next] <= cur + _cost:
#                     continue
#                 visited[cur][_next] = cur + _cost
#                 heapq.heappush(q, (time + _cost, _next, cur))

# def solution(n, start, end, roads, traps):
#     answer = 0

#     ori_graph = [[] for _ in range(n+1)]
#     reverse_graph = [[] for _ in range(n+1)]

#     for road in roads:
#         ori_graph[road[0]].append((road[1], road[2]))
#         reverse_graph[road[1]].append((road[0], road[2]))

#     answer = bfs(start, end, n, traps, ori_graph, reverse_graph)
#     return answer


''' 2트 => 답 참고.
1. trap 노드들이 눌렸는지, 안눌렸는지 여부 관리 - trap_pressed 배열을 큐에 넣고 관리한다!
    ex. v1 -> v2 로 이동할 시,
        v1 안눌림 & v2 안눌림 => 정방향 이동
        v1 또는 v2 가 눌린 상태 => 역방향
        v1 눌림 & v2 눌림 => 정방향
2. 노드 상태 관리
    - 하나의 노드 상태는 (노드 번호, 노드 뒤집힘 여부, 이웃 노드들 뒤집힘 여부) 로 관리한다.
'''
import heapq
from collections import defaultdict

def solution(n, start, end, roads, traps):
    traps = set(traps)

    graph = defaultdict(list)

    for u, v, w in roads:
        graph[u].append((v, w, False))  # (다음노드, cost, 역방향 엣지 여부)
        graph[v].append((u, w, True))

    trap_pressed = [False] * (n + 1)  # trap 노드들 눌림 여부 관리
    q = [(0, start, trap_pressed)]

    start_state = (start, False, tuple([False] * len(graph[start])))
    distance = {}
    distance[start_state] = 0

    while q:
        dist, cur, trap_pressed = heapq.heappop(q)

        cur_state = (cur, trap_pressed[cur], tuple(trap_pressed[_next] for _next, _, _ in graph[cur]))

        if dist > distance.get(cur_state, 1e9):
            continue

        for _next, _cost, is_reverse in graph[cur]:
            # cur -> _next 로의 엣지 뒤집힘 여부 판단
            edge_reversed = trap_pressed[cur] ^ trap_pressed[_next]

            # 유효한 엣지들에 대해 _next 노드로 이동
            if (is_reverse == False and edge_reversed == False) or (is_reverse == True and edge_reversed == True):
                next_trap_pressed = trap_pressed[:]
                if _next in traps:  # 다음 노드가 trap 이면, 눌린 상태로 설정
                    next_trap_pressed[_next] = not next_trap_pressed[_next]

                _next_state = (_next, next_trap_pressed[_next], tuple(next_trap_pressed[x] for x, _, _ in graph[_next]))

                if dist + _cost < distance.get(_next_state, 1e9):
                    distance[_next_state] = dist + _cost
                    heapq.heappush(q, (dist + _cost, _next, next_trap_pressed))

    candidates = [distance[k] for k in distance if k[0] == end]
    return min(candidates)