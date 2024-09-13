
n = 4
tops = [1,1,0,1]

dp = [[tops[i],0] for i in range(n)]
dp2 = [0 for i in range(n)]
if dp[0][0]:
    dp[0][1] = 4
    dp2[0] = 3
else:
    dp[0][1] = 3
    dp2[0] = 2
for i in range(1,n):
    if dp[i][0]:
        dp[i][1] = dp[i-1][1] * 3 + dp2[i-1]
        dp2[i] = dp[i-1][1] * 2
    else:
        dp[i][1] = dp[i-1][1] * 2 + dp2[i-1]
        dp2[i] = dp[i-1][1]
    print(dp, dp2)
answer = dp[n-1][1] % 10007

print(answer)