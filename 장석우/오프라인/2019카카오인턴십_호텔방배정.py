# k는 1이상 1*e12 이하
# room_number 배열 크기는 1 이상 200,000이하


def solution(k, room_number):
    answer = []
    for reception in room_number:
        if reception not in answer:
            answer.append(reception)
        else:
            val = select(reception, k, answer)
            answer.append(val)
    return answer

def select(n, k, arr):
    start = n
    end = k
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if mid not in arr:
            end = mid - 1
            ans = mid
        else:
            start = start + 1
    return ans

k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))