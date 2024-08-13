''' 1트 => 92% 성공. 테케 14, 24 실패.
1. visited[x][y]: (x,y) 위치에 도달할 수 있는 최소 cost
2. 다익스트라처럼 visited[x][y] 가 이전값보다 적은 값으로 갱신되는 경우에만 방문한다.

[ 틀린 이유 ]
- 어느 방향에서 와서 (x,y) 로 도달했는지 정보를 저장해주지 않음.
    - 어느 방향으로부터 왔냐에 따라 직선도로 || 코너 가 결정나기 때문에, 이에 대한 값도 저장해줘야 한다.
    - https://school.programmers.co.kr/questions/30355
'''
# import heapq

# dx = [0, 1, -1, 0]
# dy = [1, 0, 0, -1]

# def dijkstra(start_x, start_y, board, n):
#     visited = [[1e9]*n for _ in range(n)]
#     q = []
#     heapq.heappush(q, (0, start_x, start_y, start_x, start_y))
#     visited[start_x][start_y] = 0

#     while q:
#         cost, x, y, bx, by = heapq.heappop(q)

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]

#             add_cost = 0
#             if nx == bx or ny == by:   # 직선 도로
#                 add_cost = 100
#             else:                      # 코너
#                 add_cost = 600

#             if not (0<=nx<n and 0<=ny<n): continue
#             if board[nx][ny] == 1: continue
#             if visited[nx][ny] < cost + add_cost: continue

#             visited[nx][ny] = cost + add_cost
#             heapq.heappush(q, (cost + add_cost, nx, ny, x, y))

#     return visited[n-1][n-1]

# def solution(board):
#     answer = dijkstra(0, 0, board, len(board))
#     return answer


''' 2트 => 96% 성공. 테케 25 실패.
1. 1트에서 우선순위큐 -> 그냥 큐 로만 바꿈.
2. 1트의 문제점 그대로 발생..!

[ 반례 ]
----------------------------
input
[[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]

wrong output
3300

answer
3000
----------------------------
'''
import heapq
from collections import deque

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def bfs(start_x, start_y, board, n):
    visited = [[1e9] * n for _ in range(n)]
    q = deque([])
    q.append((0, start_x, start_y, start_x, start_y))
    visited[start_x][start_y] = 0

    while q:
        cost, x, y, bx, by = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            add_cost = 0
            if nx == bx or ny == by:  # 직선 도로
                add_cost = 100
            else:  # 코너
                add_cost = 600

            if not (0 <= nx < n and 0 <= ny < n): continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny] < cost + add_cost: continue

            visited[nx][ny] = cost + add_cost
            q.append((cost + add_cost, nx, ny, x, y))

    return visited[n - 1][n - 1]


def solution(board):
    answer = bfs(0, 0, board, len(board))
    return answer
