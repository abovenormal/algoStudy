import heapq

N=int(input())
data=[]
for _ in range(N):
    a,b,c,=map(int,input().split())
    data.append((b,c)) # 노드 번호는 안중요하니 빼고 넣기

data.sort(key=lambda x:[x[0]]) # 시작 시간으로 정렬

q=[]
heapq.heappush(q,data[0][1]) # 제일 먼저 시작하는 강의의 끝나는 시간을 저장

for i in range(1,N):
    if data[i][0] < q[0] : # 다음 강의의 시작 시간이 q 첫번째의 끝나는 시간 보다 빠르게 시작한다면 강의실 필요
        heapq.heappush(q,data[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,data[i][1])

print(len(q))






