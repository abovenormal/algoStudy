# 1<=n,m<=4, 제한시간도 없고 n,m범위는 작으므로 시간복잡도나 공간복잡도 고려할 필요 없음
# 정확한 결과 출력에 집중

from collections import deque


def solution(maze):
    n = len(maze)
    m = len(maze[0])
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rs = (i, j)
                visited[i][j][0] = 1
            if maze[i][j] == 2:
                bs = (i, j)
                visited[i][j][1] = 1
            if maze[i][j] == 3:
                rg_x = i
                rg_y = j
            if maze[i][j] == 4:
                bg_x = i
                bg_y = j
    q_r = deque()
    q_b = deque()
    q_r.append(rs)
    q_b.append(bs)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q_r or q_b:
        print(visited)
        if visited[rg_x][rg_y][0] != 0:
            q_r.clear()
        if visited[bg_x][bg_y][1] != 0:
            q_b.clear()
        if visited[rg_x][rg_y][0] == 0 and visited[bg_x][bg_y][1] == 0:  # 같이움직일때
            r_x, r_y = q_r.popleft()
            b_x, b_y = q_b.popleft()
            for i_r in range(4):
                for i_b in range(4):
                    nr_x = r_x + dx[i_r]
                    nr_y = r_y + dy[i_r]
                    nb_x = b_x + dx[i_b]
                    nb_y = b_y + dy[i_b]
                    if 0 <= nr_x and nr_x <= n - 1 and 0 <= nr_y and nr_y <= m - 1:
                        if 0 <= nb_x and nb_x <= n - 1 and 0 <= nb_y and nb_y <= m - 1:
                            if maze[nr_x][nr_y] != 5 and maze[nb_x][nb_y] != 5:
                                # 벽이나 격자밖으로 나가지 않고
                                if (nr_x, nr_y) != (nb_x, nb_y):
                                    # 같은 칸으로 움직일 수 없고
                                    if not ((nr_x, nr_y) == (b_x, b_y) and (nb_x, nb_y) == (r_x, r_y)):
                                        # 자리를 바꾸며 움직일 수 없고
                                        if visited[nr_x][nr_y][0] == 0 and visited[nb_x][nb_y][1] == 0:
                                            # 방문했던 칸으로 움직일 수 없는 경우
                                            q_r.append((nr_x, nr_y))
                                            q_b.append((nb_x, nb_y))
                                            visited[nr_x][nr_y][0] = visited[r_x][r_y][0] + 1
                                            visited[nb_x][nb_y][1] = visited[b_x][b_y][1] + 1

        if visited[rg_x][rg_y][0] == 0 and visited[bg_x][bg_y][1] != 0:
            # 빨간수레만 움직일때, 자리바꿈, 같은칸이동 고려할 필요x
            r_x, r_y = q_r.popleft()
            for i in range(4):
                nr_x = r_x + dx[i]
                nr_y = r_y + dy[i]
                if 0 <= nr_x and nr_x <= n - 1 and 0 <= nr_y and nr_y <= m - 1:
                    if maze[nr_x][nr_y] != 5 and visited[nr_x][nr_y][0] == 0:
                        q_r.append((nr_x, nr_y))
                        visited[nr_x][nr_y][0] = visited[r_x][r_y][0] + 1

        if visited[rg_x][rg_y][0] != 0 and visited[bg_x][bg_y][1] == 0:
            # 파란수레만 움직일때
            b_x, b_y = q_b.popleft()
            for i in range(4):
                nb_x = b_x + dx[i]
                nb_y = b_y + dy[i]
                if 0 <= nb_x and nb_x <= n - 1 and 0 <= nb_y and nb_y <= m - 1:
                    if maze[nb_x][nb_y] != 5 and visited[nb_x][nb_y][0] == 0:
                        q_b.append((nb_x, nb_y))
                        visited[nb_x][nb_y][1] = visited[b_x][b_y][1] + 1

    if visited[rg_x][rg_y][0] != 0 and visited[bg_x][bg_y][1] != 0:
        answer = max(visited[rg_x][rg_y][0], visited[bg_x][bg_y][1])
    else:
        answer = 0
    return answer

maze = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]

print(solution(maze))