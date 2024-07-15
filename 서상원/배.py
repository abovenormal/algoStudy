import sys
input=sys.stdin.readline

N=int(input()) # 크레인 수
crane = list(map(int,input().split()))
M=int(input()) # 박스 수
box = list(map(int,input().split()))

crane.sort(reverse=True)
box.sort()
answer=0


if crane[0] < box[-1] :
    print(-1)

else:
    while box:
        idx = len(box)
        for c in crane:  # 무거운 크레인 부터
            for i in range(idx - 1, -1, -1):  # 무거운 박스 부터 꺼내기
                if c >= box[i]:
                    box.remove(box[i])
                    idx=i
                    break
                else:  # 크레인이 처리하지 못한다면은 넘긴다
                    continue

        answer += 1

    print(answer)
