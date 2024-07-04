from itertools import combinations

def is_matched(user, banned):
    if len(user) != len(banned):
        return False

    for i in range(len(user)):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True

def dfs(step, banned_list, banned_key_list, banned_id):
    global answer

    if step >= len(banned_id):
        for answer_set in answer_sets:
            if answer_set == set(banned_list):
                return

        answer += 1
        answer_sets.append(set(banned_list))
        return

    _key = banned_id[step]
    for banned in match_dict[_key]:
        if banned not in banned_list:
            banned_list.append(banned)
            dfs(step + 1, banned_list, banned_key_list, banned_id)
            banned_list.remove(banned)

banned_dict = dict()
match_dict = dict()
banned_key_list = []
answer = 0
answer_sets = []

def solution(user_id, banned_id):
    for id in banned_id:
        if id not in banned_dict:
            banned_dict[id] = 1
            match_dict[id] = []
        else:
            banned_dict[id] += 1

    banned_key_list = list(banned_dict.keys())

    for banned in banned_dict.keys():
        for user in user_id:
            if is_matched(user, banned):
                match_dict[banned].append(user)

    _key = banned_id[0]
    start = match_dict[_key]
    for start in match_dict[_key]:
        dfs(1, [start], banned_key_list, banned_id)

    return answer