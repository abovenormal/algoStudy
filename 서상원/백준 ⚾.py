from itertools import permutations

N = int(input())  # 이닝수
data = [list(map(int, input().split())) for _ in range(N)]

entry_list = list(permutations(range(1, 9), 8))  # idx 0 번이 1번 타자
max_score=0

for entry_per in entry_list:
    entry = list(entry_per[:3]) + [0] + list(entry_per[3:]) # 순열들이 tuple이라 list로 변환
    score=0 # 점수
    idx = 0  # idx는 0~8번까지 계쏙해서 이닝이 끝날때가지 순회
    for inning in range(N): # 이닝수
        out=0
        base=[0,0,0,0]

        while out<3:
            idx=idx%9

            if data[inning][entry[idx]] ==0: # out
                out+=1
            elif data[inning][entry[idx]] ==1: # 안타
                score += base[3]
                base=[0,1,base[1],base[2]]
            elif data[inning][entry[idx]] == 2: # 2루타
                score += (base[2] + base[3])
                base=[0,0,1,base[1]]
            elif data[inning][entry[idx]] == 3: # 3루타
                score+=(base[1]+base[2]+base[3])
                base=[0,0,0,1]
            elif data[inning][entry[idx]] == 4: # 홈런
                score += (1 + base[1] + base[2] + base[3])
                base = [0, 0, 0, 0]

            idx+=1 # 다음 타자

    #1개의 entry 종료시
    max_score=max(score,max_score)

print(max_score)
