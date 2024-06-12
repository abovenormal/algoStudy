from collections import deque
import copy

n,m,t = map(int, input().split())
_map = []
for _ in range(n):
    _map.append(deque(list(map(int, input().split()))))

def spin(i, direct, k):
    k = k % m
    if direct == 0:   # 시계방향 회전
        for _ in range(k):
            _map[i].appendleft(_map[i].pop())
    else:   # 반시계방향 회전
        for _ in range(k):
            _map[i].append(_map[i].popleft())

def remove():
    flag = False
    temp = copy.deepcopy(_map)

    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0: continue
            # 양옆 인접 찾기
            if _map[i][((j-1)+m)%m] == _map[i][j]:
                temp[i][((j-1)+m)%m], temp[i][j] = 0, 0
                flag = True
            if _map[i][((j+1)+m)%m] == _map[i][j]:
                temp[i][((j+1)+m)%m], temp[i][j] = 0, 0
                flag = True
            # 위아래 인접 찾기
            if i != 0:
                if _map[i-1][j] == _map[i][j]:
                    temp[i-1][j], temp[i][j] = 0, 0
                    flag = True
            if i != n-1:
                if _map[i+1][j] == _map[i][j]:
                    temp[i+1][j], temp[i][j] = 0, 0
                    flag = True
    return flag, temp

def check_num_left():
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0: return True
    return False

def avg():
    _sum, cnt = 0, 0
    for i in range(n):
        for j in range(m):
            if _map[i][j] != 0:
                cnt += 1
                _sum += _map[i][j]
    return _sum / cnt

answer = 0
for _ in range(t):
    x, d, k = map(int, input().split())
    # 1. x 의 배수인 번호 원판을 d 방향으로 k 칸 회전
    for i in range(1, n+1):
        if i % x == 0:
            spin(i-1, d, k)

    # 2. 원판에 수가 남아 있으면, (인접하면서 수가 같은 것) 을 모두 찾고 -> 모두 지우기
    #    (인접하면서 수가 같은것) 이 없는 경우 -> 원판 수들의 평균 구하기 -> 평균보다 큰 수면 -1, 작은 수면 +1
    if check_num_left():
        flag, _map = remove()
        if flag == False:
            _avg = avg()
            for i in range(n):
                for j in range(m):
                    if _map[i][j] != 0:
                        if _map[i][j] > _avg: _map[i][j] -= 1
                        elif _map[i][j] < _avg: _map[i][j] += 1

for i in range(n):
    for j in range(m):
        answer += _map[i][j]
print(answer)