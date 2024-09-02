#시간제한2초, 메모리제한128MB

import sys
from itertools import permutations

input = sys.stdin.readline

t = int(input())

def find(favor):
    couple = [0 for _ in range(11)]
    round = True
    while round:
        for woman in range(6, 11):
            if couple[woman]: continue
            for man in favor[woman]:
                if couple[man]:
                    postwoman = couple[man]
                    idx = favor[man].index(postwoman)
                    nidx = favor[man].index(woman)
                    if idx < nidx: continue
                    else:
                        couple[postwoman] = 0
                        couple[man] = woman
                        couple[woman] = man
                        break
                else:
                    couple[man] = woman
                    couple[woman] = man
                    break
        for woman in range(6, 11):
            if couple[woman]: round = False
            else:
                round = True
                break
    return couple

for _ in range(t):
    favor = [[],[]]
    favor[1] = [6,7,8,9,10]
    for i in range(2, 11):
        favor.append(list(map(int,input().split())))
    res = find(favor)[1]
    print(res)
    text = 'NO'
    for fav in permutations(favor[1]):
        favor[1] = fav
        tmp = find(favor)[1]
        print(tmp)
        if tmp != res:
            print(fav)
            print(find(favor))
            text ='YES'
            break
    print(text)



