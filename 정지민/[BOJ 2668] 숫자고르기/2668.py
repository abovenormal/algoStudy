''' 1트 => '이분탐색 + 조합 + set 자료구조' 로 시도. 4% 메모리 초과.
'''
# from itertools import combinations

# n = int(input())

# nums = [0] * (n+1)
# for i in range(1, n+1):
#     nums[i] = int(input())

# def is_possible(set_size):
#     global n
#     combis = list(combinations([i for i in range(1, n+1)], set_size))
#     for combi in combis:
#         up_set = set(combi)
#         down_set = set()
#         for i in range(len(combi)):
#             down_set.add(nums[combi[i]])
#         same = up_set & down_set
#         if len(same) == set_size:
#             return (True, list(same))
#     return (False, [])

# start, end = 0, n
# answer = 0
# ans_arr = []
# while start <= end:
#     mid = (start + end) // 2

#     res, arr = is_possible(mid)

#     if res == True:
#         start = mid + 1
#         if mid > answer:
#             answer = mid
#             ans_arr = arr
#     else:
#         end = mid - 1

# print(answer)
# ans_arr.sort()
# for a in ans_arr:
#     print(a)



''' 2트 => dfs. 답 참고.
- 주어진 표를 그래프로 생각하고, dfs 로 탐색하다가 사이클 발생한 노드들의 집합이 답이다!
'''
import sys

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i].append(int(sys.stdin.readline()))

def dfs(num):
    if not visited[num]:
        visited[num] = True
        for _next in graph[num]:
            up_set.add(num)
            down_set.add(_next)

            if up_set == down_set:
                answer.extend(list(down_set))
                return
            
            dfs(_next)
    visited[num] = False

answer = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    up_set = set()
    down_set = set()

    dfs(i)

answer = list(set(answer))
answer.sort()

print(len(answer))
for a in answer:
    print(a)