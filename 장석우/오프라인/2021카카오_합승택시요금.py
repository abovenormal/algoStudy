import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for i,j,c in fares:
        graph[i].append((j,c))
        graph[j].append((i,c))
    distgraph = find(graph, n)
    print(distgraph)
    minfare = float('inf')
    answer = float('inf')
    for i in range(1, n+1):
        if i == s:
            minfare = distgraph[i][a] + distgraph[i][b]
        else:
            minfare = distgraph[s][i] + distgraph[i][a] + distgraph[i][b]
        print(answer, minfare)
        answer = min(answer, minfare)
    return answer


def find(graph, n): #O(n**2*logn)알고리즘 = 40000*log200
    dists = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dists[i][i] = 0
        q = []
        heapq.heappush(q,(0,i))
        while q:
            cost, node = heapq.heappop(q)
            if cost < dists[i][node] : continue
            for nxtnode, nxtcost in graph[node]:
                totalcost = cost + nxtcost
                if totalcost < dists[i][nxtnode]:
                    dists[i][nxtnode] = totalcost
                    heapq.heappush(q,(totalcost, nxtnode))
    return dists

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n,s,a,b,fares)