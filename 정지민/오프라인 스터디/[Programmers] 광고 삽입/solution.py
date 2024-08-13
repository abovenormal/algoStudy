''' 1트 => 51.6 / 100 점. 나머지는 시간초과.
1. HH:MM:SS 형식의 문자열로 구성된 시간을 모두 초 단위로 변환하여 계산한다.
    - convert() 함수
2. 초 단위로 변환하여 계산한 시간을 다시 HH:MM:SS 형식의 문자열로 변환한다.
    - to_str() 함수
3. time[x]: x 초일때, 동영상을 시청하고 있는 사람 수
    - x 의 범위: 0 ~ total_time ("죠르디" 동영상의 총 재생 시간)
4. 사용자들의 시청 기록을 담은 logs 배열을 순회한다.
    하나의 시청 기록의 start_time ~ end_time 까지를 순회하며 time[i] += 1 해준다.
5. adv_time 만큼의 구간에서 가장 많은 시청자 수를 확보할 수 있는 구간 찾기 => 슬라이딩 윈도우 사용
    - 현재 구간의 시청자 수 총합인 cnt 값을 구하고, 그러한 cnt 값의 최대와 그때의 광고 시작 시간을 구한다.

[ 잘못된 부분 ]
- 이중 for 문에서 시간초과 걸리는 듯 ??
    - total_time 의 최댓값은 359999
    - 최악의 경우 시간복잡도가 약 360000 * 300000 이다.
- 근데 같은 로직으로 자바 코드는 통과되는데.... 파이썬이 느린 탓?
    - https://school.programmers.co.kr/questions/78472
        - 그냥 운좋게 워스트케이스가 테케에 없는 듯 + 파이썬보다 자바가 빨라서 대충 어케 통과되는 듯하다.
'''
def convert(time_str):
    time = 0
    temp = time_str.split(":")
    exp = 60 ** (len(temp) - 1)
    for t in temp:
        time += int(t) * exp
        exp = exp // 60
    return time

def to_str(time):
    answer = ''
    div = 60
    ans_arr = []
    for _ in range(2):
        num = str(time % div)
        if len(num) == 1:
            num = "0" + num
        ans_arr.append(num)
        time = time // div
    time = str(time)
    if len(time) == 1:
        time = "0" + time
    ans_arr.append(time)
    ans_arr.reverse()
    for ans in ans_arr:
        answer += ans
        answer += ":"
    return answer[:-1]

def solution(play_time, adv_time, logs):

    total_time = convert(play_time)
    adv_time = convert(adv_time)

    time = [0] * (total_time + 1)

    for log in logs:
        start_str = log.split("-")[0]
        end_str = log.split("-")[1]

        start_time = convert(start_str)
        end_time = convert(end_str)

        for i in range(start_time, end_time + 1):
            time[i] += 1

    # 구간 최댓값 찾기
    max_playtime = 0
    cnt = 0
    start_pos = 0

    for i in range(adv_time + 1):
        cnt += time[i]

    for i in range(adv_time + 1, total_time + 1):
        cnt = cnt - time[i - (adv_time + 1)] + time[i]
        if cnt > max_playtime:
            max_playtime = cnt
            start_pos = i - adv_time

    answer = to_str(start_pos)
    return answer



''' 2트 => 답 참고. 누적합 + 슬라이딩 윈도우. 93.5% 성공. 테케 9, 31 왜 실패?
1. time[x]: x 초일때, 동영상을 시청하고 있는 사람 수                
    - x 의 범위: 0 ~ total_time ("죠르디" 동영상의 총 재생 시간)
    - 1트에서와 똑같이 사용한다. 다만, 누적합을 이용해 구하면 시간복잡도를 줄일 수 있다.
2. traffic[x]: x 초일때, 시청자 유입/이탈 수
    - 유입 시청자는 +1, 이탈 시청자는 -1 로 계산
    - time[x] = time[x-1] + traffic[x]
    - traffic 의 누적합으로 time 을 구할수 있다.
'''
def convert(time_str):
    time = 0
    temp = time_str.split(":")
    exp = 60 ** (len(temp) - 1)
    for t in temp:
        time += int(t) * exp
        exp = exp // 60
    return time

