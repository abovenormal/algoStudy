''' 1트 => 실패. 이진트리 자료구조 없이 dfs 로만 시도.
[ 문제점 ]
1. 어떤 노드들끼리 부모-자식 노드로 연결되어 있는지 찾지 못함.
'''
# def pre_order(cur, visited, node_pos, nodeinfo, path):
#     global max_x

#     if len(path) == len(nodeinfo):
#         return path

#     cur_x, cur_y = cur[0], cur[1]
#     visited[(cur_x, cur_y)] = True
#     path.append(node_pos[(cur_x, cur_y)])

#     # 자식 노드들 중 왼쪽부터 방문
#     for y in range(cur_y-1, -1, -1):
#         for x in range(cur_x-1, -1, -1):
#             if (x,y) in node_pos and not visited[(x,y)]:
#                 pre_order([x,y], visited, node_pos, nodeinfo, path)

#     # 왼쪽에 방문할 자식이 없으면, 자식 노드들 중 오른쪽 방문
#     for y in range(cur_y-1, -1, -1):
#         for x in range(cur_x+1, max_x+1):
#             if (x,y) in node_pos and not visited[(x,y)]:
#                 pre_order([x,y], visited, node_pos, nodeinfo, path)

# max_x = 0

# def solution(nodeinfo):
#     global max_x
#     answer = []

#     # (노드 위치 - 노드 넘버) 딕셔너리
#     node_pos = dict()
#     visited = dict()
#     for i in range(len(nodeinfo)):
#         node_pos[(nodeinfo[i][0], nodeinfo[i][1])] = i+1
#         visited[(nodeinfo[i][0], nodeinfo[i][1])] = False

#     nodeinfo.sort(key = lambda x : (-1 * x[1], x[0]))
#     for ni in nodeinfo:
#         max_x = max(max_x, ni[0])

#     pre_arr = pre_order(nodeinfo[0], visited, node_pos, nodeinfo, [])
#     answer.append(pre_arr)

#     return answer



''' 2트 => 답 참고.
1. 주어진 좌표들로 이진트리를 구성하는 것이 핵심.
'''
import sys
sys.setrecursionlimit(10 ** 9)

class Node(object):
    def __init__(self, info):
        self.num = info[2]
        self.pos = info[:2]
        self.left = None
        self.right = None

def add_node(parent, info):
    if parent.pos[0] > info[0]:
        if parent.left:                         # 이미 parent 의 left 노드가 이미 존재하면, 그 노드의 하위에 달아준다.
            add_node(parent.left, info)
        else:
            parent.left = Node(info)
    else:
        if parent.right:
            add_node(parent.right, info)
        else:
            parent.right = Node(info)

def pre_order(cur):
    path = [cur.num]
    if cur.left:
        path += pre_order(cur.left)
    if cur.right:
        path += pre_order(cur.right)
    return path

def post_order(cur):
    path = []
    if cur.left:
        path += post_order(cur.left)
    if cur.right:
        path += post_order(cur.right)
    path.append(cur.num)
    return path

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    nodeinfo.sort(key=lambda x: (-1 * x[1], x[0]))

    # 루트 노드를 설정하고, add_node 함수를 통해 트리 구조를 셋팅
    root = Node(nodeinfo[0])
    for info in nodeinfo[1:]:
        add_node(root, info)

    return [pre_order(root), post_order(root)]