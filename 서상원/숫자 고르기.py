N=int(input())
graph=[-1 for _ in range(N+1)]

result1=[] # 1번째 줄과 2번째 줄의 값이 같은 노드들
for i in range(1,N+1):
    next =int(input())
    graph[i]=next
    if i== next:
        result1.append(i)


visited=[False for _ in range(N+1)]

def dfs(start,node,course):
    if start==node:
        #print(course)
        return course

    next=graph[node]

    if visited[next]==False:
        visited[next]=True
        li = dfs(start,next,course+[next])
        visited[next] = False
        if len(li)>0:
            return li


    return []






result2=[]
for node in range(1,N+1):
    if node== graph[node]:
        continue
    li=dfs(node,graph[node],[graph[node]])
    li.sort()
    if li not in result2:
        result2.append(li)


result=[]
for r in result2:
    result+=r
result+=result1
result.sort()


print(len(result))
for r in result:
    print(r)




