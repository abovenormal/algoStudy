''' 1트 => 시간초과.
- 힙에서 뺐다가, 살아남은 나무들을 다시 힙에 넣는 과정에서 시간 초과인듯
    -> 최소 힙을 정렬된 순서로 순회하려면 이렇게 해야 할 수밖에 없으므로 힙 대신 큐를 써보자
'''
# import heapq
# import sys

# n,m,k = map(int, input().split())

# A = []
# for _ in range(n):
#     A.append(list(map(int, sys.stdin.readline().split())))

# tree = dict()       # (x,y) 에 심어진 나무들의 최소힙 - 나이 기준
# for i in range(n):
#     for j in range(n):
#         q = []
#         heapq.heapify(q)
#         tree[(i,j)] = q

# for _ in range(m):
#     x,y,z = map(int, sys.stdin.readline().split())
#     x -= 1
#     y -= 1
#     heapq.heappush(tree[(x,y)], z)

# _map = [[5] * n for _ in range(n)]

# for _ in range(k):
#     # 봄: 자신의 나이만큼 양분을 먹고, 나이가 1증가
#     # (하나의 칸에 여러 나무가 있다면, 나이가 어린 나무부터 양분 먹기)
#     # (자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음)
#     for (i,j) in tree.keys():
#         # 큐가 빌때까지 양분 먹기
#         success = []                        # 해당 칸에서 양분 먹기 성공한 나무들
#         dead = []
#         while tree[(i,j)]:
#             age = heapq.heappop(tree[(i,j)])
#             if _map[i][j] >= age:       # 먹을 수 있다면, 먹기
#                 _map[i][j] -= age
#                 success.append(age+1)
#             else:   
#                 # 여름: 봄에 죽은 나무가 양분으로 변화
#                 # (각각의 죽은 나무 나이 // 2) 값이 나무가 있던 칸에 양분으로 추가됨
#                 dead.append(age)

#         for x in success:
#             heapq.heappush(tree[(i,j)], x)
#         for x in dead:
#             _map[i][j] += age // 2

#     # 가을: 나이가 5의 배수인 나무들 번식
#     # (인접한 8개 칸에 나이가 1인 나무 생성)
#     dx = [-1, -1, -1, 0, 0, 1, 1, 1]
#     dy = [-1, 0, 1, -1, 1, -1, 0, 1]
#     for (i,j) in tree.keys():
#         for age in tree[(i,j)]:
#             if age % 5 == 0:
#                 for x in range(8):
#                     ni = i + dx[x]
#                     nj = j + dy[x]
#                     if (0<=ni<n and 0<=nj<n):
#                         heapq.heappush(tree[(ni, nj)], 1)
                
#     # 겨울: 각 칸에 A[r][c] 만큼의 양분 추가
#     for i in range(n):
#         for j in range(n):
#             _map[i][j] += A[i][j]

# answer = 0
# for (i,j) in tree.keys():
#     answer += len(tree[(i,j)])

# print(answer)



''' 2트 => 42% 시간초과.
- 우선순위큐 -> 일반 큐로 변경 후 풀이.
'''
# from collections import deque
# import sys

# n,m,k = map(int, input().split())

# A = []
# for _ in range(n):
#     A.append(list(map(int, sys.stdin.readline().split())))

# tree = dict()       # (x,y) 에 심어진 나무들의 큐 - 나이 기준 정렬
# for i in range(n):
#     for j in range(n):
#         tree[(i,j)] = deque([])

# for _ in range(m):
#     x,y,z = map(int, sys.stdin.readline().split())
#     x -= 1
#     y -= 1
#     if not tree[(x,y)]:
#         tree[(x,y)].append(z)
#     else:
#         if z <= tree[(x,y)][0]:
#             tree[(x,y)].appendleft(z)
#         else:
#             tree[(x,y)].append(z)

# _map = [[5] * n for _ in range(n)]

# for _ in range(k):
#     # 봄: 자신의 나이만큼 양분을 먹고, 나이가 1증가
#     # (하나의 칸에 여러 나무가 있다면, 나이가 어린 나무부터 양분 먹기)
#     # (자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음)
#     for (i,j) in tree.keys():
#         dead = []
#         trees = len(tree[(i,j)])
#         for k in range(trees):
#             age = tree[(i,j)][k]
#             if _map[i][j] >= age:               # 먹을 수 있다면, 먹기
#                 _map[i][j] -= age
#                 tree[(i,j)][k] += 1
#             else:                               # 먹을 수 없다면, 그 뒤 나무들은 모두 죽음
#                 for _ in range(trees-k):
#                     dead.append(tree[(i,j)].pop())
#                 break
#         # 여름 : (각각의 죽은 나무 나이 // 2) 값이 나무가 있던 칸에 양분으로 추가됨
#         for age in dead:      
#             _map[i][j] += age // 2

#     # 가을: 나이가 5의 배수인 나무들 번식
#     # (인접한 8개 칸에 나이가 1인 나무 생성)
#     dx = [-1, -1, -1, 0, 0, 1, 1, 1]
#     dy = [-1, 0, 1, -1, 1, -1, 0, 1]
#     for (i,j) in tree.keys():
#         for age in tree[(i,j)]:
#             if age % 5 == 0:
#                 for x in range(8):
#                     ni = i + dx[x]
#                     nj = j + dy[x]
#                     if (0<=ni<n and 0<=nj<n):
#                         tree[(ni, nj)].appendleft(1)
                
#     # 겨울: 각 칸에 A[r][c] 만큼의 양분 추가
#     for i in range(n):
#         for j in range(n):
#             _map[i][j] += A[i][j]

# answer = 0
# for (i,j) in tree.keys():
#     answer += len(tree[(i,j)])

# print(answer)



''' 3트
- tree 를 dict() 로 관리하는 대신 2차원 배열로 해보자.
    -> 어차피 2차원 배열 형태로 dict() 를 관리할 거면 그냥 이차원 배열로 접근하는게 더 빠르다!
'''
from collections import deque
import sys

n,m,k = map(int, input().split())

A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

tree = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    tree[x][y].append(z)

_map = [[5] * n for _ in range(n)]

for _ in range(k):
    # 봄: 자신의 나이만큼 양분을 먹고, 나이가 1증가
    # (하나의 칸에 여러 나무가 있다면, 나이가 어린 나무부터 양분 먹기)
    # (자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음)
    for i in range(n):
        for j in range(n):
            dead = []
            trees = len(tree[i][j])
            for k in range(trees):
                age = tree[i][j][k]
                if _map[i][j] >= age:               # 먹을 수 있다면, 먹기
                    _map[i][j] -= age
                    tree[i][j][k] += 1
                else:                               # 먹을 수 없다면, 그 뒤 나무들은 모두 죽음
                    for _ in range(trees-k):
                        dead.append(tree[i][j].pop())
                    break
            # 여름 : (각각의 죽은 나무 나이 // 2) 값이 나무가 있던 칸에 양분으로 추가됨
            for age in dead:      
                _map[i][j] += age // 2

    # 가을: 나이가 5의 배수인 나무들 번식
    # (인접한 8개 칸에 나이가 1인 나무 생성)
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(n):
        for j in range(n):
            for age in tree[i][j]:
                if age % 5 == 0:
                    for x in range(8):
                        ni = i + dx[x]
                        nj = j + dy[x]
                        if (0<=ni<n and 0<=nj<n):
                            tree[ni][nj].appendleft(1)
        
            # 겨울: 각 칸에 A[r][c] 만큼의 양분 추가
            _map[i][j] += A[i][j]
                
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)