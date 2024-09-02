import copy
from itertools import permutations

t = int(input())

def process(pref, partner):
    while check_fin(partner) == False:
        for girl in range(6, 11):       # 6번 ~ 10번까지 프러포즈하기
            if partner[girl] != 0: continue
            boy = propose(girl, pref)
            decide(partner, pref, boy, girl)
    rate = prefer[1].index(partner[1])
    return rate

def propose(girl, pref):
    # 가장 좋아하는 남학생에게 프러포즈
    # (그 남학생이 퇴짜를 놓은 적이 있다면 (-1), 다음 남학생에게 프러포즈)
    for i in range(len(pref[girl])):
        if pref[girl][i] != -1:
            return pref[girl][i]

def decide(partner, pref, boy, _from):
    # 현재 짝이 없으면, 무조건 프러포즈 받아들이기
    if partner[boy] == 0:
        partner[boy] = _from
        partner[_from] = boy
    # 현재 짝이 있으면, 두명에 대한 자신의 선호도 비교해서 더 좋아하는 여자랑 짝 && 나머지 한명에게 퇴짜
    else:
        ori_girl = partner[boy]
        new_rate = pref[boy].index(_from)
        ori_rate = pref[boy].index(ori_girl)
        if new_rate < ori_rate:                                # 새 여자랑 짝
            partner[ori_girl] = 0
            pref[ori_girl][pref[ori_girl].index(boy)] = -1
            partner[boy] = _from
            partner[_from] = boy
        else:                                                  # 기존 여자랑 짝 유지
            pref[_from][pref[_from].index(boy)] = -1

def check_fin(partner):        # 모든 학생들이 짝을 찾았는지 체크    
    for i in range(1, 11):
        if partner[i] == 0:
            return False
    return True

for _t in range(t):
    answer = False

    prefer = [[] for _ in range(11)]
    prefer[1] = [6,7,8,9,10]
    for i in range(2, 11):
        prefer[i] = list(map(int, input().split()))
     
    # 현재 선호도일때 태현이가 맺어지는 여학생
    pref = copy.deepcopy(prefer)
    partner = [0] * 11
    ori_rate = process(pref, partner)
    
    # 0 순위 여학생과 맺어졌다면, 선호도 바꾸기 X
    if ori_rate == 0:
        print("NO")
        continue

    # 선호도를 바꿨을 때 어떻게 되는가
    permus = list(permutations(prefer[1], 5))
    for permu in permus:
        pref = copy.deepcopy(prefer)
        pref[1] = list(permu)
        partner = [0] * 11
        new_rate = process(pref, partner)
        if new_rate < ori_rate:
            answer = True
            break

    if answer: print("YES")
    else: print("NO")