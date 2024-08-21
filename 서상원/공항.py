G=int(input())
P=int(input())
parents=[i for i in range(G+1)]


def find(x):
    if x!=parents[x]:
        parents[x]=find(parents[x])
    return parents[x]

def union(u,v): # u가 더 하위 노드
    u=find(u)
    v=find(v)

    parents[v]=u


result=0
for _ in range(P):
    p=int(input())
    p=find(p)
    if p == 0 :
        break
    union(p-1,p)
    result+=1



print(result)
