#다른 사람의 코드를 참조했습니다
#따라하면서 연습했습니다 
from collections import deque

def solution(nodeinfo):
    answer = [[], []]
    nodes = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(len(nodeinfo))]
    
    # 노드를 y를 기준으로 내림차순, x를 기준으로 오름차순 정렬
    nodes = sorted(nodes, key=lambda x: (-x[1], x[0]))
    
    mdict = {}
    
    for x, y, idx in nodes:
        mdict[idx] = [x, y, None, None]  # [x, y, left, right]
        curr = nodes[0][2]  # 현재 노드 (루트 노드의 인덱스)
        
        while True:
            if x > mdict[curr][0]:  # 현재 노드의 x값보다 크면 오른쪽 자식
                if mdict[curr][3] is None:
                    mdict[curr][3] = idx
                    break
                curr = mdict[curr][3]
            elif x < mdict[curr][0]:  # 현재 노드의 x값보다 작으면 왼쪽 자식
                if mdict[curr][2] is None:
                    mdict[curr][2] = idx
                    break
                curr = mdict[curr][2]
            else:
                break

    # 전위 순회와 후위 순회를 통해 답을 구함
    for idx, order in enumerate([[3, 2], [2, 3]]):  # 전위 순회는 오른쪽 -> 왼쪽, 후위 순회는 왼쪽 -> 오른쪽
        stack = [nodes[0][2]]
        result = deque()
        while stack:
            curr = stack.pop()
            if idx == 0:
                result.append(curr)  # 전위 순회
            else:
                result.appendleft(curr)  # 후위 순회
            
            for child in order:
                if mdict[curr][child] is not None:
                    stack.append(mdict[curr][child])
        answer[idx] = list(result)
    
    return answer
