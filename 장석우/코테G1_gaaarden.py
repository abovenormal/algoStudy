# 시간 제한 2초 => 연산횟수 4000만 정도
# 메모리제한 512MB => 데이터 개수 100,000,000 정도
# 2<=n<=50, 2<=m<=50, 1<=g<=5, 1<=r<=5
# 배양액 뿌릴 수 있는 경우의 수 = 10C5 * 5C5 = 252, 조합으로 접근 가능

from itertools import combinations
from collections import deque

n, m, g, r = map(int, input().split())

garden = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flowercnt = []
tmp = []

for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            tmp.append((i, j))

coms_g = combinations(tmp, g)
print(tmp,list(coms_g),g)

for com_g in coms_g:
    coms_r = combinations([x for x in tmp if x not in list(com_g)] , r)
    print(com_g, coms_r)
    for com_r in coms_r:
        _garden = garden.copy()
        flower = []
        q = deque()
        q.append([list(com_g),list(com_r)])
        print(q)
        while q:
            print(_garden,q)
            xy_g, xy_r = q.popleft()
            floweryn_g = []
            floweryn_r = []
            qg = []
            qr = []
            for x_g, y_g in xy_g:
                _garden[x_g][y_g] = 3
                for i in range(4):
                    nx_g, ny_g = x_g+dx[i], y_g+dy[i]
                    if nx_g < 0 or nx_g > n-1 or ny_g < 0 or ny_g > m-1:
                        continue
                    if [nx_g, ny_g] in xy_g: continue
                    if _garden[nx_g][ny_g] == 1 or _garden[nx_g][ny_g] == 2:
                        if [nx_g, ny_g] not in floweryn_g:
                            floweryn_g.append([nx_g, ny_g])
                            qg.append([nx_g, ny_g])

            for x_r, y_r in xy_r:
                _garden[x_r][y_r] = 4
                for i in range(4):
                    nx_r, ny_r = x_r+dx[i], y_r+dy[i]
                    if nx_r < 0 or nx_r > n-1 or ny_r < 0 or ny_r > m-1:
                        continue
                    if [nx_r, ny_r] in xy_r: continue
                    if _garden[nx_r][ny_r] == 1 or _garden[nx_r][ny_r] == 2:
                        if [nx_r, ny_r] not in floweryn_r:
                            floweryn_r.append([nx_r, ny_r])
                            qr.append([nx_r, ny_r])

            floweryn = [x for x in floweryn_g if x in floweryn_r]
            if floweryn:
                for x_f, y_f in floweryn:
                    _garden[x_f][y_f] = 5
                    flower.append([x_f, y_f])
                qg = [x for x in qg if x not in floweryn]
                qr = [x for x in qr if x not in floweryn]
            q.append([qg, qr])
        flowercnt.append(len(flower))

print(max(flowercnt))
