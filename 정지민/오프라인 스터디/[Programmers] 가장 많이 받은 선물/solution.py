def solution(friends, gifts):
    answer = 0
    
    n = len(friends)
    name_num = dict()
    for i in range(len(friends)):
        name_num[friends[i]] = i
    
    graph = [[0]*n for _ in range(n)]
    for gift in gifts:
        _list = list(gift.split(" "))
        _from, _to = _list[0], _list[1]
        _from = name_num[_from]
        _to = name_num[_to]
        graph[_from][_to] += 1
    
    # 선물 지수 구하기
    rate = [0] * n
    for i in range(n):
        give, get = 0, 0
        for j in range(n):
            give += graph[i][j]
        for j in range(n):
            get += graph[j][i]
        rate[i] = give - get
    
    cnt = [0] * n
    for _from in range(n):
        for _to in range(n):    
            # 두 사람 사이에 선물 기록이 있다면 -> 이번 달까지 더 많은 선물을 준 사람이 하나 받는다.
            if (graph[_from][_to] != 0 or graph[_to][_from] != 0) and (graph[_from][_to] != graph[_to][_from]):
                if graph[_from][_to] > graph[_to][_from]:
                    cnt[_from] += 1
                else:
                    cnt[_to] += 1
            # 두 사람 사이에 선물 기록이 없다면 -> 선물 지수가 더 큰 사람이 하나 받는다.
            else:
                if rate[_from] == rate[_to]: continue
                
                if rate[_from] > rate[_to]:
                    cnt[_from] += 1
                else:
                    cnt[_to] += 1

    answer = max(cnt) // 2
    return answer