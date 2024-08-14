#시간제한2초, 메모리제한256MB
import copy

n = 5

graph = [input() for _ in range(n)]
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]
res = []
def dfs(i,j,s,step):
    print(i,j,s,step)
    if len(step) == 7:
        if s == 4:
            res.append(step)
            return True
        else:
            return False
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0<=ni<=4 and 0<=nj<=4 and (ni,nj) not in step:
            _step = copy.deepcopy(step)
            _step.add((ni, nj))
            if graph[ni][nj] == 'S':
                dfs(ni,nj,s+1,_step)
            else:
                dfs(ni,nj,s,_step)
    return

for x in range(4):
    for y in range(4):
        if graph[x][y] == 'S': cnt = 1
        else: cnt = 0
        arr = set()
        arr.add((x,y))
        dfs(x,y,cnt,arr)

print(res)
res1 = dict.fromkeys(res)
print(res1)