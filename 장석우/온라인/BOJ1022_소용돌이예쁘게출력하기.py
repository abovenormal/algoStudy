# 시간제한 2초, 메모리제한 128MB

r1, c1, r2, c2 = map(int,input().split())

num = [[0 for _ in range(10001)] for _ in range(10001)]
minusflag = 1
dx = [0, -1]
dy = [1, 0]
dxm = [0, 1]
dym = [-1, 0]
x, y = 5000, 5000
num[x][y] = 1

for i in range(10002):
    print(i)
    for j in range(2):
        for k in range(i):
            if minusflag == 1:
                nx, ny = x + dx[j], y + dy[j]
                if 0<=nx<=10000 and 0<=ny<=10000:
                    num[nx][ny] = num[x][y] + 1
                    x, y = nx, ny
            if minusflag == -1:
                nx, ny = x + dxm[j], y + dym[j]
                if 0<=nx<=10000 and 0<=ny<=10000:
                    num[nx][ny] = num[x][y] + 1
                    x, y = nx, ny
    minusflag *= -1

print(num[0][0], num[10000][10000])