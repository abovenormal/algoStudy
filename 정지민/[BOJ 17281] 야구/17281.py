''' 1트 => 시간초과
- 1,2,3 루 진출 구현을 바꿔보자
'''
# from itertools import permutations
# from collections import deque
#
# n = int(input())
# result = []
# for _ in range(n):
#     result.append([0] + list(map(int, input().split())))
#
# def change_player(idx):
#     if idx == 8: return 0
#     else: return idx + 1
#
# def get_score(players):
#     score = 0
#     player_idx = 0
#     for inning in range(n):
#         roo = deque([0,0,0])
#         out = 0
#         while out < 3:
#             # (1) 안타: 타자, 모든 주자 한 루씩 진루
#             if result[inning][players[player_idx]] == 1:
#                 roo.append(players[player_idx])
#             # (2) 2루타: 타자, 모든 주자 두 루씩 진루
#             elif result[inning][players[player_idx]] == 2:
#                 roo.append(players[player_idx])
#                 roo.append(0)
#             # (3) 3루타: 타자, 모든 주자 3루씩 진루
#             elif result[inning][players[player_idx]] == 3:
#                 roo.append(players[player_idx])
#                 roo.append(0)
#                 roo.append(0)
#             # (4) 홈런: 타자와 모든 주자가 홈까지 진루
#             elif result[inning][players[player_idx]] == 4:
#                 roo.append(players[player_idx])
#                 roo.append(0)
#                 roo.append(0)
#                 roo.append(0)
#             # (0) 아웃: 모든 주자가 진루하지 못하고, 공격 팀에 아웃 하나 증가
#             else:
#                 out += 1
#             while len(roo) > 3:
#                 if roo.popleft() > 0:
#                     score += 1
#             player_idx = change_player(player_idx)
#     return score
#
# answer = 0
# players_permu = list(permutations([i for i in range(1, 10)], 9))
# for players in players_permu:
#     if players[3] != 1: continue
#     # 해당 players 순서일 때, 얻을 수 있는 점수 구하기
#     answer = max(answer, get_score(players))
#
# print(answer)


''' 2트
[ 최적화 방법 ]
1. 위에서 deque() 로 처리해줬던 것을 변수로 처리
2. 4번 타자는 결정되어 있으므로, 8명 선수에 대한 순열만 구한다.
3. sys.stdin.readline() 으로 변경
4. 다음 타자 번호 모듈러 연산으로 구하기
5. result 배열 순회 시, result[inning][players[player_idx]] 보다 res[players[player_idx]] 로 해주는게 빠름 ?
'''
import sys
from itertools import permutations

n = int(input())
result = []
for _ in range(n):
    result.append([0] + list(map(int, sys.stdin.readline().split())))

def get_score(players):
    score = 0
    player_idx = 0
    for res in result:
        roo1, roo2, roo3 = 0, 0, 0
        out = 0
        while out < 3:
            # (1) 안타: 타자, 모든 주자 한 루씩 진루
            if res[players[player_idx]] == 1:
                score += roo3
                roo1, roo2, roo3 = 1, roo1, roo2
            # (2) 2루타: 타자, 모든 주자 두 루씩 진루
            elif res[players[player_idx]] == 2:
                score += (roo2 + roo3)
                roo1, roo2, roo3 = 0, 1, roo1
            # (3) 3루타: 타자, 모든 주자 3루씩 진루
            elif res[players[player_idx]] == 3:
                score += (roo1 + roo2 + roo3)
                roo1, roo2, roo3 = 0, 0, 1
            # (4) 홈런: 타자와 모든 주자가 홈까지 진루
            elif res[players[player_idx]] == 4:
                score += (roo1 + roo2 + roo3 + 1)
                roo1, roo2, roo3 = 0, 0, 0
            # (0) 아웃: 모든 주자가 진루하지 못하고, 공격 팀에 아웃 하나 증가
            else:
                out += 1
            player_idx = (player_idx + 1) % 9
    return score

answer = 0
players_permu = list(permutations([i for i in range(2, 10)], 8))
for players in players_permu:
    players = list(players[:3]) + [1] + list(players[3:])
    # 해당 players 순서일 때, 얻을 수 있는 점수 구하기
    answer = max(answer, get_score(players))

print(answer)