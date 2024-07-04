from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# start_x, start_y 에서 bfs 돌리면서 다른 사람 만나면 맨해튼거리 계산해서 체크하기
def bfs(start_x, start_y, _map):
    visited = [[False] * 5 for _ in range(5)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True

    while q:
        cx, cy, cnt = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not (0 <= nx < 5 and 0 <= ny < 5): continue
            if _map[nx][ny] == 'X': continue

            if not visited[nx][ny]:
                if _map[nx][ny] == 'P':
                    if abs(nx - start_x) + abs(ny - start_y) <= 2 and cnt <= 2:
                        return False
                else:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True

    return True


def solution(places):
    answer = [1] * 5

    for t in range(5):
        place = places[t]
        _map = []
        people_pos = []
        for i in range(5):
            _map.append(list(place[i]))
            for j in range(5):
                if place[i][j] == 'P':
                    people_pos.append((i, j))

        for px, py in people_pos:
            res = bfs(px, py, _map)
            if res == False:
                answer[t] = 0
                break
    return answer