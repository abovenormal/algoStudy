from collections import deque
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]


for idx in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()


S,E=map(int,input().split())

# S->E로 가는 경로 구하기 ,경로는 path에 저장
def bfs1():
    visited=[False for _ in range(N+1)]
    q=deque([(S,[])]) # node , path
    visited[S]=True
    while q:
        node,path=q.popleft()
        if node == E:
            return path

        for next_node in graph[node]:
            if not visited[next_node] : # 방문을 안한 노드라면
                visited[next_node]=True

                q.append((next_node,path+[next_node]))

path=bfs1()

def bfs2(path):
    visited=[False for _ in range(N+1)]
    q=deque([(E,path)])
    visited[E]=True
    while q:
        node,node_path=q.popleft()

        if node==S:
            return node_path

        for next_node in graph[node]:
            if not visited[next_node] and next_node not in node_path: # 방문안한 노드 + 이전 bfs에서 안가본 노드
                visited[next_node]=True

                q.append((next_node,node_path+[next_node]))

result=bfs2(path)

#print(result)
print(len(result))

