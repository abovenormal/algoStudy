n=int(input())
def hanoi(n,start , to , other):
    if n==0: return
    hanoi(n-1 , start , other , to ) # A에서 B로 간다 C를 보조 기둥 삼아
    print(start , to)
    hanoi(n-1 , other , to ,start) # B에서 C로 간다 A를 보조 기둥 삼아


print(2**n-1)
hanoi(n,1,3,2)
