import sys

n,m = map(int, sys.stdin.readline().split())
booth = []
for _ in range(n):
    booth.append(int(sys.stdin.readline()))

start = min(booth)
end = max(booth) * m
answer = end

while start <= end:
    time = (start + end) // 2

    cnt = 0
    for _booth in booth:
        cnt += (time // _booth)

    if cnt >= m:
        answer = min(answer, time)
        end = time - 1
    else:
        start = time + 1

print(answer)