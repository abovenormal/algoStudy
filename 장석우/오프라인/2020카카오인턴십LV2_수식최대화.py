# expression은 길이가 3~100 문자열
from itertools import permutations

def solution(expression):
    arr = ['*','+','-']
    res = 0
    _expression = expression[:]
    for evaluators in permutations(arr):
        e1, e2, e3 = evaluators
        s1 = []
        s2 = []
        tmp = ''
        for i in expression:
            if i.isdigit():
                tmp += i
            else:
                s1.append(tmp)
                tmp = ''
                s2.append(i)


    return res

expression = "100-200*300-500+20"

print(solution(expression))