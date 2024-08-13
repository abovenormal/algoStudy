# 시간제한1초, 메모리제한128MB

n, m = map(int,input().split())

students = list(map(int,input().split()))

dirty = 0
total = 0
arr = []
maxval = 0
maxidx = 0
res = []

for idx, i in enumerate(students):
    total = dirty * i
    arr.append(total)
    dirty += i
    if total > maxval:
        maxval = total
        maxidx = idx

res.append(maxidx)


