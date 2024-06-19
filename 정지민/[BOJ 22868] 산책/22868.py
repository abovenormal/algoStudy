from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
s,e = map(int, input().split())

for i in range(1, n+1):
    graph[i].sort()

answer = 0

def bfs(start, end):
    global answer
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()

        if cur == end:
            return

        for _next in graph[cur]:
            if not visited[_next]:
                q.append(_next)
                visited[_next] = True
                prev[_next] = cur

visited = [False] * (n+1)
prev = [-1] * (n+1)
bfs(s, e)
visited = [False] * (n+1)
end = e
while end != s:
    visited[end] = True
    end = prev[end]
    answer += 1

prev = [-1] * (n+1)
bfs(e, s)
end = s
while end != e:
    end = prev[end]
    answer += 1

print(answer)