import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(cur):
    global visited, path, answer

    visited[cur] = True
    path.append(cur)

    _next = choice[cur]
    if visited[_next]:               # 방문한 적 있는 노드를 다시 방문한 것이므로, 사이클 발생
        if _next in path:            
            answer -= len(path[path.index(_next):])
            return
    else:                            # 방문한 적 없
        dfs(_next)

for _ in range(t):
    n = int(input())
    choice = list(map(int,input().split()))
    for i in range(n):
        choice[i] -= 1
    
    path = []
    visited = [False] * n
    answer = n
    for start in range(n):
        if not visited[start]:
            path = []
            dfs(start)
            
    print(answer)   