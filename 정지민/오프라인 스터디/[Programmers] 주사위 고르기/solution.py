'''
1. a 가 가져갈 수 있는 주사위 조합, b 가 가져갈 수 있는 주사위 조합을 구한다.
2. 해당 주사위 조합대로 가져갔을 때, a 와 b 가 주사위를 굴려 낼 수 있는 주사위 면의 합을 모두 구한다.
    - python 의 product 함수를 이용: 여러 개의 리스트들에서 원소를 뽑아 만들 수 있는 모든 순서쌍 조합 구하기 가능
3. b 가 낼 수 있는 점수 리스트 정렬 후, 이진탐색으로 a 의 점수가 a_score 일때 몇 번 이길 수 있는지 찾는다.
    - bisect_left 함수의 반환값 == a 가 이길 수 있는 횟수
==> '이진탐색' 을 떠올리는게 핵심
'''
from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    answer = []
    
    dice_combis = list(combinations([i for i in range(len(dice))], len(dice)//2))
    
    max_win_cnt = 0
    for a_dice_nums in dice_combis:
        a_dice_nums = list(a_dice_nums)
        b_dice_nums = []
        for num in range(len(dice)):
            if num not in a_dice_nums:
                b_dice_nums.append(num)
        
        # a 가 낼 수 있는 점수 리스트 구하기
        a_dices = [dice[dice_num] for dice_num in a_dice_nums]      # a 가 가지는 주사위들
        a_scores = [sum(combination) for combination in product(*a_dices)]
        
        # b 가 낼 수 있는 점수 리스트
        b_dices = [dice[dice_num] for dice_num in b_dice_nums]
        b_scores = [sum(combination) for combination in product(*b_dices)]
        
        # a 가 이기는 횟수 구하기
        a_win_cnt = 0
        b_scores.sort()
        for a_score in a_scores:
            a_win_cnt += bisect_left(b_scores, a_score)
        
        if max_win_cnt < a_win_cnt:
            max_win_cnt = a_win_cnt
            answer = [num+1 for num in a_dice_nums]
    return answer