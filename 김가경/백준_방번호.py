def find_max_room_number(N, prices, M):
    # dp[i] = i원을 사용해서 만들 수 있는 가장 큰 숫자
    dp = [""] * (M + 1)

    # 숫자를 가격이 저렴한 순서대로 정렬
    sorted_numbers = sorted([(prices[i], str(i)) for i in range(N)])

    # dp 배열 채우기
    for i in range(1, M + 1):
        for price, number in sorted_numbers:
            if price > i:
                break
            candidate = dp[i - price] + number
            # 방 번호가 0으로 시작하지 않도록 하기 위한 조건
            if candidate[0] == '0':
                continue
            if len(candidate) > len(dp[i]) or (len(candidate) == len(dp[i]) and candidate > dp[i]):
                dp[i] = candidate

    return dp[M] if dp[M] else '0'

N = int(input().strip()) 
prices = list(map(int, input().strip().split()))  # 각 숫자의 가격
M = int(input().strip())  # 사용할 수 있는 금액

print(find_max_room_number(N, prices, M))
