#시간제한1초, 메모리제한256MB
#G~10**5, p~10**5, g<=G

import sys


def find_alter(x):
    if x != alter[x]:
        alter[x] = find_alter(alter[x])
    return alter[x]

def union_find(a, b):
    x = find_alter(a)
    y = find_alter(b)
    if x<y: alter[y] = x
    else: alter[x] = y


input = sys.stdin.readline

g = int(input())
p = int(input())
alter = [i for i in range(g+1)]
flight = []
cnt = 0
for i in range(p):
    flight.append(int(input()))

for p in flight:
    x = find_alter(p)
    if x == 0:
        break
    union_find(x,x-1)
    cnt += 1

print(cnt)


