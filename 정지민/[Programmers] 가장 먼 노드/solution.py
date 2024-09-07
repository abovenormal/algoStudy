import heapq

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)] 
    for v1, v2 in edge:
        graph[v1].append((v2, 1))
        graph[v2].append((v1, 1))
    
    distance = [1e9] * (n+1)
    distance[1] = 0
    
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, cur = heapq.heappop(q)
        
        if distance[cur] < dist: continue
        
        for _next, cost in graph[cur]:
            if dist + cost < distance[_next]:
                distance[_next] = dist + cost
                heapq.heappush(q, (dist + cost, _next))
    
    _max = max(distance[1:])
    for i in range(1, n+1):
        if distance[i] == _max:
            answer += 1

    return answer