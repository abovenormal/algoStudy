#다른 사람의 코드를 참고하였습니다...

S,N,K,R1,R2,C1,C2=map(int,input().split())

def is_black(y,x,size):
    if size==1:
        return False

    I= size// N # 한 변의 길이
    start,end=((N-K)//2) * I , ((N-K) //2 + K) * I
    if (start <= y < end and start<= x < end): # 검정색의 범위에 들어가면
        return True

    return is_black(y % I , x% I , I)


for  i in range(R1,R2+1):
    for j in range(C1,C2+1):
        if is_black(i,j,N**S):
            print(1,end='')
        else:
            print(0,end='')
    print()




