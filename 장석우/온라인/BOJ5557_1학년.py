# 시간제한1초, 메모리제한128MB
# 3<=n<=100, 정수범위 0~9

import sys

n = int(input())
nums = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n-1)]

dp[0][nums[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if nums[i]+j<=20: dp[i][nums[i]+j] += dp[i-1][j]
        if j-nums[i]>=0: dp[i][j-nums[i]] += dp[i-1][j]

print(dp)
print(dp[-1][nums[-1]])