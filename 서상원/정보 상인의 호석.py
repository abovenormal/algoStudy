import heapq

n=int(input())
hash_map={}
result=0
for _ in range(n):
    data=list(input().split())
    if data[0]=='1':
        if data[1] not in hash_map.keys():
            li=[]
            for i in data[3:]:
                i=int(i)
                li+=[(-i ,i)]

            heapq.heapify(li)
            hash_map[data[1]]=li

        else:
            li=hash_map[data[1]]
            for i in data[3:]:
                i=int(i)
                heapq.heappush(li,(-i,i))
                

            
            

    else:
        if data[1] in hash_map.keys():
            li=hash_map[data[1]]
            for _ in range(int(data[2])):
                if li:
                    value=heapq.heappop(li)
                    result+=value[1]
                else:
                    break



print(result)
