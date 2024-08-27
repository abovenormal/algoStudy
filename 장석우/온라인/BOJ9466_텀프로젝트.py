# 시간제한 3초, 메모리제한 256MB
# 2<=n<=100,000
import sys
sys.setrecursionlimit(111111)
def find(num):
    if num == selection[num]:
        avail[num] = 1
        return True
    else:
        if avail[selection[num]]: return False
        if selection[num] == q[0]:
            for i in q:
                avail[i] = 1
            return True
        q.append(selection[num])
        find(selection[num])


t = int(input())
for _ in range(t):
    n = int(input())
    selection = [0] + list(map(int,input().split()))
    avail = [0] + [0 for _ in range(n)]
    for i in range(1, n+1):
        if not avail[i]:
            q = [i]
            find(i)
    print(avail.count(0)-1)