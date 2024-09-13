def solution(edges):
    graph = [[] for _ in range(1000001)]
    answer = []
    sset = set()
    for a, b in edges:
        graph[a].append(b)
    for i in range(len(graph)):
        if len(graph[i]) > 1:
            answer.append(i)
            set.add(i)

    return answer


def iscycle(num):
    group = []
    dfs(num)


def dfs(i):
    if group and i == num:
        return True
    group.append(i)
    for j in graph[i]:
        dfs(j)