from collections import deque

def solution(land):
    answer = 0
    N=len(land) # 행
    M=len(land[0]) # 열
    visited=[[False for _ in range(M)] for _ in range(N)]
    result=[0 for _ in range(M)] # 최종 값이 저장될 list
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def bfs(x,y,result):
        visited[x][y]=True
        collums=set()
        collums.add(y)
        cnt=1
        q=deque([(x,y)])
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and land[nx][ny]==1:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    cnt+=1
                    collums.add(ny)
        
        for c in collums:
            result[c]+=cnt
        
        return 
    
    for i in range(N):
        for j in range(M):
            if visited[i][j]==False and land[i][j]==1:
                bfs(i,j,result)
    
    
                
    answer=max(result)
                    
  
    
    return answer
