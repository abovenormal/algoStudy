from collections import deque

def solution(n,path,order):
    answer = True
    graph = [[] for _ in range(n)]
    nvisit = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    for i, j in path:
        graph[i].append(j)
        graph[j].append(i)
    for i, j in order:
        nvisit[j] = i
    return answer

def dfs(start):
    q = deque([start])