def to_str(time):
    answer = ''
    div = 60
    ans_arr = []
    for _ in range(2):
        num = str(time % div)
        if len(num) == 1:
            num = "0" + num
        ans_arr.append(num)
        time = time // div
    time = str(time)
    if len(time) == 1:
        time = "0" + time
    ans_arr.append(time)
    ans_arr.reverse()
    for ans in ans_arr:
        answer += ans
        answer += ":"
    return answer[:-1]

def solution(play_time, adv_time, logs):
    total_time = convert(play_time)
    adv_time = convert(adv_time)

    time = [0] * 360000
    traffic = [0] * 360000

    # traffic 배열 채우기
    for log in logs:
        start_str = log.split("-")[0]
        end_str = log.split("-")[1]

        start_time = convert(start_str)
        end_time = convert(end_str)

        traffic[start_time] += 1
        traffic[end_time] -= 1

    # time 배열 채우기
    time[0] = traffic[0]
    for i in range(1, total_time + 1):
        time[i] = time[i - 1] + traffic[i]

    # 구간 최댓값 찾기
    max_playtime = 0
    cnt = 0
    start_pos = 0

    for i in range(adv_time):
        cnt += time[i]

    for i in range(adv_time, total_time):
        cnt = cnt - time[i - adv_time] + time[i]
        if cnt > max_playtime:
            max_playtime = cnt
            start_pos = i - adv_time + 1

    answer = to_str(start_pos)
    return answer



''' 3트 => 답 참고. 누적합 두번 사용.
1. time 배열 초기화
    : 유입 시청자는 +1, 이탈 시청자는 -1 로 계산
2. 첫번째 누적합 적용 -> time[i] = i ~ i+1 초 구간에서의 재생 횟수
    : time[x] = time[x-1] + time[x]
3. 두번째 누적합 적용 -> time[i] = 0 ~ i+1 초까지의 누적 재생 시간
4. 구간 합 알고리즘 사용
    : times[i] - time[i-adv_time] = i-adv_time+1 초 부터 광고를 시작했을 때 누적 재생 시간
'''
def convert(time_str):
    time = 0
    temp = time_str.split(":")
    exp = 60 ** (len(temp) - 1)
    for t in temp:
        time += int(t) * exp
        exp = exp // 60
    return time

def to_str(time):
    answer = ''
    div = 60
    ans_arr = []
    for _ in range(2):
        num = str(time % div)
        if len(num) == 1:
            num = "0" + num
        ans_arr.append(num)
        time = time // div
    time = str(time)
    if len(time) == 1:
        time = "0" + time
    ans_arr.append(time)
    ans_arr.reverse()
    for ans in ans_arr:
        answer += ans
        answer += ":"
    return answer[:-1]

def solution(play_time, adv_time, logs):

    play_time = convert(play_time)
    adv_time = convert(adv_time)

    time = [0] * 360000

    for log in logs:
        start_str = log.split("-")[0]
        end_str = log.split("-")[1]

        start_time = convert(start_str)
        end_time = convert(end_str)

        time[start_time] += 1
        time[end_time] -= 1

    for i in range(1, play_time + 1):
        time[i] += time[i-1]

    for i in range(1, play_time + 1):
        time[i] += time[i-1]

    # 구간 최댓값 찾기
    max_playtime = 0
    start_pos = 0

    for i in range(play_time):
        if i < adv_time - 1:
            if max_playtime < time[i]:
                max_playtime = time[i]
                start_pos = 0
        else:
            if max_playtime < time[i] - time[i-adv_time]:
                max_playtime = time[i] - time[i-adv_time]
                start_pos = i - adv_time + 1

    answer = to_str(start_pos)
    return answer