'''
1. 처음에는 이분탐색으로 접근 -> mid 값 조정 기준 애매
2. 총 사람 수에서 (우체국 기준 왼쪽 사람 수 >= 오른쪽 사람 수) 인 지점에 놓는 것이 최적값
    << 이 아이디어를 떠올리는게 핵심..!
3. 해당 지점을 찾기 위해 누적합을 이용하면 쉽다
    - prefix_sum[i]: i 번째 마을까지 누적 사람 수
'''
n = int(input())
arr = []
for _ in range(n):
    x, a = map(int, input().split())
    arr.append([x, a])

arr.sort()

prefix_sum = [0] * n
prefix_sum[0] = arr[0][1]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i][1]

for i in range(n):
    if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i]:
        print(arr[i][0])
        exit()