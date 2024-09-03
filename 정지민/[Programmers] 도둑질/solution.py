'''
1. 첫번째 집을 선택하는 경우 / 그렇지 않은 경우를 나눠서 계산
'''

def solution(money):
    answer = 0
    
    n = len(money)
    dp = [0] * n
    
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[2]
    
    if n == 3:
        return max(dp)
    
    # 첫번째 집을 선택하는 경우
    dp[2] += dp[0]
    for i in range(3, n):
        if i == n-1:
            dp[i] = dp[i-1]
        else:
            dp[i] = max(dp[i-3] + money[i], dp[i-2] + money[i], dp[i-1])
    answer = dp[n-1]

    # 첫번째 집을 선택하지 않는 경우
    dp = [0] * n
    dp[0] = 0
    dp[1] = money[1]
    dp[2] = money[2]
    for i in range(3, n):
        dp[i] = max(dp[i-3] + money[i], dp[i-2] + money[i], dp[i-1])
    answer = max(answer, dp[n-1])
   
    return answer