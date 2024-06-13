import sys
from itertools import permutations

N = int(sys.stdin.readline())
innings = []
for _ in range(N):
    innings.append(list(map(int, sys.stdin.readline().split())))
p_nums = [1, 2, 3, 4, 5, 6, 7, 8]

answer = 0
for order in permutations(p_nums):
    order = list(order)
    order.insert(3, 0)
    score = 0
    p = 0
    for inning in range(N):
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            if innings[inning][order[p]] == 0:
                out += 1
            elif innings[inning][order[p]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif innings[inning][order[p]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif innings[inning][order[p]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            else:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            p = (p + 1) % 9
    answer = max(answer, score)


print(answer)