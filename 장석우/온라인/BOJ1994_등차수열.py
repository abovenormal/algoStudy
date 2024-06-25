# 시간제한1초, 메모리제한128MB

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
numlist = []
for _ in range(n):
    val = int(input())
    numlist.append(val)

numlist = list(numlist)
numlist.sort() # 리스트 변환 후 오름차순 정렬
print(numlist)
difflist = [] # 인접한 값들의 차이 저장
for i in range(len(numlist)-1):
    diff = numlist[i+1] - numlist[i]
    difflist.append(diff)

maxdiff = set(difflist)
maxdiff = list(maxdiff)
maxdiff.sort(reverse=True)

cntlist = []
for i in maxdiff:
    diffq = deque(difflist)
    cnt = 1
    maxcntlist = []
    tmpsum = 0
    while diffq:
        j = diffq.popleft()
        if i == j:
            cnt += 1
            tmpsum = 0
        elif i > j:
            tmpsum += j
            if i == tmpsum:
                cnt += 1
                tmpsum = 0
            if i < tmpsum:
                maxcntlist.append(cnt)
                tmpsum = 0
        elif i < j:
            maxcntlist.append(cnt)
            cnt = 1
            tmpsum = 0
    if cnt == 1:
        cnt = 0
    maxcntlist.append(cnt)
    cntlist.append(max(maxcntlist))

print(difflist,maxdiff,cntlist)
if cntlist:
    print(max(cntlist))
else:
    print(0)
