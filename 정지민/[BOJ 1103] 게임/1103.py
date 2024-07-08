'''
[ bfs 에서 사이클 찾기 ]
- path 배열로 지나온 경로 추적
- (nx, ny) 가 path 배열에 들어있다면, 사이클 발생
'''

from collections import deque

n,m = map(int, input().split())
_map = []
for i in range(n):
    _map.append(list(input()))

for i in range(n):
    for j in range(m):
        if _map[i][j] != 'H':
            _map[i][j] = int(_map[i][j])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start_x, start_y):
    q = deque([(start_x, start_y, 1, [(start_x, start_y)])])
    visited = [[-1]*m for _ in range(n)]
    cx, cy, cnt, path = 0, 0, 1, [(start_x, start_y)]
    visited[start_x][start_y] = 1

    while q:
        cx, cy, cnt, path = q.popleft()

        next_pos = []
        end_flag = False
        for i in range(4):
            nx, ny = cx + dx[i] * _map[cx][cy], cy + dy[i] * _map[cx][cy]

            if 0<=nx<n and 0<=ny<m:
                # 사이클 발생 체크 -> 사이클 발생 시 -1 리턴
                if (nx, ny) in path:
                    return -1
                if visited[nx][ny] != cnt + 1 and _map[nx][ny] != 'H':
                    next_pos.append((nx, ny))
                    visited[nx][ny] = cnt + 1
                if _map[nx][ny] == 'H':
                    end_flag = True
            else:
                end_flag = True

        if len(q) == 0 and len(next_pos) == 0 and end_flag == True:
            break

        for nx, ny in next_pos:
            q.append((nx, ny, cnt + 1, path + [(nx, ny)]))

    return cnt

answer = bfs(0,0)
print(answer)