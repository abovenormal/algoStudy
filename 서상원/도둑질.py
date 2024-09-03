def solution(money):
    answer = 0
    n=len(money)
    dp1=[0 for _ in range(n)]
    dp1[0]=money[0]
    
    dp2=[0 for _ in range(n)]
    
    #이전 집을 털은 경우 
    for i in range(1,n-1): # 마지막 집은 못텀 
        dp1[i]=max(dp1[i-1] , dp1[i-2]+money[i])
    
    #이전 집을 안 턴 경우 
    for i in range(1,n):
        dp2[i]=max(dp2[i-2]+money[i] , dp2[i-1])
    
    answer=max(dp1[-2],dp2[-1])
    
    
    
    
    return answer
