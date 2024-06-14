# 1 <= cap <= 50 , 1 <= n <= 100,000, 0<= deliveries & pickups 원소개수 <=50
# 완전탐색 불가, 그리디로 접근

def solution(cap, n, deliveries, pickups):
    answer = 0
    delivernow = 0
    pickupnow = 0

    for i in range(n-1, -1, -1):
        delivernow += deliveries[i]
        pickupnow += pickups[i]

        while delivernow > 0 or pickupnow > 0:
            delivernow -= cap
            pickupnow -= cap
            answer += (i+1) * 2

    return answer