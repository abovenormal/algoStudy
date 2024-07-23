import sys
input=sys.stdin.readline
n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(int(input()))
data.sort()

start = data[0]
end = data[-1]*m
answer = 1e20
while start <= end:
    # 최소시간 ~ 최대시간
    mid = (start + end ) // 2
    total = 0 # 해당 시간동안 몇명을 통과 시킬 수 있는지 저장 
    for i in range(n):
        total += mid // data[i] # 각 심사대 별로 통과 시킬 수 있는 사람 수 
    if total < m:
        start = mid + 1
    elif total >= m:
        end = mid - 1
        answer = min(answer, mid)

print(answer)
