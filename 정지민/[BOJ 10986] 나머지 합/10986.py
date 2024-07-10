n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

remainder = [0] * m
for ps in prefix_sum:
    remainder[ps % m] += 1

answer = remainder[0]
for r in remainder:
    answer += (r * (r-1)) // 2

print(answer)