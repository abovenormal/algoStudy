import sys

def lis(sequence):
    num = len(sequence)
    dp = [1] * num

    for i in range(num):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

input = sys.stdin.read
data = list(map(int, input().strip().split()))

num = data[0]
seq = data[1:num+1]

answer = lis(seq)
print(answer)
