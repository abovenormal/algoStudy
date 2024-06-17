import copy
from collections import deque
from itertools import combinations
N,M,G,R=map(int,input().split())
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))

possible=[]
for i in range(N):
    for j in range(M):
        if data[i][j]==2:
            possible.append((i,j)) # 배양 가능한 땅에 좌표 저장


print(possible)

green_red_list=list(combinations(possible,G+R))



dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(data_,total,green):
    gq=deque()
    rq=deque()
    for i,j in total: # 전처리
        if [i,j] not in rq:
            gq.append((i,j))
            data_[i][j]=3
        else:
            rq.append((i,j))
            data_[i][j]=4
    while gq:







for gr_list in green_red_list:
    for g_list in combinations(gr_list,G): # GR리스트에서 G만큼 뽑아내자
        copy_data=copy.deepcopy(data)
        bfs(copy_data,gr_list,g_list)
