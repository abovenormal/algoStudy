from collections import deque


def bfs(V, edges):
    color = [0] * (V + 1)  

    for start in range(1, V + 1):
        if color[start] == 0:  # 미방문 노드에서 BFS 시작
            queue = deque([start])
            color[start] = 1  # 시작 노드 색칠

            while queue:
                node = queue.popleft()

                for next_node in edges[node]:
                    if color[next_node] == 0:  # 아직 방문하지 않은 노드
                        color[next_node] = -color[node]  # 반대 색으로 색칠
                        queue.append(next_node)
                    elif color[next_node] == color[node]:  # 인접 노드가 같은 색이라면 이분 그래프가 아님
                        return "NO"
    return "YES"


# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())  # 정점과 간선의 수
    edges = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)  # 양방향 그래프 처리

    result = bfs(V, edges)
    print(result)
