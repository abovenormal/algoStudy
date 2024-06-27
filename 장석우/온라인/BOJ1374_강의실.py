# 시간제한 2초, 메모리제한 128MB
# 1<=n<=100,000
# 완전탐색 불가, 그리디?

import sys, heapq

input = sys.stdin.readline

n = int(input())
lectures = []
s_min = float('inf')
e_max = 0
for _ in range(n):
    num, s, e = map(int, input().split())
    runtime = e - s
    lectures.append([s,e])

lectures.sort(key = lambda x : x[0])
rooms = []

for s, e in lectures:
    if rooms and rooms[0] <= s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, e)

print(len(rooms))
''' # 시간초과 코드
lectures.sort(key = lambda x : x[3], reverse = True) 

rooms = dict()
for i, lecture in enumerate(lectures):
    num, s, e, runtime = lecture
    if not rooms: # 강의실이 없다면, 강의실 추가
        rooms[i] = [(s, e)]
    else:
        for j, room in rooms.copy().items():
            rflag = False
            for r_s, r_e in room: # 강의 시간 체크
                if s >= r_e or e <= r_s:
                    rflag = True
                else:
                    rflag = False
                    break
            if rflag: # 들어갈 수 있다면 추가
                rooms[j].append((s, e))
        if not rflag: # 없다면 새로운 강의실 개설
            rooms[i] = [(s, e)]
'''

