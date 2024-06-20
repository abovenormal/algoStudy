# 시간제한 2초, 메모리제한 128MB
# X[i] <= 1,000,000,000 , 1 <= A[i] <= 1,000,000,000
# 1<=n<=100,000
# n이 크므로 O(nlogn)이하의 알고리즘 고려

import sys

input = sys.stdin.readline
n = int(input())

towns = [list(map(int, input().split())) for _ in range(n)]
towns.sort(key=lambda x : x[0])
total = 0
for town in towns:
    total += town[1]

cnt = 0
for town in towns:
    location = town[0]
    cnt += town[1]
    if cnt >= total/2:
        break

print(location)