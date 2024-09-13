def solution(friends, gifts):
    fdict = dict()
    for i, friend in enumerate(friends):
        fdict[friend] = i
    n = len(friends)
    graph = [[0] * n for _ in range(n)]
    gidxs = [[0, 0] for _ in range(n)]

    for gift in gifts:
        a, b = gift.split(' ')
        aidx, bidx = fdict[a], fdict[b]
        graph[aidx][bidx] += 1
        gidxs[aidx][0] += 1
        gidxs[bidx][1] += 1

    for gidx in gidxs:
        gidx.append(gidx[0] - gidx[1])

    answer = 0
    for friend in friends:
        cnt = 0
        i = fdict[friend]
        for j in range(n):
            if i == j: continue
            i_to_j = graph[i][j]
            j_to_i = graph[j][i]
            if i_to_j > j_to_i: cnt += 1
            if i_to_j == j_to_i:
                i_gidx = gidxs[i][2]
                j_gidx = gidxs[j][2]
                if i_gidx > j_gidx: cnt += 1
        answer = max(answer, cnt)
    return answer