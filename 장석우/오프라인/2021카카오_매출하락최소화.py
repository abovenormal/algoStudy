def solution(sales, links):
    graph = [[] for _ in range(len(sales)+1)]
    level = [[0,0] for _ in range(len(sales)+1)]
    for i, j in links:
        graph[i].append(j)
        level[j][0] = i
        level[j][1] = level[i][1] - 1

    print(graph)
    print(level)

    answer = 0
    return answer

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
solution(sales, links)