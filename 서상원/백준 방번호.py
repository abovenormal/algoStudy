N=int(input())
data=list(map(int,input().split()))
M=int(input())
INF=int(1e9)
dp=[-INF for _ in range(M+1)]

for i in range(N-1,-1,-1):
    x=data[i]
    for j in range(x,M+1):
        dp[j]=max(dp[j-x]*10+i  , i , dp[j])

print(dp)
print(dp[M])
