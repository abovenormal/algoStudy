import sys
INF=int(1e5)
sys.setrecursionlimit(INF)

N,M=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(input()))

max_value=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
dp=[[0 for _ in range(M)] for _ in range(N)] # dp
visited=[[False for _ in range(M)] for _ in range(N)]

def dfs(x,y,cost,move):
    global max_value
    move=int(move) # str -> int
    max_value=max(max_value,cost)


    for i in range(4):
        nx=x+dx[i]*move # 숫자 값 만큼 이동
        ny=y+dy[i]*move
        if 0<=nx<N and 0<=ny<M and data[nx][ny]!='H' and cost+1 > dp[nx][ny]: # 유효 범위 , cost+1의 값이 기존 dp에 저장된 값 보다 커야 함
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny]=cost+1
                visited[nx][ny]=True
                dfs(nx,ny,cost+1,data[nx][ny])
                visited[nx][ny]=False



dfs(0,0,1,data[0][0])
print(max_value)
