import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]

for i in range(2,N+1):
    a,b,c=input().split()
    b,c=int(b), int(c)
    amount=b

    if a=='W':
        amount = -b
    graph[c].append((i,amount))

def dfs(node,amount):
    for n_node , n_amount in graph[node]:
        temp=dfs(n_node,n_amount)


        if temp>0:
            amount+=temp

    return amount

print(dfs(1,0))

