''' 1트 => n*n 시간초과.
'''
# n = int(input())
# lectures = []
# for _ in range(n):
#     num, start, end = map(int, input().split())
#     lectures.append((start, end))
#
# lectures.sort()
#
# answer = 0
# room = [-1] * n
# for lec_start, lec_end in lectures:
#     found_flag = False
#     new_room_candi = -1
#     for i in range(n):
#         # 빈 강의실을 찾으면
#         if room[i] == -1 and new_room_candi == -1:
#             new_room_candi = i
#         if room[i] != -1 and room[i] <= lec_start:
#             room[i] = lec_end
#             found_flag = True
#     # 새로운 강의실을 생성해야 하는 경우라면
#     if found_flag == False:
#         room[new_room_candi] = lec_end
#         answer += 1
#
# print(answer)


''' 2트 => 힙 사용해서 최적화하기.
1. 최소힙에 강의 종료시간 저장
2. 힙의 최소 종료시간 <= 강의 시작시간이면, 힙에서 pop 후 추가
    아니면, 새로운 강의실이 필요한 경우므로 힙에 새로 추가
'''
import heapq

n = int(input())
lectures = []
for _ in range(n):
    num, start, end = map(int, input().split())
    lectures.append((start, end))

lectures.sort()

q = []
heapq.heappush(q, lectures[0][1])

for i in range(1,n):
    if q[0] <= lectures[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, lectures[i][1])

print(len(q))







