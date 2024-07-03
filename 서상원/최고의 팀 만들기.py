#틀린 코드이고 아직 이해를 다 못했습니다...
data=[]
for _ in range(30):
    b,w=map(int,input().split())
    data.append((b,w))

#black_sorted=sorted(data,key=lambda x: (-x[0])) # 1번째 원소로 내림차순
#white_sorted=sorted(data,key=lambda x: (-x[1])) # 2번째 원소로 내림차순

dp=[[-1 for _ in range(16)] for _ in range(16)] # dp는 2차원 테이블
dp[0][0]=0

for black,white in data:
    for i in range(15,-1,-1):
        for j in range(15,-1,-1):
            if dp[i][j]!=-1:
                if i<15:
                    dp[i+1][j]=max(dp[i+1][j],dp[i][j]+black)
                if j<15:
                    dp[i][j+1]=max(dp[i][j+1],dp[i][j]+white)

answer=0
for i in range(16):
    for j in range(16):
        if i+j==30:
            answer=max(answer,dp[i][j])

print(answer)







