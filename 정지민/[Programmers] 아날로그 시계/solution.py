def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 초로 환산
    cur_time = h1 * 60 * 60 + m1 * 60 + s1
    end_time = h2 * 60 * 60 + m2 * 60 + s2
    
    # 시작 지점에 겹쳐있는 경우
    if cur_time == 0 or cur_time == 12 * 3600:
        answer += 1
    
    # 1초씩 증가시켜 가면서, 겹침 판단
    # (현재 분침 위치 > 현재 초침 위치) && (1초뒤 분침 위치 <= 1초뒤 초침 위치) 라면 1초 사이에 겹침이 발생한 것으로 판단
    while cur_time < end_time:
        # 현재 시/분/초침의 위치 구하기
        # (시침: 1초에 1/120도 | 분침: 1초에 1/10도 | 초침: 1초에 6도씩 이동)
        cur_h = cur_time / 120 % 360
        cur_m = cur_time / 10 % 360
        cur_s = cur_time * 6 % 360
        
        # 1초 뒤 시/분/초침의 위치 구하기
        # 1초 뒤 위치가 360 도가 되면 360도로 처리해 주어야 위 조건문을 적용할 수 있다.
        next_h = (cur_time+1) / 120 % 360
        next_m = (cur_time+1) / 10 % 360
        next_s = (cur_time+1) * 6 % 360
        if next_h == 0: next_h = 360
        if next_m == 0: next_m = 360
        if next_s == 0: next_s = 360
        
        if cur_s < cur_h and next_s >= next_h:
            answer += 1
        if cur_s < cur_m and next_s >= next_m:
            answer += 1
        # 시/분/초침이 모두 중복하여 겹쳐 있는 경우, 한번만 카운트
        if next_s == next_m and next_s == next_h:
            answer -= 1
        
        cur_time += 1
                
    return answer