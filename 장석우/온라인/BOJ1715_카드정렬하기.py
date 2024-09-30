# 시간제한2초, 메모리제한128MB

import sys
import heapq

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    num = int(input())
    heapq.heappush(nums, num)

res = 0

if n >= 2:
    while len(nums) > 1:
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        sumnum = num1 + num2
        res += sumnum
        heapq.heappush(nums, sumnum)


print(res)
