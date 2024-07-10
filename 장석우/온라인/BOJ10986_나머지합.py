# 시간제한1초, 메모리제한256MB
# n ~ 10**6, m ~ 10**3

n, m = map(int, input().split())

arr = list(map(int, input().split()))

table = [0] * m
sum = 0
for i in range(n):
    sum += arr[i]
    table[sum % m] += 1

res = table[0]
for j in range(m):
    res += table[j] * (table[j] - 1) // 2

print(res)