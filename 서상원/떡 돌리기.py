import heapq

N,M,X,Y=map(int,input().split())
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) # 양방향으로 간선 정보를 저장
    graph[b].append((a,c))

INF=int(1e9)
distance=[INF for _ in range(N)]

def dijkstra(node): #
    q=[] # cost , node
    heapq.heappush(q,(0,Y))
    distance[node]=0 # 출발점은 거리가 0
    while q:
        cost,node=heapq.heappop(q) # 거리 , 노드

        if distance[node] > cost: # 현재 노드 까지 도착한 거리가 현재 저장된 최단거리보다 크다면 continue
            continue

        for next_node , c in graph[node]: # 현재 노드 에서 갈 수 있는 경로들
            total_cost=cost+c
            if total_cost < distance[next_node]:
                distance[next_node]=total_cost # 거리 갱신
                heapq.heappush(q,(total_cost,next_node)) # 새로운 경로 추가

dijkstra(Y)

# (index, 거리)로 다시 계싼
for i in range(N):
    distance[i]=(i,distance[i])

# 람다로 정렬
distance.sort(key=lambda x : -x[1])

# 떡 돌리기 수행
days=0
if distance[0][1] > X: # 최대 cost가 X를 초과
    print(-1)
else:
    day=1
    cur=0
    for idx,cost in distance:

        if cur + 2*cost <= X:
            cur+= 2* cost
        else:
            day+=1
            cur = 2* cost

    print(day)
