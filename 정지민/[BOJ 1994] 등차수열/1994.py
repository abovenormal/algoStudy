''' 1트 => 22% 실패
'''
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# nums.sort()
#
# cnt = dict()
# for i in range(1,n):
#     for j in range(i-1, -1, -1):
#         cha = nums[i] - nums[j]
#         if cha in cnt:
#             cnt[cha] += 1
#         else:
#             cnt[cha] = 2
#
# answer = 0
# for key in cnt.keys():
#     answer = max(answer, cnt[key])
#
# print(answer)


''' 2트
1. answer 의 최솟값은 0 이 아닌 1 이다.
2. 등차의 값은 음수나 0도 될수 있다.
3. 2차원 dp 를 써야 하는 이유: 현재 방식에서 i 번째 숫자가 이전 숫자들 중 어디에서 이어져 왔는지 판단 불가.

[ 반례 ]
4
2
2
2
2
- 답: 4
- 결과: 7
'''
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# nums.sort()
#
# cnt = dict()
# for i in range(1,n):
#     for j in range(i-1, -1, -1):
#         cha = nums[i] - nums[j]
#         if cha in cnt:
#             cnt[cha] += 1
#         else:
#             cnt[cha] = 2
#         if cha != 0:
#             if -1 * cha in cnt:
#                 cnt[(-1)*cha] += 1
#             else:
#                 cnt[(-1)*cha] = 2
#
# answer = 1
# for key in cnt.keys():
#     answer = max(answer, cnt[key])
#
# print(answer)


''' 3트 => dp
- dp[i]: i 번째 수까지의 (key: 등차, val: 등차수열 개수) 를 저장하는 해시
- dp[i][diff]: i번째 수까지 diff 등차를 갖는 등차수열의 개수
'''
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

dp = [{} for _ in range(n)]
answer = 1

for i in range(n):
    for j in range(i):
        diff = nums[i] - nums[j]

        if diff in dp[j]:
            dp[i][diff] = dp[j][diff] + 1
        else:
            dp[i][diff] = 2

        answer = max(answer, dp[i][diff])

print(answer)
