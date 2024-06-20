N=int(input())
data=[]
for _ in range(N):
    a,b=map(int,input().split())
    data.append((a,b))

data.sort() # 마을 순서로 정렬
prefix=[0 for _ in range(N)] # 누적합
prefix[0]=data[0][1] # 처음 값 저장
for i in range(1,N):
    prefix[i]=prefix[i-1]+data[i][1]


for i in range(N):
    left=prefix[i]
    right=prefix[N-1]-prefix[i]
    if left>=right:
        print(data[i][0])
        break
