from itertools import combinations

N=int(input())
result=[]

for i in range(1,11):
    for comb in combinations(range(0,10),i):
        li=list(comb)
        #print(li[0],type(li[0]))
        li.sort(reverse=True)
        result.append(int(''.join(map(str,li))))

result.sort()


try:
    print(result[N-1])
except:
    print(-1)












