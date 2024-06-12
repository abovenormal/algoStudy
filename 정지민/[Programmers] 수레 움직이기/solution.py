import sys
sys.setrecursionlimit(10 ** 9)

answer = 1e9
n, m = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

b_start, r_start = [0, 0], [0, 0]
b_end, r_end = [0, 0], [0, 0]

def turn_move(bx, by, rx, ry, turn, _map, visited_blue, visited_red):
    global answer

    # 백트랙 조건
    if turn >= answer:
        return

    # 완료 조건
    if bx == b_end[0] and by == b_end[1] and rx == r_end[0] and ry == r_end[1]:
        answer = min(answer, turn)
        return

    # 가능한 모든 (파란수레 다음위치, 빨간수레 다음위치) 에 대해 dfs
    for bi in range(4):
        for ri in range(4):
            nbx, nby = bx + dx[bi], by + dy[bi]
            nrx, nry = rx + dx[ri], ry + dy[ri]

            # 자신의 위치에 도착한 수레는 그 위치에 고정
            if bx == b_end[0] and by == b_end[1]:
                nbx, nby = bx, by
            if rx == r_end[0] and ry == r_end[1]:
                nrx, nry = rx, ry

            # 조건 검사
            # 벽이나 격자판 밖 불가
            if not (0 <= nbx < n and 0 <= nby < m): continue
            if not (0 <= nrx < n and 0 <= nry < m): continue
            if _map[nbx][nby] == 5 or _map[nrx][nry] == 5: continue
            # 방문했던 칸으로 이동 불가
            if bx != b_end[0] or by != b_end[1]:
                if visited_blue[nbx][nby]: continue
            if rx != r_end[0] or ry != r_end[1]:
                if visited_red[nrx][nry]: continue
            # 동시에 두 수레를 같은 칸에 놓기 불가
            if nbx == nrx and nby == nry: continue
            # 위치를 바꾸면서 이동 불가
            if nbx == rx and nby == ry and nrx == bx and nry == by: continue

            # 다음 위치로 이동
            visited_blue[nbx][nby], visited_red[nrx][nry] = True, True
            turn_move(nbx, nby, nrx, nry, turn + 1, _map, visited_blue, visited_red)
            visited_blue[nbx][nby], visited_red[nrx][nry] = False, False

def solution(maze):
    global n, m
    n, m = len(maze), len(maze[0])

    visited_blue = [[False] * m for _ in range(n)]
    visited_red = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                r_start[0], r_start[1] = i, j
                visited_red[i][j] = True
            elif maze[i][j] == 2:
                b_start[0], b_start[1] = i, j
                visited_blue[i][j] = True
            elif maze[i][j] == 3:
                r_end[0], r_end[1] = i, j
            elif maze[i][j] == 4:
                b_end[0], b_end[1] = i, j

    turn_move(b_start[0], b_start[1], r_start[0], r_start[1], 0, maze, visited_blue, visited_red)

    if answer == 1e9: return 0
    return answer