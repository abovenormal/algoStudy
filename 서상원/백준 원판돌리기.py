from collections import deque
N,M,T=map(int,input().split())
data=[0] # idx가 1부터 시작이기에 편의상 0 넣자
for  _ in range(N):
    data.append(list(map(int,input().split())))

test=[]
for _ in range(T):
    test.append(list(map(int,input().split())))

def rotate(x,d,k):

    global data
    if d==1:
        k*=-1

    for i in range(1,N//x+1):
        q=deque(data[i*x])
        q.rotate(k)
        data[i*x]=list(q)

def calculate():
    global data

    # 같은 원판 내에서 확인
    remove = set()
    for i in range(1,N+1):
        for j in range(M):
            if data[i][j]!=0 and data[i][(j+1)%M]!=0 and data[i][j]==data[i][(j+1)%M]:
                remove.add((i,j))
                remove.add((i,(j+1)%M))

    #다른 원판들 끼리 확인 (1번원판 부터 M-1 원판 까지)
    for i in range(1,N):
        for j in range(M):
            if data[i][j]!=0 and data[i+1][j]!=0 and data[i][j]==data[i+1][j]:
                remove.add((i,j))
                remove.add((i+1,j))

    if remove: # 지울 숫자가 있으면
        for i,j in remove:
            data[i][j]=0

    else: # 지울 숫자가 없으면
        sum_=0
        count=0
        for i in range(1,N+1):
            for j in range(M):
                if data[i][j]!=0:
                    count+=1
                    sum_+=data[i][j]

        if count==0:
            return
        
        avg=sum_/count

        for i in range(1,N+1):
            for j in range(M):
                if data[i][j]!=0:
                    if data[i][j] > avg:
                        data[i][j]-=1
                    elif data[i][j] < avg:
                        data[i][j]+=1

for x,d,k in test:
    rotate(x,d,k)
    calculate()

result=0
for i in range(1,N+1):
    for j in range(M):
        if data[i][j]!=0:
            result+=data[i][j]

print(result)
