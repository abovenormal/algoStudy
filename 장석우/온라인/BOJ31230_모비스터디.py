# 시간제한2초, 메모리제한1024MB
# 2<=n<=200,000, 1<=m<=300,000, 1<=a,b<=n
# 힙큐이용한 다익스트라로 접근, O(mloge)

import sys
import heapq
import copy

input = sys.stdin.readline
n, m, a, b = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2, d = map(int,input().split())
    graph[n1].append((d,n2))
    graph[n2].append((d,n1))

dists = [[float('inf'), set()] for _ in range(n+1)]
dists[a][0] = 0
dists[a][1].add(a)

q = []
heapq.heappush(q,(0,a))
while q:
    nowdist, nownode = heapq.heappop(q)
    if nowdist > dists[nownode][0]: continue
    for nxtdist, nxtnode in graph[nownode]:
        cost = nowdist+nxtdist
        if cost < dists[nxtnode][0]:
            print(dists[nownode][1], dists[nxtnode][1])
            dists[nxtnode][0] = cost
            heapq.heappush(q,(cost,nxtnode))
            dists[nxtnode][1] = copy.deepcopy(dists[nownode][1])
            dists[nxtnode][1].add(nxtnode)
            print(dists[nxtnode][1])
        elif cost == dists[nxtnode][0]:
            dists[nxtnode][1].add(nxtnode)
            dists[nxtnode][1] = dists[nxtnode][1].union(dists[nownode][1])

tmp = list(dists[b][1])
tmp.sort()
print(len(tmp))
tmp = list(map(str, tmp))
tmp = ' '.join(tmp)
print(tmp)