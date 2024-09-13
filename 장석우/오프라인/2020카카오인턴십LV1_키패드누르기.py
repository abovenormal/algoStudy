# numbers 배열 크기 1~1,000
# numbers 배열 원소 값은 0~9

def solution(numbers, hand):
    left = [1,4,7,'*']
    right = [3,6,9,'#']
    mid = [2,5,8,0]
    lpos = '*'
    rpos = '#'
    answer = ''
    for num in numbers:
        if num in left:
            answer += 'L'
            lpos = num
        elif num in right:
            answer += 'R'
            rpos = num
        else:
            if lpos in mid:
                ldist = abs(mid.index(lpos) - mid.index(num))
            else:
                ldist = abs(left.index(lpos) - mid.index(num))+1
            if rpos in mid:
                rdist = abs(mid.index(rpos) - mid.index(num))
            else:
                rdist = abs(right.index(rpos) - mid.index(num))+1
            if ldist > rdist:
                answer += 'R'
                rpos = num
            elif ldist < rdist:
                answer += 'L'
                lpos = num
            else:
                if hand == 'right':
                    answer += 'R'
                    rpos = num
                elif hand == 'left':
                    answer += 'L'
                    lpos = num
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(numbers, hand))