# 시간제한2초, 메모리제한128MB
# n ~ 1,000,000

n = int(input())
arr = []
res = set()

def solution():
    if len(arr) > 0 :
        res.add(int(''.join(map(str, arr))))

    for i in range(10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            solution()
            arr.pop()

try:
    solution()
    res = list(res)
    res.sort()
    print(res[n-1])
except:
    print(-1)