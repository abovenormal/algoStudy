from collections import defaultdict

def solution(n, path, order):
    answer = True

    graph = [[] for _ in range(n)]
    for (x, y) in path:
        graph[x].append(y)
        graph[y].append(x)

    prev_visit = defaultdict(int)
    next_visit = defaultdict(int)

    # order 적용
    for (_before, _next) in order:
        prev_visit[_next] = _before

    # stack 을 이용한 dfs 탐색
    stack = [0]
    visited = [False] * n
    while stack:
        cur = stack.pop()

        if cur in prev_visit and not visited[prev_visit[cur]]:  # cur 이전에 방문할 노드를 아직 방문하지 않은 경우
            next_visit[prev_visit[cur]] = cur  # cur 이전 노드 방문 시, 이어서 cur 를 방문할 거다 라고 next_visit 리스트에 저장해두고 스킵
            continue

        visited[cur] = True
        for _next in graph[cur]:
            if not visited[_next]:  # 방문한 적 없는 노드일 경우, 방문처리
                stack.append(_next)

        if cur in next_visit:  # cur 다음에 이어서 방문할 노드가 있는 경우, 해당 노드로 이동
            stack.append(next_visit[cur])

    # 탐색이 끝나고, 노드들을 모두 방문했을 경우 True
    if sum(visited) == n:
        answer = True
    else:
        answer = False
    return answer