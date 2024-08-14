from itertools import combinations
data=[]
for _ in range(5): # 입력
    data.append(list(input()))

positions=[]
for i in range(5): # S 좌표
    for j in range(5):
        positions.append((i,j))

answer=0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def is_validate(x,y):
    visited = [[False for _ in range(5)] for _ in range(5)]
    stack=[(x,y)]
    count=1
    visited[x][y]=True
    while stack:
        x,y=stack.pop()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<5 and 0<=ny<5 and (nx,ny) in selected and  not visited[nx][ny]:
                visited[nx][ny]=True
                stack.append((nx,ny))
                count+=1

    if count==7:
        return True
    else:
        return False




for selected in combinations(positions,7):
    s_count=0
    for x,y in selected:
        if data[x][y]=='S':
            s_count+=1

    if s_count<=3:
        continue

    if is_validate(selected[0][0],selected[0][1]):
        answer+=1




print(answer)
