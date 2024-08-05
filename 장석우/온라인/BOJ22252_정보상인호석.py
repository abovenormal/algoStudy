# 시간제한2초, 메모리제한512MB
# 1<=q<=100,000, 1<=k<=100,000, 1<=c<=100,000, 1<=b<=100,000

import sys
import heapq

input = sys.stdin.readline

q = int(input())

infos = dict()
purchase = []
for i in range(q): # O(nlogn)
    tmp = input().split()
    a = int(tmp[0])
    name = tmp[1]
    if a == 1:
        try:
            for item in tmp[2:]:
                heapq.heappush(infos[name], -int(item))
        except:
            infos[name] = []
            for item in tmp[2:]:
                heapq.heappush(infos[name], -int(item))
    if a == 2:
        purchase.append((name,int(tmp[-1])))

res = 0

for name, cnt in purchase:
    for i in range(cnt):
        try:
            if not infos[name]: break
            res += heapq.heappop(infos[name])
        except:
            continue

print(-res)