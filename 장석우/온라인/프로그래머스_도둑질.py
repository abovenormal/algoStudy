# 집의 개수는 3~1,000,000
# moeny 배열의 각 원소는 0~1,000

def solution(money):
    n = len(money)
    dp1 = [0 for i in range(n)]
    for i in range(n):
        m = money[i]
        dp1[i] = max(dp1[i - 2], dp1[i - 3]) + m
    dp2 = [0 for i in range(n)]
    for i in range(1, n):
        m = money[i]
        dp2[i] = max(dp2[i - 2], dp2[i - 3]) + m
    answer = max(dp1[-3], dp1[-2], dp2[-2], dp2[-1])
    return answer
