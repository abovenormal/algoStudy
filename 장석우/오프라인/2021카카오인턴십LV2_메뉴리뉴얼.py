def solution(info, query):
    tmpq = []
    for s in query:
        tmpq.append(s[:-4].split(' and '))
        tmpq[-1].append(s[-3:])
    tmpi = []
    for s in info:
        tmpi.append(s.split(' '))
    print(tmpi)
    print(tmpq)
    answer = []
    for s in query:

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)