def solution(s):
    answer = ""

    _map = dict()
    _map['zero'] = 0
    _map['one'] = 1
    _map['two'] = 2
    _map['three'] = 3
    _map['four'] = 4
    _map['five'] = 5
    _map['six'] = 6
    _map['seven'] = 7
    _map['eight'] = 8
    _map['nine'] = 9

    num_str = ""
    for _s in s:
        if _s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer += str(_s)
        else:
            num_str += _s
            if num_str in _map.keys():
                answer += str(_map[num_str])
                num_str = ""

    return int(answer)