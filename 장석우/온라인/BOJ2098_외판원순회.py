# 시간제한 1초, 메모리제한 128MB
# 2<=n<=16

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            w[i][j] = float('inf')
def search(start):
    nvisit = set([i for i in range(n)])
    nvisit.remove(start)
    visited = set([start])
    q = deque([(0, start)])
    totalcost = 0
    while q:
        cost, node = q.popleft()
        totalcost += cost
        nxtcost = float('inf')
        nxtnode = -1
        for i in range(n):
            if i in visited: continue
            if w[node][i] < nxtcost:
                nxtcost = w[node][i]
                nxtnode = i

        if nxtnode != -1:
            q.append((nxtcost,nxtnode))
            nvisit.remove(nxtnode)
            visited.add(nxtnode)
        if nxtnode == -1:
            totalcost += w[node][start]
    return totalcost

answer = float('inf')
for i in range(n):
    res = search(i)
    answer = min(answer, res)
print(answer)



