# 시간제한1초, 메모리제한256MB

n = int(input())

arr = list(map(int,input().split()))
parents = dict()
def find_parents(n1,n2):
    parent, cnt = parents[n1]
    if n2 > parent:
        parents[n2] = [parent, cnt]
        return 1
    if n1 == parent and n2 < parent:
        parents[n2] = [n2, 1]
        return 2
    elif n2 < parent:
        return find_parents(parent, n2)

def solution(s, e):
    minval = arr[s]
    cnt = 1
    parents[arr[s]] = [arr[s], cnt]
    for i in range(s, e):
        if arr[i] == minval: continue
        if arr[i] > minval:
            cnt = parents[minval][1] + 1
            parents[arr[i]] = [minval,cnt]
            minval = arr[i]
        elif arr[i] < minval:
            yn = find_parents(minval, arr[i])
            if yn == 1:
                minval = arr[i]
            if yn == 2:
                solution(i, e)
    res.append(cnt)

res = []


solution(0, n)
print(max(res))

