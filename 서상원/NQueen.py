n=int(input())
row=[0]* n
ans=0

#x는 현재 row
def checking(x):
    for i in range(x):
        if row[x]== row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

    
    


#백트랙킹 전체 함수
def solutions(x):
    global ans
    if x==n:
        ans+=1
    else:
        #각 열에 따라 퀸을 놓아보자
        for i in range(n):
            row[x]=i
            if checking(x):
                solutions(x+1)
                
                
solutions(0)
print(ans)
