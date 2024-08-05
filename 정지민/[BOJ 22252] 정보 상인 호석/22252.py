import heapq

q = int(input())
names = dict()
answer = 0

for _ in range(q):
    _input = list(input().split())

    if _input[0] == '1':
        name = _input[1]
        if name in names:
            for i in range(3, len(_input)):
                heapq.heappush(names[name], -1 * int(_input[i]))
        else:
            pq = []
            for i in range(3, len(_input)):
                heapq.heappush(pq, -1 * int(_input[i]))
            names[name] = pq

    else:
        name = _input[1]
        b = int(_input[2])

        if name not in names: continue

        if b <= len(names[name]):
            for _ in range(b):
                answer += -1 * heapq.heappop(names[name])
        else:
            answer += -1 * sum(names[name])
            del(names[name])

print(answer)