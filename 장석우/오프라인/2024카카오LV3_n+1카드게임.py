def solution(coin, cards):
    from collections import deque
    n = len(cards)
    cards = deque(cards)
    hand = [0] * (n + 1)
    tmp = []
    for _ in range(n // 3):
        selected = cards.popleft()
        tmp.append(selected)
        hand[selected] = 1
    checked = [0] * (len(tmp))
    couple = deque([])
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if i == j: continue
            if checked[i] and checked[j]: continue
            if tmp[i] + tmp[j] == n + 1:
                couple.append((tmp[i], tmp[j]))
                checked[i] = 1
                checked[j] = 1
    answer = 0
    while cards:
        print(couple, hand,coin)
        answer += 1
        select1 = cards.popleft()
        select2 = cards.popleft()
        want1 = n + 1 - select1
        want2 = n + 1 - select2
        if hand[want1] and coin:
            coin -= 1
            hand[select1] = 1
            couple.append((select1, want1))
        if hand[want2] and coin:
            coin -= 1
            hand[select2] = 1
            couple.append((select2, want2))
        if not couple: break
        if couple:
            c1, c2 = couple.popleft()
            hand[c1] = 0
            hand[c2] = 0

    return answer

coin = 4
cards= [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]

print(solution(coin, cards))