from collections import deque

def solution(maze):
    N = len(maze)
    M = len(maze[0])
    r_s_x, r_s_y = 0, 0
    b_s_x, b_s_y = 0, 0
    
    # 시작 위치 찾기
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                r_s_x, r_s_y = i, j
            elif maze[i][j] == 2:
                b_s_x, b_s_y = i, j

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(rx, ry, bx, by):
        visited_red = [[False for _ in range(M)] for _ in range(N)]
        visited_blue = [[False for _ in range(M)] for _ in range(N)]
        
        visited_red[rx][ry] = True  # 시작 위치 방문 처리
        visited_blue[bx][by] = True
        
        q = deque([(rx, ry, bx, by, 0)])  # (레드 x, 레드 y, 블루 x, 블루 y, 비용)
        
        while q:
            rx, ry, bx, by, cost = q.popleft()
            r_flag, b_flag = False, False
            
            # red, blue 도착 했는지 체크
            if maze[rx][ry] == 3 and maze[bx][by] == 4:  # 둘 다 도착
                return cost
            elif maze[rx][ry] == 3 and maze[bx][by] != 4:  # 레드 도착

                r_flag = True
            elif maze[rx][ry] != 3 and maze[bx][by] == 4:  # 블루 도착
                b_flag = True
            
            if r_flag and not b_flag:  # 블루 혼자 움직이기
                for i in range(4):
                    nbx = bx + dx[i]
                    nby = by + dy[i]
                    if 0 <= nbx < N and 0 <= nby < M and not visited_blue[nbx][nby] and (nbx != rx or nby != ry) and maze[nbx][nby] != 5:
                        visited_blue[nbx][nby]=True
                        q.append((rx,ry,nbx,nby,cost+1))
                       


            elif not r_flag and b_flag:  # 레드 혼자 움직이기
                for i in range(4):
                    nrx = rx + dx[i]
                    nry = ry + dy[i]
                    if 0 <= nrx < N and 0 <= nry < M and not visited_red[nrx][nry] and nrx != bx and nry != by and maze[nrx][nry] != 5:
                        visited_red[nrx][nry] = True
                        q.append((nrx, nry, bx, by, cost + 1))
                        
            else:  # 레드, 블루 같이 움직이기
                for i in range(4):
                    nrx = rx + dx[i]
                    nry = ry + dy[i]
                    if 0 <= nrx < N and 0 <= nry < M and not visited_red[nrx][nry] and maze[nrx][nry] != 5:
                        for j in range(4):
                            nbx = bx + dx[j]
                            nby = by + dy[j]
                            if 0 <= nbx < N and 0 <= nby < M and not visited_blue[nbx][nby] and maze[nbx][nby] != 5:
                                if not (nrx == bx and nry == by and nbx == rx and nby == ry):  # 자리 스왑 방지
                                    if not (nrx == nbx and nry == nby):  # 같은 칸 이동 방지
                                        q.append((nrx, nry, nbx, nby, cost + 1))
                                        visited_red[nrx][nry] = True
                                        visited_blue[nbx][nby] = True
        return 0

    answer = bfs(r_s_x, r_s_y, b_s_x, b_s_y)
    return answer
