''' 1트 => 정확성 100% / 효율성 0%
'''
# def solution(stones, k):
#     answer = 0
#     n = len(stones)
#     stones.append(1e9)

#     while True:
#         # 한 명 출발
#         i = 0
#         find_next_stone = True
#         while i < n and find_next_stone == True:
#             if stones[i] > 0:
#                 stones[i] -= 1
#                 i += 1
#                 continue
#             elif stones[i] == 0:
#                 find_next_stone = False
#                 for j in range(i+1, n+1):
#                     if j - i > k-1:
#                         break
#                     if stones[j] > 0:
#                         i = j
#                         find_next_stone = True
#                         break

#         if find_next_stone == True:
#             answer += 1
#         else:
#             break
#     return answer


''' 2트 => 이분탐색 접근. 정확성 100% / 효율성 0%
[ 시간초과 원인 ]
- maybe check_possible 함수 내부에서 이중 for 문..?
    => 이중 for 문 없이 되는경우/안되는경우 를 판단할 수 있는 방법을 찾아보자..!
'''
# def check_possible(stones, n, people, k):
#     stones = [1e9] + stones + [1e9]
#     n += 2
#     for i in range(1, n-1):
#         stones[i] -= people

#     for i in range(n-1):
#         if stones[i] > 0 and stones[i+1] <= 0:
#             # 양수인 돌을 기준으로 0 이하 돌이 k 개 이상 연속되면 -> 불가능한 케이스!
#             cnt = 0
#             for j in range(i+1, n-1):
#                 if stones[j] > 0: break
#                 else: cnt += 1
#                 if cnt >= k:
#                     return False
#     return True

# def solution(stones, k):
#     answer = 0
#     n = len(stones)

#     start, end = 0, max(stones)

#     while start <= end:
#         mid = (start + end) // 2

#         if check_possible(stones, n, mid, k) == True:
#             start = mid + 1
#             answer = max(answer, mid+1)
#         else:
#             end = mid - 1

#     return answer


''' 3트 => 이분탐색 접근. 정확성 100% / 효율성 테케 8, 10, 12 실패.
'''
# def check_possible(stones, n, people, k):
#     cnt = 0
#     for i in range(n):
#         # 0 이하 돌을 만나면 cnt += 1
#         # 0 이하 돌이 k 개 이상 연속되면 -> 불가능한 케이스!
#         if stones[i] - people <= 0:
#             cnt += 1
#             if cnt >= k:
#                 return False
#         else:
#             cnt = 0
#     return True

# def solution(stones, k):
#     answer = 0
#     n = len(stones)

#     start, end = 0, max(stones)

#     while start <= end:
#         mid = (start + end) // 2

#         if check_possible(stones, n, mid, k) == True:
#             start = mid + 1
#             answer = max(answer, mid+1)
#         else:
#             end = mid - 1

#     return answer


''' 4트
'''
def check_possible(stones, n, people, k):
    cnt = 0
    for i in range(n):
        # 0 이하 돌을 만나면 cnt += 1
        # 0 이하 돌이 k 개 이상 연속되면 -> 불가능한 케이스!
        if stones[i] <= people:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True


def solution(stones, k):
    answer = 0
    n = len(stones)

    start, end = 0, max(stones)

    while start <= end:
        mid = (start + end) // 2

        if check_possible(stones, n, mid, k) == True:
            start = mid + 1
            answer = max(answer, mid + 1)
        else:
            end = mid - 1

    return answer























