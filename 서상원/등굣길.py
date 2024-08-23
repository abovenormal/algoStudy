
def solution(m, n, puddles): 
    answer = 0
    data=[[0 for _ in range(m)] for _ in range(n)]
    MOD = 1000000007
    
    for x,y in puddles:
        data[y-1][x-1]=-1
    
    for i in range(m): # 열 , 기본 값 채워주기 
        if data[0][i]==-1:
            break
        data[0][i]=1
    
    for j in range(n): # 행 , 기본 값 채워주기 
        if data[j][0]==-1:
            break
        data[j][0]=1
    
    
    for i in range(1,n):
        for j in range(1,m):           
            if data[i][j]==-1: # 해당 좌표가 puddle이면 pass
                continue
            else:
                if data[i-1][j]==-1 and data[i][j-1]==-1: # 위쪽,왼쪽에 둘 다 puddle이 있는 경우 
                    continue
                elif data[i][j-1]==-1: # 왼쪽에 puddle이 있는 경우 
                    data[i][j]=data[i-1][j]
                elif data[i-1][j]==-1: # 위쪽에 puddle이 있는 경우 
                    data[i][j]=data[i][j-1]
                else:
                    data[i][j]=(data[i-1][j]+data[i][j-1])%MOD
            
        
    
    
    # 출력문 
    # for i in range(n): 
    #     for j in range(m):
    #         print(data[i][j],end=' ')
    #     print()
    answer=data[n-1][m-1]
            
        
            
                
            
    
    return answer
```
