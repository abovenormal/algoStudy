N=int(input())
nums=[int(input().strip()) for _ in range(N)]

nums.sort() # 정렬
dp=[{} for _ in range(N)] # 각 nums별로 해시를 저장할 dp 테이블 생성
answer=1

for i in range(N): # 전체 순회 탐색
    for j in range(i): # i번까지
        diff=nums[i]-nums[j] # 차이 값
        if diff in dp[j]: # 차이값이 해시에 있으면
            dp[i][diff]=dp[j][diff]+1
        else: # 없으면 2로 초기화
            dp[i][diff]=2
        answer=max(answer,dp[i][diff])
    #print(i, dp)

#print(dp)
print(answer)




