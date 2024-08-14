n = int(input())

move = []
# 리턴: 이동 횟수
def process(n, start, mid, end):        # (원판 수, 시작 기둥, 중간 기둥, 끝 기둥): start -> end 로 옮긴다는 의미
    if n <= 1:
        move.append((start, end))
        return 1

    cnt = 0
    cnt += process(n-1, start, end, mid)        # 가장 큰 원판을 제외한 n-1 개의 원판을 보조 기둥으로 이동
    cnt += process(1, start, mid, end)      # 가장 큰 원판 1개를 마지막 기둥으로 이동
    cnt += process(n-1, mid, start, end)        # 보조 기둥에 있던 n-1 개를 마지막 기둥으로 이동

    return cnt

print(process(n, 1, 2, 3))
for _from, _to in move:
    print(_from, _to)