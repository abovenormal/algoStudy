#시간제한1초, 메모리제한256MB
#1<=n,k<=300,000, 0<=m,v<=1,000,000, 1<=c<=100,000,000
#O(nlogn)까지 접근 가능, 완전탐색불가, 그리디로 접근

import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
jewels = []
for _ in range(n):
    heapq.heappush(jewels, list(map(int,input().split())))
bags = [int(input()) for _ in range(k)]
bags.sort()

res=0
tmp=[]
for bag in bags: #앞에서 담은 가방은 뒤에서 또 담을 수 있기 때문에 중복체크 x
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewels)[1])
    if tmp:
        res -= heapq.heappop(tmp)
    elif not jewels:
        break

print(res)