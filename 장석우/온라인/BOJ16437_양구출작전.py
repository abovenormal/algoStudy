#시간제한1초, 메모리제한256MB
#2<=n<=123,456, 1<=a<=10**9, 1<=p<=n

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
wolfs = [0] * (n+1)
sheep = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(2,n+1):
    t, a, p = input().split()
    if t == 'S':
        sheep[i] = int(a)
    elif t == 'W':
        wolfs[i] = int(a)
    graph[i].append(int(p))

def search(node):
    visited = [0] * (n+1)
    visited[node] = 1
    scnt = [sheep[node]]
    sheep[node] = 0
    q = deque([(node,scnt)])
    while q:
        nownode, nowscnt = q.popleft()

        if nownode == 1:
            return sum(nowscnt)
        for nxtnode in graph[nownode]:
            if not visited[nxtnode]:
                if sheep[nxtnode]:
                    nowscnt.append(sheep[nxtnode])
                    sheep[nxtnode] = 0
                if wolfs[nxtnode]:

                    for i in range(len(nowscnt)):
                        cnt = nowscnt[i] - wolfs[nxtnode]
                        if cnt < 0: cnt = 0
                        nowscnt[i] = cnt

                q.append((nxtnode, nowscnt))
                visited[nxtnode] = 1
    return -1

total = 0
for i in range(2, n+1):
    if not sheep[i]: continue
    else:
        total += search(i)

print(total)