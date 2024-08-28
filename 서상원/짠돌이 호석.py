#19개중 11개 맞았습니다..
import copy
p1=[]
p2=[]
n1,m1=map(int,input().split())
for _ in range(n1):
    p1.append(list(map(int,input())))
n2,m2=map(int,input().split())
for _ in range(n2):
    p2.append(list(map(int, input())))


data=[[0 for _ in range(100)] for _ in range(100)]

for i in range(n1):
    for j in range(m1):
        data[i][j]=p1[i][j]


def rotate(p): # puzzle
    n=len(p) # 행
    m=len(p[0]) # 열
    li=[[-1 for _ in range(n)] for _ in range(m)] # 행과 열을 체인지
    for i in range(m): # 바뀌어서 m이 행
        for j in range(n): # 바뀌어서 n이 열
            li[i][j]=p[j][m-1-i]
    return li


INF=int(1e9)
def try_(x,y,board,n,m): # board에 이미 p1은 장착되어있고 x,y부터 p2를 더한다
    for i in range(n):
        for j in range(m):
            board[x+i][y+j]+=p2[i][j]
            if board[x+i][y+j] >=2:
                return INF
    n=max(n1 ,x+n )
    m=max(m1, y+m)
    return n * m





result=INF
for k in range(4):
    p2=rotate(p2)
    n=len(p2)
    m=len(p2[0])
    # for i in range(n):
    #     for j in range(m):
    #         print(p2[i][j],end=' ')
    #     print()
    # print()

    for i in range(n1):
        for j in range(m1):
            result = min(try_(i,j,copy.deepcopy(data),n,m),result)

print(result)


