#


def solution(new_id):
    tmp = []
    for i in new_id:
        if i.isalpha(): tmp.append(i.lower())
        if not i.isalpha():
            if i.isdigit():
                tmp.append(i)
                continue
            if not (i == '-' or i == '_' or i == '.'):
                continue
            tmp.append(i)
    tmp2 = []
    for i in range(len(tmp)):
        if tmp2 and tmp[i] == '.' and tmp2[-1] == '.':
            continue
        tmp2.append(tmp[i])
    print(tmp2)
    if tmp2 and tmp2[0] == '.':
        tmp2 = tmp2[1:]
    if tmp2 and tmp2[-1] == '.':
        tmp2 = tmp2[:-1]
    if not tmp2: tmp2 = ['a']
    if len(tmp2) >= 16:
        tmp2 = tmp2[:15]
        if tmp2[-1] == '.':
            tmp2 = tmp2[:-1]
    if len(tmp2) <= 2:
        while len(tmp2) < 3:
            tmp2 += [tmp2[-1]]
    answer = ''
    for i in tmp2:
        answer+=i
    return answer

print(solution("abcdefghijklmn.p"
))