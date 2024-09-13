# user_id배열크기는 1~8, 각 원소길이는 1~8
# 문자 하나씩 다 체크 해도 시간복잡도는 ok

from itertools import combinations
import math
def solution(user_id, banned_id):
    arr = dict()
    answer = 1
    for banned in banned_id:
        arr[banned] = []
        for user in user_id:
            eflag = True
            if len(banned) != len(user): continue
            for s_banned, s_user in zip(banned, user):
                if s_banned != '*' and s_banned != s_user:
                    eflag = False
            if eflag:
                arr[banned].append(user)
    multiplied = []
    usercnt = dict()
    for user in user_id:
        selected = []
        ucnt = 0
        for banned in banned_id:
            if banned in selected: continue
            if user in arr[banned]:
                ucnt += 1
            selected.append(banned)
        usercnt[user] = ucnt

    for banned in banned_id:
        if banned in multiplied: continue
        cnt = banned_id.count(banned)
        if cnt > 1:
            multiplied.append(banned)
            answer *= len(list((combinations(arr[banned],cnt))))
        else:
            multiplied.append(banned)
            answer *= len(arr[banned])
    minus = 0
    for user in user_id:
        tmp = usercnt[user]
        if tmp > 1:
            if minus == 0:
                minus = eval(tmp)
            else:
                minus *= eval(tmp)
    answer -= minus
    print(arr)
    print(usercnt)
    print(minus)
    return answer

def eval(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return math.comb(n,n) + math.comb(n,n-1)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))