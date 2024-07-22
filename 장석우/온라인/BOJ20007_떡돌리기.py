#시간제한1초, 메모리제한512MB
#2<=n<=1000, 1<=m<=100,000, 1<=x<=10,000,000, 0<=y<=n
#0<=a,b<=n, 1<=c<=10,000
#완전탐색불가

import sys
import heapq
from collections import deque

input = sys.stdin.readline

n,m,x,y = map(int,input().split())
dists = [float('inf')] * n

graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijkstra(start): #O(mlogn)
    q = []
    dists[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        curdist, curnode = heapq.heappop(q)
        if curdist > dists[curnode]: continue
        for nxtdist, nxtnode in graph[curnode]:
            cost = curdist + nxtdist
            if cost < dists[nxtnode]:
                dists[nxtnode] = cost
                heapq.heappush(q, (cost, nxtnode))

dijkstra(y)

dists.sort()
dists = deque(dists[1:])
res = 0
maximum = x
while dists:
    dist = dists.popleft()
    if maximum == x and dist > maximum//2:
        res = -1
        break
    if dist <= maximum//2:
        maximum -= 2*dist
    if dist > maximum//2:
        res += 1
        maximum = x

print(res)