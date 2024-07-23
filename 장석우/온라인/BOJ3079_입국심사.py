#시간제한1초, 메모리제한128MB
#1<=n<=100,000, 1<=m<=1,000,000,000, 1<=t<=10**9
#O(logm)이하 알고리즘으로만 접근가능

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

times = [int(input()) for _ in range(n)]

left = min(times)
right = max(times) * m
res = float('inf')

while left<=right:
    mid = (left+right) // 2
    total = 0
    for time in times:
        total += mid//time

    if total >= m:
        right = mid - 1
        if mid < res:
            res = mid

    elif total < m:
        left = mid + 1

print(res)