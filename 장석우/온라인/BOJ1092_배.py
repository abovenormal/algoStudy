# 시간제한2초, 메모리제한128MB
# n ~ 50, 무게제한 ~ 1,000,000, m ~ 10,000, 박스무게 ~ 1,000,000
# 완전탐색불가, 그리디로 접근

n = int(input())
cranes = list(map(int,input().split()))
cranes.sort(reverse=True)

m = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)

cnt = 0

if boxes[0] > cranes[0] : cnt = -1
else:
    while boxes:
        for crane in cranes:
            if boxes and crane < boxes[-1]:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        cnt += 1
print(cnt)

