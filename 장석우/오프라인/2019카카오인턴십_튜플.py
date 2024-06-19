# s의 길이는 5 ~ 1,000,0000

def solution(s):
    answer = []
    _answer = []
    s = s.split('},{')
    for strings in s:
        strings = list(map(int,strings.strip('{}').split(',')))
        _answer.append(strings)
    _answer.sort(key = lambda x : len(x))
    for items in _answer:
        if items:
            for item in items:
                if item not in answer:
                    answer.append(item)
    return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))