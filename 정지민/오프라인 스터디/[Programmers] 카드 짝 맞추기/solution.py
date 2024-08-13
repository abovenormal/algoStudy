''' 1트 => 정확성 66.7 / 100 점
[ 틀린 이유 - bfs 함수 ]
- 왜 틀림 ?..?

[ 풀이법 ]
1. 방문할 카드 번호 순서를 순열로 찾는다.
2. process 함수로 재귀 돌리기
    - 이번에 찾고자 하는 카드 번호 = target = order[o_idx]
    - pos 배열에 target 이 위치한 좌표 2개의 위치를 저장한다.
    - start ~ pos[0] ~ pos[1] 순서로 찾는 경우와, start ~ pos[1] ~ pos[0] 순서로 찾는 경우가 존재한다.
        - 두 경우에 대해 각각 bfs 돌려서 이동횟수 찾기
        - 찾은 이동횟수와, 다음 커서 위치를 기반으로 재귀 수행
3. bfs 함수
    - start ~ end 까지의 최소 이동 횟수를 찾아 반환한다.
'''
from itertools import permutations
from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 리턴: (start ~ end) 까지의 최소 이동 횟수
def bfs(start_x, start_y, end_x, end_y, n, _map):
    q = deque([(start_x, start_y, 0)])
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0

    while q:
        cx, cy, cnt = q.popleft()

        if cx == end_x and cy == end_y:
            return visited[cx][cy]

        # 누른 키 방향으로 한 칸 이동
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = cnt + 1

        # 누른 키 방향에 있는 가장 가까운 카드로 이동 || 그 방향의 가장 마지막 칸으로 이동
        for i in range(4):
            for exp in range(2, n):
                nx, ny = cx + exp * dx[i], cy + exp * dy[i]

                # 그 방향의 가장 마지막 칸
                if nx < 0:
                    nx = 0
                    if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = cnt + 1
                    break
                elif nx >= n:
                    nx = n - 1
                    if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = cnt + 1
                    break
                elif ny < 0:
                    ny = 0
                    if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = cnt + 1
                    break
                elif ny >= n:
                    ny = n - 1
                    if visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = cnt + 1
                    break

                # 가장 가까운 카드
                if _map[nx][ny] != 0 and (visited[nx][ny] == -1 or visited[nx][ny] > cnt + 1):
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt + 1
                    break

process_cnt = 1e9
# 리턴: order 순서로 order[o_idx] 부터 찾기 시작 && start_x, start_y 부터 방문 시작할때 최소 횟수
def process(_map, n, order, o_idx, start_x, start_y, cnt):
    global process_cnt

    if o_idx == len(order):
        process_cnt = min(process_cnt, cnt)
        return

    target = order[o_idx]
    pos = []
    for i in range(n):
        for j in range(n):
            if _map[i][j] == target:
                pos.append((i, j))

    # start ~ pos[0] ~ pos[1]
    case_1_cnt = bfs(start_x, start_y, pos[0][0], pos[0][1], n, _map) + bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1],
                                                                            n, _map)
    # start ~ pos[1] ~ pos[0]
    case_2_cnt = bfs(start_x, start_y, pos[1][0], pos[1][1], n, _map) + bfs(pos[1][0], pos[1][1], pos[0][0], pos[0][1],
                                                                            n, _map)

    # 카드 없애기
    for (x, y) in pos:
        _map[x][y] = 0

    process(_map, n, order, o_idx + 1, pos[1][0], pos[1][1], cnt + case_1_cnt + 2)
    process(_map, n, order, o_idx + 1, pos[0][0], pos[0][1], cnt + case_2_cnt + 2)

    # 카드 원상태
    for (x, y) in pos:
        _map[x][y] = target

def solution(board, r, c):
    global process_cnt
    answer = 1e9
    n = len(board[0])
    nums = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and board[i][j] not in nums:
                nums.append(board[i][j])

    orders = list(permutations(nums))
    for order in orders:  # order 순서로 방문
        _map = copy.deepcopy(board)
        process(_map, n, order, 0, r, c, 0)  # order 순서로 order[0] 부터 찾기 시작 && r,c 부터 방문 시작할때 최소 횟수
        answer = min(answer, process_cnt)
    return answer



''' 2트 => 답 참고.
1. bfs 함수만 수정
'''
from itertools import permutations
from collections import deque
import copy
from math import inf

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(start_x, start_y, end_x, end_y, n, _map):
    q = deque()
    q.append((start_x, start_y))
    visited = [[inf for _ in range(4)] for _ in range(4)]
    visited[start_x][start_y] = 0

    while q:
        cx, cy = q.popleft()

        if cx == end_x and cy == end_y:
            return visited[cx][cy]

        # 한 칸 이동
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] > visited[cx][cy] + 1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

        # 카드 있는 곳으로 한번에 이동 || 그러한 곳이 없다면 가장 마지막 칸 이동
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            while 0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4 and _map[nx][
                ny] == 0:  # 다음 칸이 0 이고, 다다음 칸이 범위 내에 있다면 이동한다.
                nx, ny = nx + dx[i], ny + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] > visited[cx][cy] + 1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

process_cnt = 1e9

# 리턴: order 순서로 order[o_idx] 부터 찾기 시작 && start_x, start_y 부터 방문 시작할때 최소 횟수
def process(_map, n, order, o_idx, start_x, start_y, cnt):
    global process_cnt

    if o_idx == len(order):
        process_cnt = min(process_cnt, cnt)
        return

    target = order[o_idx]
    pos = []
    for i in range(n):
        for j in range(n):
            if _map[i][j] == target:
                pos.append((i, j))

    # start ~ pos[0] ~ pos[1]
    case_1_cnt = bfs(start_x, start_y, pos[0][0], pos[0][1], n, _map) + bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1],
                                                                            n, _map)
    # start ~ pos[1] ~ pos[0]
    case_2_cnt = bfs(start_x, start_y, pos[1][0], pos[1][1], n, _map) + bfs(pos[1][0], pos[1][1], pos[0][0], pos[0][1],
                                                                            n, _map)

    # 카드 없애기
    for (x, y) in pos:
        _map[x][y] = 0

    process(_map, n, order, o_idx + 1, pos[1][0], pos[1][1], cnt + case_1_cnt + 2)
    process(_map, n, order, o_idx + 1, pos[0][0], pos[0][1], cnt + case_2_cnt + 2)

    # 카드 원상태
    for (x, y) in pos:
        _map[x][y] = target

def solution(board, r, c):
    global process_cnt
    answer = 1e9
    n = len(board[0])
    nums = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and board[i][j] not in nums:
                nums.append(board[i][j])

    orders = list(permutations(nums))
    for order in orders:  # order 순서로 방문
        _map = copy.deepcopy(board)
        process(_map, n, order, 0, r, c, 0)  # order 순서로 order[0] 부터 찾기 시작 && r,c 부터 방문 시작할때 최소 횟수
        answer = min(answer, process_cnt)
    return answer