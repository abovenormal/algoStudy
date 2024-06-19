# 2<=n<=50, 시간 제한 1초(2000만)
# 완전 탐색 시, 1번 타자 제외 8명으로 할 수 있는 모든 경우의 수(순열) = 8! = 40320

import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
res = 0 #최대값 저장

for hitter in permutations(range(1, 9), 8):
    hitter = list(hitter[:3]) + [0] + list(hitter[3:]) # 4번 타자는 0번 고정
    score = 0
    hitorder = 0
    for i in range(n):
        out = 0
        onbase = [0, 0, 0]
        while out < 3:
            hit = innings[i][hitter[hitorder]]
            if  hit == 0: # 아웃
                out += 1
            elif hit == 1: # 1루타
                score += onbase[2]
                onbase = [1, onbase[0], onbase[1]]
            elif hit == 2: # 2루타
                score += onbase[1] + onbase[2]
                onbase = [0, 1, onbase[0]]
            elif hit == 3: # 3루타
                score += onbase[0] + onbase[1] + onbase[2]
                onbase = [0, 0, 1]
            elif hit == 4: # 홈런
                score += sum(onbase) + 1
                onbase = [0, 0, 0]
            hitorder += 1 # 다음 주자 변경
            if hitorder > 8: hitorder = 0
    if score > res: # 최대값 저장
        res = score

print(res)