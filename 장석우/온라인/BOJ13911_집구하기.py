# 시간제한1초, 메모리제한256MB

import heapq
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 3)]


macV = n + 1
starV = n + 2

for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

mac, macinHome = map(int, input().split())
macList = list(map(int, input().split()))
star, starinHome = map(int, input().split())
starList = list(map(int, input().split()))


for i in macList:
    adj[macV].append([i, 0])
    adj[i].append([macV, 0])

for i in starList:
    adj[starV].append([i, 0])
    adj[i].append([starV, 0])


hq = []
cost = [float('inf')] * (n + 3)
cost[macV] = 0
heapq.heappush(hq, [0, macV])

while hq:
    t, x = heapq.heappop(hq)
    if cost[x] != t: continue
    for nx, nt in (adj[x]):
        if nx == macV or nx == starV: continue

        if cost[nx] > t + nt:
            cost[nx] = t + nt
            heapq.heappush(hq, [cost[nx], nx])


hq = []
costt = [float('inf')] * (n + 3)
costt[starV] = 0
heapq.heappush(hq, [0, starV])

while hq:
    t, x = heapq.heappop(hq)
    if costt[x] != t: continue
    for nx, nt in (adj[x]):
        if nx == macV or nx == starV: continue

        if costt[nx] > t + nt:
            costt[nx] = t + nt
            heapq.heappush(hq, [costt[nx], nx])

ans = float('inf')
for i in range(1, n + 1):
    if i in macList: continue
    if i in starList: continue
    if cost[i] <= macinHome and costt[i] <= starinHome: ans = min(ans, cost[i] + costt[i])
if ans == float('inf'):
    print(-1)
else:
    print(ans)