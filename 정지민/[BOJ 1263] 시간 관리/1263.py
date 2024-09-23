'''
1. 아이디어: 마감기한이 늦은 것부터 채워간다.
    - 시간 순 그래프가 있다면 오른쪽(늦은 시간) 부터 채워가는 느낌으로 접근
    - 아이디어 떠올리는게 핵심..!!
    - 참고 블로그: https://nahwasa.com/entry/%EC%9E%90%EB%B0%94-%EB%B0%B1%EC%A4%80-1263-%EC%8B%9C%EA%B0%84-%EA%B4%80%EB%A6%AC-java
'''
n = int(input())
tasks = []
for _ in range(n):
    t, s = map(int, input().split())
    tasks.append((s, t))

tasks.sort(reverse = True)

time = tasks[0][0]

for i in range(n):
    limit_time = tasks[i][0]
    duration = tasks[i][1]

    if limit_time >= time:          # task 채워넣기
        time -= duration
    else:
        time = limit_time - duration
    
    if time < 0:
        print(-1)
        exit()

print(time)