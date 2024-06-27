import heapq
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
lectures = []

index = 1
for i in range(N):
    lecture_num = int(data[index])
    start = int(data[index + 1])
    end = int(data[index + 2])
    lectures.append((start, end))
    index += 3

lectures.sort()

min_heap = []

heapq.heappush(min_heap, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] >= min_heap[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, lectures[i][1])

print(len(min_heap))
