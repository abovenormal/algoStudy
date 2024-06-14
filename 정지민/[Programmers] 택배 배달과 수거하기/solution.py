''' 1트 => 테케 16,17,19,20 시간초과. 80% 성공.
'''
def solution(cap, n, deliveries, pickups):
    answer = 0

    d_avail = cap
    p_avail = cap

    for i in range(n - 1, -1, -1):
        # 배달할 거나, 수거할게 존재하면, i 번째까지 가야한다.
        while deliveries[i] > 0 or pickups[i] > 0:
            d_avail = cap
            p_avail = cap
            answer += (i + 1)
            if deliveries[i] >= cap:  # 그 위치에 온전히 배달
                deliveries[i] -= cap
            else:
                d_avail -= deliveries[i]
                deliveries[i] = 0
                if d_avail > 0:  # 앞 집들에도 배달할 수 있음
                    for j in range(i - 1, -1, -1):
                        if deliveries[j] >= d_avail:  # 그 위치에 온전히 배달
                            deliveries[j] -= d_avail
                            d_avail = 0
                            break
                        else:
                            d_avail -= deliveries[j]
                            deliveries[j] = 0
            if pickups[i] >= cap:
                pickups[i] -= cap
            else:
                p_avail -= pickups[i]
                pickups[i] = 0
                if p_avail > 0:  # 앞 집들에도 수거할 수 있음
                    for j in range(i - 1, -1, -1):
                        if pickups[j] >= p_avail:  # 그 위치에 온전히 수거
                            pickups[j] -= p_avail
                            p_avail = 0
                            break
                        else:
                            p_avail -= pickups[j]
                            pickups[j] = 0
    return answer * 2


''' 2트 => 답 참고
1. have_to_deliver 과 have_to_pickup 이 모두 0 이나 음수라면, i번째 배달/수거는 오가는 길에 처리 가능하다는 것.
    -> i번째를 따로 한번 더 안와도 된다.
2. have_to_deliever 나 have_to_pickup 둘 중 하나라도 양수라면, 배달/수거하러 i번째 방문 필요
    -> answer 에 더해준다.
'''
def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries.reverse()
    pickups.reverse()

    have_to_deliver, have_to_pickup = 0, 0

    for i in range(n):
        have_to_deliver += deliveries[i]
        have_to_pickup += pickups[i]

        while have_to_deliver > 0 or have_to_pickup > 0:
            have_to_deliver -= cap
            have_to_pickup -= cap
            answer += (n - i) * 2

    return answer