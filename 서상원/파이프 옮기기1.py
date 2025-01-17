#DFS 풀이
N=int(input())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

# DFS(완전탐색) : 매번 3가지의 경우의 수를 다 실행
# 1. 파라미터 : status , 좌표

status=0 # 0,1,2는 순서대로 가로 , 세로 , 대각선
answer=0



def dfs(status,x,y):
    global answer
    if x==N-1 and y==N-1:
        answer+=1
        return

    if status==0 and y<N-1: # 가로 또는 대각선으로만 이동 가능
        if y<N-1 and data[x][y+1]==0: # 가로로 이동 할 수 있다면은 이동
            dfs(0,x,y+1)
        if x<N-1 and y<N-1 and data[x][y+1]==0 and data[x+1][y]==0 and data[x+1][y+1]==0: # 대각선으로 이동 할 수 있다면은 이동
            dfs(2,x+1,y+1)

    elif status==1 and x<N-1: # 세로 또는 대각선으로만 이동 가능
        if x<N-1 and  data[x+1][y]==0:
            dfs(1,x+1,y)
        if x<N-1 and y<N-1 and data[x][y+1]==0 and data[x+1][y]==0 and data[x+1][y+1]==0:
            dfs(2,x+1,y+1)


    elif status==2: # 가로 , 세로 , 대각선으로 이동 가능
        if y<N-1 and data[x][y+1]==0:
            dfs(0, x, y + 1)
        if x<N-1 and data[x+1][y]==0:
            dfs(1,x+1,y)
        if x<N-1 and y<N-1 and data[x][y + 1] == 0 and data[x + 1][y] == 0 and data[x + 1][y + 1] == 0:
            dfs(2, x + 1, y + 1)


dfs(0,0,1)

print(answer)


# DP 풀이
#N의 최대 크기는 16
#가로 -> 가로 , 대각
#세로 -> 세로 , 대각
#대각 -> 가로 , 세로 , 대각
N=int(input())
data=[]
shape=1 #가로 1, 세로 2 , 대각 3
x,y=0,1
for _ in range(N):
    data.append(list(map(int,input().split())))

dp=[[[0] * 3 for _ in range(N)] for _ in range(N)]

#0,1,2 가로,세로,대각선

dp[0][1][0]=1
for i in range(2,N):
    if data[0][i]==0:
        dp[0][i][0]=1
    else:
        break

for i in range(1,N):
    for j in range(2,N):
        if data[i][j]==0 and data[i-1][j]==0 and data[i][j-1]==0: # 대각
            dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

        if data[i][j]==0:
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]
            dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]

result=sum(dp[N-1][N-1])
print(result)



