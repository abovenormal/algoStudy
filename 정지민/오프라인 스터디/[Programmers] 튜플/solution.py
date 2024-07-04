def solution(s):
    subset = []
    splitted = list(s[1:-1].split("},"))
    n = len(splitted)

    for i in range(n):
        if i == n - 1:
            subset.append(splitted[i][1:].split(","))
            subset[n - 1][-1] = int(subset[n - 1][-1][0:-1])
            subset[n - 1] = sorted(list(map(int, subset[n - 1])))
        else:
            subset.append(sorted(list(map(int, splitted[i][1:].split(",")))))

    subset.sort(key=lambda x: len(x))

    check = [False] * 100001
    answer = [subset[0][0]]
    check[subset[0][0]] = True

    for _subset in subset:
        for i in range(len(_subset)):
            if check[_subset[i]] == False:
                answer.append(_subset[i])
                check[_subset[i]] = True
                break
    return answer