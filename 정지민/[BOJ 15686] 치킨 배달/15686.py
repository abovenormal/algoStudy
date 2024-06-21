from itertools import combinations

n, m = map(int, input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if _map[i][j] == 1:
            house.append((i,j))
        elif _map[i][j] == 2:
            chicken.append((i,j))

chicken_candis = list(combinations(chicken, m ))

answer = 1e9
for chicken_candi in chicken_candis:
    total_dist = 0
    for hr, hc in house:
        house_dist = 1e9
        for i in range(m):
            house_dist = min(house_dist, abs(chicken_candi[i][0]-hr) + abs(chicken_candi[i][1]-hc))
        total_dist += house_dist
    answer = min(answer, total_dist)

print(answer)