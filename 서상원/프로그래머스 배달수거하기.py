def solution(cap, n, deliveries, pickups):
    d_clear=[False for _ in range(n)]
    p_clear=[False for _ in range(n)]
    answer=0
    
    for i in range(n): # clear처리 
        if deliveries[i]==0:
            d_clear[i]=True
        if pickups[i]==0:
            p_clear[i]=True

    
    while (False in d_clear and False in p_clear): # 하나라도 처리가 안된 곳이 있다면 반복 
        can_d=cap # 배달 할 수 있는량은 cap
        can_p=0 # 현재 수거량 0 
        max_cost=0
        
        for i in range(n-1,-1,-1): # 뒤에서부터 계산
            if d_clear[i]==True and p_clear[i]==True: # clear라면 continue
                continue
            else: # 택배 배달 or 수거 
                if d_clear[i]==False and can_d-deliveries[i]>=0 : #  전부 배달 가능하다면
                    d_clear[i]=True
                    can_d-=deliveries[i] # 현재 배달 가능량 갱신
                    deliveries[i]=0 # 배달완료 
                elif d_clear[i]==False and can_d-deliveries[i]<0 : # 전부 배달이 안되면 일부만 배달 
                    deliveries[i]-=can_d # 현재 배달 가능량 갱신
                    can_d=0 # 배달 가능량 0
                    
                if p_clear[i]==False and can_p+pickups[i]<=cap: # 전부 수거 가능하다면
                    p_clear[i]=True
                    can_p+=pickups[i]
                    pickups[i]=0 # 수거 완료 
                elif p_clear[i]==False and can_p+pickups[i]>cap: # 전부 수거가 안된다면 일부만 수거
                    pickups[i]-=(cap-can_p)
                    can_p=cap # 수거 가능량 0
                max_cost=max(max_cost,i+1)
                
        
        answer+=max_cost*2

    
    return answer
