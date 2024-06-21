from itertools import combinations

n,m=map(int,input().split())

data=[]
chicken_home=[]
home=[]

for i in range(n):
    data.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j]==2:
            chicken_home.append((i+1,j+1))
        elif data[i][j]==1:
            home.append((i+1,j+1))
        else:
            continue

chicken_home2=list(combinations(chicken_home,m))


min_result=[]

#li는 치킨집의 조합 중 리스트 하나
for li in chicken_home2:
    result=0
    #일반 집 하나의 좌표
    for hx,hy in home:
        value = 10e9
        #li에 있는 치킨집 좌표 하나
        for cx,cy in li:
            value=min(value , abs(hx-cx)+abs(hy-cy))
        #일반집에서 각 치킨집들 까지 거리중 최소 거리 저장
        result+=value
    min_result.append(result)

print(min(min_result))
