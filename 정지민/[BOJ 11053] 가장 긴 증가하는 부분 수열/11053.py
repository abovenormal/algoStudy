n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i-1, -1, -1):
        if a[j] < a[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
