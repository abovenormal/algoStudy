def get_max_length(arr):
    if not arr:
        return 0
    
    n = len(arr)
    arr.sort()
    longest = 1

    dp = [{} for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = arr[i] - arr[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            longest = max(longest, dp[i][diff])

    return longest

n = int(input())
arr = [int(input()) for _ in range(n)]

print(get_max_length(arr))
