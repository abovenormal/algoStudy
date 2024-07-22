N=int(input())
data=list(map(int,input().split()))
dp=[[0 for _ in range(21)] for _ in range(N)] # 열은 0~20 , 한 행씩 차례대로 계산
dp[0][data[0]]=1

for i in range(1,N-1):
    for j in range(21):
        if j-data[i] >=0:
            dp[i][j-data[i]]+=dp[i-1][j]
        if j+data[i]<=20:
            dp[i][j+data[i]]+=dp[i-1][j]


print(dp[-2][data[-1]])
#
# for i in range(N):
#     for j in range(21):
#         print(dp[i][j],end=' ')
#     print()

