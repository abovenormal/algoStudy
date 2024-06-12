# 2<=n,m<=50, 1<=T<=50, 2<=x<=n, 0<=d<=1, 1<=k<m, 1<=원판숫자<=1000
# O(n*m*t) = 125000 정도로 시간복잡도 & 공간복잡도는 고려할 필요 x
# 시간제한 1초, 메모리제한 512MB

from collections import deque

n, m, t = map(int, input().split())
plates = [list(map(int, input().split())) for _ in range(n)]
steps = [list(map(int,input().split())) for _ in range(t)]

for step in steps: # 원판회전
    flag = True
    x, d, k = step
    for i_divx in range(1,n//x+1):
        i = i_divx * x # x의 배수
        if d == 0: # 시계방향회전
            plates[i-1] = plates[i-1][m-k:] + plates[i-1][:m-k] # index가 0부터 시작하므로 -1, k칸
        if d == 1: # 반시계방향회전
            plates[i-1] = plates[i-1][k:] + plates[i-1][:k]

    # bfs 수행하며 인접한 같은 수 찾기
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    q = deque()
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and plates[i][j] != 0:
                q.append([i, j])
                neighbours = []
                while q:
                    x, y = q.popleft()
                    visited[x][y] = 1
                    neighbours.append([x, y])
                    for s in range(4):
                        nx, ny = x + dx[s], y + dy[s]
                        if nx < 0 or nx > n - 1: continue  # 1번째 원판과 i번째 원판은 인접x
                        if ny == -1: ny = m - 1  # 1번째 수와 j번째 수는 인접
                        if ny == m: ny = 0
                        if visited[nx][ny] == 0 and plates[nx][ny] == plates[x][y]:
                            q.append([nx, ny])
                if len(neighbours) >= 2:  # bfs수행 후 인접한 같은수가 2개 이상이라면 소거
                    for x, y in neighbours:
                        plates[x][y] = 0
                        flag = False

    if flag:
        total = sum(list(map(sum, plates)))
        cnt = 0
        for i in range(n):
            cnt += plates[i].count(0)
        cnt = n * m - cnt
        if cnt == 0: continue
        else:
            avg = total / cnt
            for i in range(n):
                for j in range(m):
                    if plates[i][j] == 0: continue
                    if plates[i][j] > avg: plates[i][j] -= 1
                    elif plates[i][j] < avg: plates[i][j] += 1

res = sum(list(map(sum, plates)))
print(res)