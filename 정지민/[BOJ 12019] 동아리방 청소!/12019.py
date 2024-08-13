''' 답 참고. 하지만 이해 잘 못함..
- 참고 블로그: https://kimcodingvv.github.io/BOJ-12019/

1. dp[날짜][남은 청소 횟수][이전 청소 날짜] = 불쾌함 총합 최솟값
    : (날짜, 남은 청소 횟수, 이전 청소 날짜) 에 따라 경우가 나뉘므로 이를 바탕으로 dp 테이블 설정
2. 원하는 답은 dp[1][m][0] 에 들어있다.
    - N 일 까지의 각 사람들이 느낀 불쾌함의 총합의 최솟값
3. dp[now][cnt][pre] = min(dp[now+1][cnt-1][now], dp[now+1][cnt][pre] + sum * arr[now])
    - dp[now+1][cnt-1][now]: now 일에 청소를 하는 경우
    - dp[now+1][cnt][pre] + sum * arr[now]: now 일에 청소를 하지 않는 경우
4. 청소한 날짜 구하기
    - dp 배열 역추적
    - dp[now][cnt][pre] 를 저장하기 위해 (dp[now+1][cnt][pre], dp[now+1][cnt-1][now]) 를 비교하여 둘 중 최솟값을 저장함
    - 둘을 비교하여 더 작은 쪽을 따라간다.
        - dp[now+1][cnt][pre] 가 더 작으면 -> 청소를 안한 것
        - dp[now+1][cnt-1][now] 가 더 작으면 -> 청소를 한 것
'''
import sys
sys.setrecursionlimit(1000000)

def DP(now, cnt, pre, sum_):
    if dp[now][cnt][pre] != -1:
        return dp[now][cnt][pre]
    if now == n:
        return sum_ * arr[now]

    ret = float('inf')
    if cnt > 0:
        ret = min(ret, DP(now + 1, cnt - 1, now, 0))
    ret = min(ret, DP(now + 1, cnt, pre, sum_ + arr[now]))

    dp[now][cnt][pre] = ret + arr[now] * sum_
    return dp[now][cnt][pre]

def trace():
    cnt = m
    pre = 0
    for i in range(1, n):
        if cnt == 0:
            break
        a = dp[i + 1][cnt][pre]
        b = dp[i + 1][cnt - 1][i]
        if a >= b:
            pre = i
            cnt -= 1
            print(i, end=' ')

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [[[-1] * 101 for _ in range(11)] for _ in range(101)]

print(DP(1, m, 0, 0))
trace()
