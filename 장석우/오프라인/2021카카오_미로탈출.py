def solution(n, start, end, roads, traps):
    from collections import deque
    dists = [float('inf') for _ in range(n+1)]
    dists[start] = 0
    q = deque([[start,1]])
    visited = [[start,1]]
    while q:
        node, flag = q.popleft()
        cost = dists[node]
        print(dists, node, flag)
        if flag == 1:
            i = 0
            j = 1
        elif flag == -1:
            i = 1
            j = 0
        for road in roads:
            if road[i] == node:
                adjnode = road[j]
                dist = road[2]
                if dists[adjnode] > dist + cost:
                    dists[adjnode] = dist + cost
                    if adjnode in traps:
                        flag = -1 * flag
                        q.append([adjnode,flag])
                    else:
                        q.append([adjnode,flag])
    answer = dists[end]
    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps =[2,3]
print(solution(n, start, end, roads, traps))