# stones 배열 크기 1~200,000, 원소값은 1~200,000,000, k는 1이상 자연수
# 건널 수 있는지 검사 => 배열크기(200,000) => 100번이상 검사하면 시간초과, 완전탐색 불가
# 이진탐색으로 접근 원소값 1~200,000,000 사이의 값을 찾아내기

def solution(stones, k):
    answer = 0
    start = min(stones)
    end = max(stones)
    while start <= end:
        sflag = True
        mid = (start+end) // 2
        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
                if cnt > k:
                    end = mid - 1
                    sflag = False
                    break
            if stone > mid:
                cnt = 0
        if sflag:
            answer = mid
            start = mid + 1

    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))