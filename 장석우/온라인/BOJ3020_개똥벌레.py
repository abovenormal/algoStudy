# 시간제한 1초, 메모리제한 128MB
# 2<=n<=200,000, 2<=h<=500,000
import sys

input = sys.stdin.readline
n, h = map(int,input().split())

down = []
up = []

for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()
mincnt = n
cnt = 0
def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    return start

for i in range(1, h+1):
    downcnt = len(down) - bs(down, i-0.5, 0, len(down)-1)
    upcnt = len(up) - bs(up, h-i+0.5, 0, len(up)-1)

    if mincnt == downcnt+upcnt:
        cnt +=1
    elif mincnt > downcnt+upcnt:
        cnt = 1
        mincnt = downcnt+upcnt

print(mincnt,cnt)