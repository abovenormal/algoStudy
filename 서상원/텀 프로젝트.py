import sys
sys.setrecursionlimit(int(1e5+1))
def dfs(node):
    global result
    visited[node]=True # 방문처리
    next_node=graph[node]
    cycle.append(node)

    if visited[next_node]:# 방문이 된 노드라면
        if next_node in cycle : # 다음 노드가 사이클에 포함되어있다면은
            result+=cycle[cycle.index(next_node) : ] # 싸이클이 시작되는 시점부터 끝까지 result에 더한다
        return
    else:
        dfs(next_node)





T=int(input())
for _ in range(T):
    N=int(input())
    graph=[-1]+list(map(int,input().split()))
    visited = [False for _ in range(N + 1)] # 방문처리
    result=[]

    for i in range(1,N+1):
        if not visited[i]:
            cycle=[]
            dfs(i)

    print(N - len(result))



