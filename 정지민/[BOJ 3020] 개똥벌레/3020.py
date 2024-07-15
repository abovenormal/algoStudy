'''
1. total[i]: 높이 i 에서 부딪히는 모든 석순, 종유석 개수
    down[i]: 높이 i 에서 부딪히는 모든 석순 개수
    up[i]: 종유석이 바닥에서 자란다고 생각했을 때 높이 i 에서 부딪히는 모든 종유석 개수
    => up 배열을 뒤집고 down 의 각 원소들과 더해주면 total 배열 구하기 가능
2. 누적합 개념을 이용해서 down, up 배열을 채운다.
    - down[i-1] += down[i]
        : i 층에서 부딪혔다면, 그것보다 낮은 층인 i-1 층에서도 부딪히게 된다.
'''

n, h = map(int, input().split())
down = [0] * (h+1)
up = [0] * (h+1)
total = [0] * (h+1)

for i in range(n):
    height = int(input())
    if i % 2 == 0:
        down[height] += 1
    else:
        up[height] += 1

for i in range(h, 1, -1):
    down[i-1] += down[i]
    up[i-1] += up[i]

up.reverse()
up = [0] + up[:-1]

for i in range(h+1):
    total[i] = down[i] + up[i]

min_val = min(total[1:])
min_cnt = 0
for i in range(1, h+1):
    if total[i] == min_val:
        min_cnt += 1

print(min_val, min_cnt)
