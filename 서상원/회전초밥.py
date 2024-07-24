N,d,k,c=map(int,input().split())
data=[]
for _ in range(N):
    data.append(int(input()))

sushi=[0 for _ in range(d+1)]

count=0
result=0

#초기 세팅
for i in range(k):
    if sushi[data[i]]==0:
        count+=1
    sushi[data[i]] += 1

    if sushi[c]==0:
        result=count+1
    else:
        result=count

for i in range(1,N):
    sushi[data[i-1]]-=1
    if sushi[data[i-1]]==0:
        count-=1

    if sushi[data[(i+k-1)%N]] ==0 :
        count+=1
    sushi[data[(i + k - 1) % N]] += 1

    if sushi[c]==0:
        result=max(result,count+1)
    else:
        result=max(result,count)

print(result)
