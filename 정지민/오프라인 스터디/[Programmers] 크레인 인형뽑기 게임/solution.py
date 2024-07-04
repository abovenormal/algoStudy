def solution(board, moves):
    answer = 0
    n = len(board)

    last_pos = [-1] * n
    for j in range(n):
        for i in range(n):
            if board[i][j] != 0:
                last_pos[j] = i
                break

    bucket = []
    for m in moves:
        m -= 1
        if last_pos[m] < n:  # 인형이 해당 열에 존재한다면
            doll = board[last_pos[m]][m]
            if len(bucket) > 0 and bucket[-1] == doll:
                answer += 2
                bucket.pop()
            else:
                bucket.append(board[last_pos[m]][m])
            board[last_pos[m]][m] = 0
            last_pos[m] += 1

    return answer