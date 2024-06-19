# board 5*5 ~ 30*30, 인형종류는 100가지, moves는 1~1000
# 1000moves에 거쳐서 900가지를 탐색해도 시간복잡도는 900000정도로 넉넉하다


def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            item = board[i][move-1]
            if item == 0 : continue
            basket.append(item)
            board[i][move-1] = 0
            if len(basket) > 1:
                if basket[-1] == basket[-2]:
                    answer += 2
                    basket = basket[:-2]
            break
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))