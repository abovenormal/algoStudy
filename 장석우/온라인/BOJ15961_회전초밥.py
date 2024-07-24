#시간제한 1초, 메모리제한 512MB
#2<=n<=3,000,000, 2<=d<=3,000, 2<=k<=3,000

import sys
input = sys.stdin.readline

n, d, k, c = map(int,input().split())

dishes = [int(input()) for _ in range(n)]

cntlist = [0] * (d+1)
cntlist[c] = 1
cnt = 1

for i in range(k):
    cntlist[dishes[i]] += 1
    if cntlist[dishes[i]] == 1:
        cnt += 1

res = cnt

for s in range(n-1):
    e = s+k
    cntlist[dishes[s]] -= 1
    if cntlist[dishes[s]] == 0:
        cnt -= 1
    cntlist[dishes[e%n]] += 1
    if cntlist[dishes[e%n]] == 1:
        cnt += 1
    res = max(cnt, res)

print(res)

