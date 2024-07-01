MOD = 1000000007
N, K = map(int, input().split())
S = input().strip()


dp = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]

if S[0] == '0': # leang zero인 경우
    dp[1][1][1] = 1
else: # 아닌 경우 
    dp[1][1][0] = 1

for i in range(2, N + 1):
    for j in range(1, i + 1):
        if S[i - 1] == '0':
            dp[i][j][0] = dp[i - 1][j][0] 
            dp[i][j][1] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) % MOD
        else:
            dp[i][j][0] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j][0]) % MOD

result=(dp[N][K][0] + dp[N][K][1]) % MOD

print(result)







