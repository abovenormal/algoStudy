n = int(input())

def dfs(cur):
    des_nums.append(int(cur))
    for j in range(0, int(cur[-1])):       # 현재 자리의 마지막 수보다 작은 수들을 이어붙인다.
        dfs(cur + str(j))

des_nums = []
for start_num in range(10):     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ...
    dfs(str(start_num))

if n > len(des_nums):
    print(-1)
else:
    print(sorted(des_nums)[n-1])