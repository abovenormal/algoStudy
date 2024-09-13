# gems 배열 크기 1~100,000

def solution(gems):
    gemset = set()
    for gem in gems:
        gemset.add(gem)
    idx = 0
    nxtidx = 0
    item = 0
    nxtitem = 0
    for i in range(1,len(gems)):
        gem = gems[i-1]
        if not item:
            item = gem
            idx = i
            gemset.remove(item)
        else:
            if gem in gemset:
                gemset.remove(item)
                if not nxtidx:
                    nxtidx = i
                    nxtitem = gem
            if gem == nxtitem:
                nxtidx = i
            if gem == item:


    answer=[]
    return answer