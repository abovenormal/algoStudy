# 시간제한1초, 메모리제한256MB
# 1<=n<=20

n = int(input())

def hanoi(n, s, e):
    if n == 1:
        print(s, e)
        return

    hanoi(n-1, s, 6-s-e)
    print(s, e)
    hanoi(n-1, 6-s-e, e)

print(2**n-1)
hanoi(n,1,3)