#틀린 코드입니다 ㅠ

from itertools import combinations
import copy
from collections import deque

def solutions(a, data_, monsters, d): # 궁수의 좌표와 데이터 , 몬스터수 , 사정거리
    cnt = 0  # 잡은 몬스터의 수
    tern = 0
    while cnt < monsters and tern < N: # 몬스터 다 잡거나 턴이 끝나면 종료
        killed = set()  # 한 턴에 죽이는 몬스터 위치 저장
        for archer in a:
            target = bfs(archer, d, data_)  # 가장 가까운 적을 찾는다
            if target:  # 적을 찾았으면
                killed.add(target)

        for x, y in killed:
            if data_[x][y] == 1:  # 이미 죽인 적이 아닌 경우만 카운트
                data_[x][y] = 0  # 죽인 몬스터 위치를 0으로 바꿈
                cnt += 1

        tern += 1  # 턴 증가
        move_monsters(data_)  # 몬스터 이동

    return cnt

def bfs(archer, d, data_):
    x, y = N, archer
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False for _ in range(M)] for _ in range(N + 1)]
    visited[x][y] = True
    q = deque([(x, y, 0)])

    potential_targets = []

    while q:
        x, y, cost = q.popleft()
        if cost > d:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if data_[nx][ny] == 1:  # 몬스터 도착
                    potential_targets.append((nx, ny, cost))
                q.append((nx, ny, cost + 1))

    if potential_targets:
        # 거리(cost)가 가장 작고, 열 번호(ny)가 가장 작은 순으로 정렬
        potential_targets.sort(key=lambda x: (x[2], x[1]))
        return (potential_targets[0][0], potential_targets[0][1])
    return None

def move_monsters(data):
    for i in range(N - 1, 0, -1):
        data[i] = data[i - 1]
    data[0] = [0] * M

N, M, D = map(int, input().split())  # 행, 열, 사정거리
data = [list(map(int, input().split())) for _ in range(N)]
monsters = sum(row.count(1) for row in data)

# 궁수의 좌표를 조합하기
comb_archers = list(combinations(range(M), 3))
max_value = 0
for archers in comb_archers:
    value = solutions(archers, copy.deepcopy(data), monsters, D)
    max_value = max(max_value, value)

print(max_value)
