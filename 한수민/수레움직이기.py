from collections import deque

def solution(maze):
    #answer = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dir = []
    for i in range(4):
        for j in range(4):
            dir.append((i, j))

    r = len(maze)
    c = len(maze[0])
    q = deque() # q의 내용 : 빨간색의 track, 파란색의 track

    red = []
    blue = []

    for i in range(r):
        for j in range(c):
            if maze[i][j] == 1:
                red.append((i, j))
            if maze[i][j] == 2:
                blue.append((i, j))
            if maze[i][j] == 3:
                red_goal = (i, j)
            if maze[i][j] == 4:
                blue_goal = (i, j)
    q.append([red, blue])

    while q:
        tracks = q.popleft()
        red_now = tracks[0][-1]
        blue_now = tracks[1][-1]
        if red_now == red_goal and blue_now == blue_goal:
            return max(len(tracks[0])-1, len(tracks[1])-1)
        # 파란색만 움직이는 경우
        if red_now == red_goal:
            for i in range(4):
                nx = blue_now[0] + dx[i]
                ny = blue_now[1] + dy[i]
                # 범위 체크
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                # 이미 지난곳인지
                if (nx, ny) in tracks[1]:
                    continue
                # 벽인지
                if maze[nx][ny] == 5:
                    continue
                # 지금 빨간색이 있는 곳인지
                if (nx, ny) == red_now:
                    continue
                q.append([tracks[0], tracks[1] + [(nx, ny)]])
                continue
        if blue_now == blue_goal:
            for i in range(4):
                nx = red_now[0] + dx[i]
                ny = red_now[1] + dy[i]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if (nx, ny) in tracks[0]:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if (nx, ny) == blue_now:
                    continue
                q.append([tracks[0] + [(nx, ny)], tracks[1]])
                continue

        for re, bl in dir:
            r_nx = red_now[0] + dx[re]
            r_ny = red_now[1] + dy[re]
            b_nx = blue_now[0] + dx[bl]
            b_ny = blue_now[1] + dy[bl]

            # 빨강, 파랑 범위 체크
            if r_nx < 0 or r_nx >= r or r_ny < 0 or r_ny >= c:
                continue
            if b_nx < 0 or b_nx >= r or b_ny < 0 or b_ny >= c:
                continue
            # 벽 체크
            if maze[r_nx][r_ny] == 5 or maze[b_nx][b_ny] == 5:
                continue
            # 둘이 같은 곳으로 가는지
            if r_nx == b_nx and r_ny == b_ny:
                continue
            # 각자 이미 지난곳인지 확인
            if (r_nx, r_ny) in tracks[0] or (b_nx, b_ny) in tracks[1]:
                continue
            # 서로 위치는 바꾸는 경우인지
            if (r_nx, r_ny) == blue_now and (b_nx, b_ny) == red_now:
                continue
            q.append([tracks[0] + [(r_nx, r_ny)], tracks[1] + [(b_nx, b_ny)]])

    return 0