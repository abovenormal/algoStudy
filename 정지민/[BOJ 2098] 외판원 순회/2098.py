'''
1. dp[i][route]: route 에 해당하는 도시들을 방문하고, 현재 i 번 도시에 있게 될 때까지 든 비용의 최솟값
2. 비트마스킹을 이용해 route 를 관리한다.
'''

n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))

dp = [[0 for _ in range(1 << n - 1)] for _ in range(n)]

def dfs(cur, route):
    global n, w, dp

    if dp[cur][route] != 0:         # 이미 방문한 경로인 경우
        return dp[cur][route]

    # 모든 도시를 다 방문한 뒤, 마지막 도시에 위치해 있는 경우
    if route == (1 << (n-1)) - 1:
        # 마지막 위치 -> 시작 위치로의 경로가 없는 경우
        if w[cur][0] == 0:
            return 1e9
        else:
            return w[cur][0]

    # 다음 도시 방문하기
    min_cost = 1e9
    for _next in range(1, n):
        # cur -> _next 로의 경로가 없는 경우
        if w[cur][_next] == 0: continue
        # _next 도시를 이미 방문했을 경우
        if route & (1 << _next - 1): continue

        cost = w[cur][_next] + dfs(_next, route | (1 << (_next-1)))
        if min_cost > cost:
            min_cost = cost

    dp[cur][route] = min_cost
    return min_cost

answer = dfs(0, 0)
print(answer)
