''' 1트 => 테케 8 ~ 26 시간초과. (35.9 / 100 점)
'''
from collections import deque

def bfs(n, graph, start):    # start 에서 bfs 돌렸을 때, (start 로 몇번 되돌아오는지, 해당 사이클 구성 집합) 리턴
    q = deque([start])
    visited = [-1] * (n+1)
    visited[start] = 0
    cycles = set()
    
    while q:
        cur = q.popleft()
        cycles.add(cur)
        
        if cur == start and visited[start] != 0:
            continue
        
        for _next in graph[cur]:
            if visited[_next] == -1 or _next == start:
                visited[_next] += 1
                q.append(_next)
    
    return visited[start], cycles
    
def solution(edges):
    answer = []
    extra_node = 0
    eight_cnt = 0
    donut_cnt = 0
    stick_cnt = 0
    
    n = 0           # 전체 노드 개수
    for v1, v2 in edges:
        n = max(n, v1, v2)
    
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
    
    # 각 노드가 어디 속하는지 찾아냈는지 여부
    found = [False] * (n+1)
    found[0] = True
        
    # 팔자, 도너츠 구성 노드 집합 set
    eights = set()
    donuts = set()
    
    # 팔자 모양 찾기
    # (어떤 정점(출발지점) 에서 bfs 돌렸을때, 출발지점으로 2번 돌아옴)
    for start_node in range(1, n+1):
        if found[start_node] == False:
            cnt, cycles = bfs(n, graph, start_node)
            if cnt == 2:
                eight_cnt += 1
                for cycle in cycles:
                    found[cycle] = True
                    eights.add(cycle)
    
    # 도넛 모양 찾기
    # (어떤 정점에서 bfs 돌렸을 때, 출발 지점으로 1번만 돌아옴)
    for start_node in range(1, n+1):
        if found[start_node] == False:
            cnt, cycles = bfs(n, graph, start_node)
            if cnt == 1:
                donut_cnt += 1
                for cycle in cycles:
                    found[cycle] = True
                    donuts.add(cycle)
    
    # 추가 정점은 나가는 엣지 개수가 2 이상이고, 들어오는 엣지가 0개인 정점
    out_edge = [0] * (n+1)
    in_edge = [0] * (n+1)
    for v1, v2 in edges:
        out_edge[v1] += 1
        in_edge[v2] += 1
    for node in range(1, n+1):
        if out_edge[node] >= 2 and in_edge[node] == 0:
            extra_node = node
    
    # 추가 정점에서 연결된 노드 중 (도넛 or 팔자 에 속하지 않는 노드 개수) 가 막대모양 그래프 개수임!
    for _next in graph[extra_node]:
        if found[_next] == False:
            if (_next not in eights) and (_next not in donuts):
                stick_cnt += 1
    
    answer.append(extra_node)
    answer.append(donut_cnt)
    answer.append(stick_cnt)
    answer.append(eight_cnt)
    return answer



''' 2트 => 답 참고.
1. 그래프 완탐으로 순회 시 시간초과?
2. 엣지의 특징을 이용해 각 그래프를 구분한다.
    - 생성된 정점: 나가는 간선 수가 2이상, 들어오는 간선 수가 0
    - 막대 모양 그래프 개수: 나가는 간선 수가 0, 들어오는 간선 수가 1인 노드의 개수
    - 8자 모양 그래프 개수: 나가는 간선 수가 2, 들어오는 간선 수가 2인 노드의 개수
    - 도넛 모양 그래프 개수: 생성된 정점에서 나가는 간선 수 - (막대모양 + 8자모양 그래프 수 합)
'''
def solution(edges):
    answer = []
    extra_node = 0
    eight_cnt = 0
    donut_cnt = 0
    stick_cnt = 0

    n = 0                       # 전체 노드 개수
    for v1, v2 in edges:
        n = max(n, v1, v2)
    
    out_edge = [0] * (n+1)
    in_edge = [0] * (n+1)
    for v1, v2 in edges:
        out_edge[v1] += 1
        in_edge[v2] += 1
    
    for node in range(1, n+1):
        if out_edge[node] >= 2 and in_edge[node] == 0:
            extra_node = node
        elif out_edge[node] == 0 and in_edge[node] >= 1:        # 추가 정점에서 들어오는 엣지를 고려하여 in_edge[node] >= 1
            stick_cnt += 1
        elif out_edge[node] == 2 and in_edge[node] >= 2:        # 추가 정점에서 들어오는 엣지를 고려하여 in_edge[node] >= 2
            eight_cnt += 1
    donut_cnt = out_edge[extra_node] - (stick_cnt + eight_cnt)
    
    answer.append(extra_node)
    answer.append(donut_cnt)
    answer.append(stick_cnt)
    answer.append(eight_cnt)
    return answer





















