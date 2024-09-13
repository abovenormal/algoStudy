# 5<=n<=1,000,000, 0<=k<n, 1<=cmd원소개수<=200,000

from heapq import heappush, heappop

def solution(n, k, cmd):
    delyn = ['O'] * n
    chart = [i for i in range(n)]
    selected = k
    delq = []
    for _cmd in cmd:
        print(delyn, chart, selected,delq)
        if _cmd[0] == 'U':
            move = int(_cmd[2:])
            selected = selected - move
            if selected < 0:
                selected = 0
        elif _cmd[0] == 'D':
            move = int(_cmd[2:])
            selected = selected + move
            if selected > len(chart)-1:
                selected = len(chart)-1
        elif _cmd[0] == 'C':
            item = chart[selected]
            delq.append(item)
            delyn[item] = 'X'
            chart.remove(item)
            if selected > len(chart)-1:
                selected=len(chart)-1
        elif _cmd[0] == 'Z':
            item = delq.pop()
            delyn[item] = 'O'
            num = delyn[:item].count('X')
            chart = chart[:item-num] + [item] + chart[item-num:]
            if selected >= item-num:
                selected += 1
    answer = ''
    for i in delyn:
        answer += i
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))