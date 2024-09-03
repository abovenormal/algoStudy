'''
[ 참고: https://nahwasa.com/entry/%EB%B0%B1%EC%A4%80-22866-%EC%9E%90%EB%B0%94-%ED%83%91-%EB%B3%B4%EA%B8%B0-BOJ-22866-JAVA?category=1049955?category=1049955 ]
1. 현재 빌딩 기준 왼쪽에 보이는 빌딩들을 스택에 저장해 가며 처리 후, 오른쪽에 보이는 빌딩들에 대해서 동일하게 처리
'''
n = int(input())
buildings = list(map(int, input().split()))

view_cnt = [0] * n
nearby = [-1] * n

# 왼쪽 처리 - 스택에는 (빌딩높이, 빌딩번호) 저장
stack = [(buildings[0], 0)]
for i in range(1, len(buildings)):
    # 스택의 마지막 <= 현재빌딩 이라면, 현재빌딩보다 높은 애가 나올때까지 빼고 현재빌딩만 스택에 추가
    if stack[-1][0] <= buildings[i]:
        while stack and stack[-1][0] <= buildings[i]:
            stack.pop()
        view_cnt[i] += len(stack)
        if len(stack) > 0:
            if nearby[i] == -1:
                nearby[i] = stack[-1][1]
            else:
                if abs(i-nearby[i]) > abs(i-stack[-1][1]):
                    nearby[i] = stack[-1][1]
        stack.append((buildings[i], i))
    # 스택의 마지막 > 현재빌딩 이라면, 현재빌딩 뒤에 나오는 건물들은 현재빌딩 & 스택에 들어있는 빌딩들 보기 가능
    else:
        view_cnt[i] += len(stack)
        if len(stack) > 0:
            if nearby[i] == -1:
                nearby[i] = stack[-1][1]
            else:
                if abs(i-nearby[i]) > abs(i-stack[-1][1]):
                    nearby[i] = stack[-1][1]
        stack.append((buildings[i], i))

# 오른쪽 처리
stack = [(buildings[n-1], n-1)]
for i in range(n-2, -1, -1):
    # 스택의 마지막 <= 현재빌딩 이라면, 현재빌딩보다 높은 애가 나올때까지 빼고 현재빌딩만 스택에 추가
    if stack[-1][0] <= buildings[i]:
        while stack and stack[-1][0] <= buildings[i]:
            stack.pop()
        view_cnt[i] += len(stack)
        if len(stack) > 0:
            if nearby[i] == -1:
                nearby[i] = stack[-1][1]
            else:
                if abs(i-nearby[i]) > abs(i-stack[-1][1]):
                    nearby[i] = stack[-1][1]
        stack.append((buildings[i], i))
    # 스택의 마지막 > 현재빌딩 이라면, 현재빌딩 뒤에 나오는 건물들은 현재빌딩 & 스택에 들어있는 빌딩들 보기 가능
    else:
        view_cnt[i] += len(stack)
        if len(stack) > 0:
            if nearby[i] == -1:
                nearby[i] = stack[-1][1]
            else:
                if abs(i-nearby[i]) > abs(i-stack[-1][1]):
                    nearby[i] = stack[-1][1]
        stack.append((buildings[i], i))

for i in range(n):
    if view_cnt[i] > 0:
        print(view_cnt[i], nearby[i]+1)
    else:
        print(0)