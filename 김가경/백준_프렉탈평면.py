# 문제 이해부터 어려움을 겪어 타 블로그 답을 참고했으며 다시 풀어보았습니다..!

def fractal_pattern(s, N, K, R1, R2, C1, C2):
    result = []
    for r in range(R1, R2 + 1):
        row = []
        for c in range(C1, C2 + 1):
            if is_black(s, N, K, r, c):
                row.append('1')
            else:
                row.append('0')
        result.append(''.join(row))
    return result

def is_black(s, N, K, r, c):
    if s == 0:
        return False
    
    segment_size = N ** s
    mid_size = (N - K) // 2
    
    r_segment = (r % segment_size) // (segment_size // N)
    c_segment = (c % segment_size) // (segment_size // N)
    
    if mid_size <= r_segment < mid_size + K and mid_size <= c_segment < mid_size + K:
        return True
    
    return is_black(s - 1, N, K, r, c)

s, N, K, R1, R2, C1, C2 = map(int, input().split())

pattern = fractal_pattern(s, N, K, R1, R2, C1, C2)

for line in pattern:
    print(line)
