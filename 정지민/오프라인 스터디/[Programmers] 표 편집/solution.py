''' 1트 => 정확성 테케 21, 27 실패 / 효율성 테케 6,7,8,9,10 실패
'''
# def solution(n, k, cmd):
#     answer = ''

#     deleted = []
#     current_row = k
#     is_deleted = [False] * n

#     for _cmd in cmd:
#         command, x = "", 0
#         if len(_cmd) == 1:
#             command = _cmd
#         else:
#             command, x = _cmd.split(" ")
#             x = int(x)

#         # u x : 현재 선택된 행에서 x 칸 위에 있는 행 선택
#         if command == 'U':
#             cnt = 0
#             for row in range(current_row-1, -1, -1):
#                 if is_deleted[row] == False:
#                     cnt += 1
#                 if cnt == x:
#                     current_row = row
#                     break

#         # d x : 현재 선택된 행에서 x 칸 아래에 있는 행 선택
#         elif command == 'D':
#             cnt = 0
#             for row in range(current_row+1, n):
#                 if is_deleted[row] == False:
#                     cnt += 1
#                 if cnt == x:
#                     current_row = row
#                     break

#          # c : 현재 행 삭제 -> 다음 행 선택 / 마지막 행인 경우 -> 바로 윗 행 선택
#         elif command == 'C':
#             deleted.append(current_row)
#             is_deleted[current_row] = True
#             if current_row + 1 < n:
#                 cnt = 0
#                 for row in range(current_row+1, n):
#                     if is_deleted[row] == False:
#                         cnt += 1
#                     if cnt == 1:
#                         current_row = row
#                         break
#             else:
#                 cnt = 0
#                 for row in range(current_row-1, -1, -1):
#                     if is_deleted[row] == False:
#                         cnt += 1
#                     if cnt == 1:
#                         current_row = row
#                         break

#         # z : 최근 삭제된 행을 복구 (현재 선택된 행 바꾸지 X)
#         else:
#             if len(deleted) > 0:
#                 row = deleted.pop()
#                 is_deleted[row] = False

#     for _row in range(n):
#         if is_deleted[_row]:
#             answer += 'X'
#         else:
#             answer += 'O'
#     return answer


''' 2트 => LinkedList 없이 풀이. 근데 안됨. 정확성 100% / 효율성 테케 3,4,5 만 통과. 왜?-? 
https://velog.io/@yuiopre98/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level-3-%ED%91%9C-%ED%8E%B8%EC%A7%91
'''
# def solution(n, k, cmd):
#     deleted = []
#     current_row = k
#     table_size = n

#     for _cmd in cmd:
#         command, x = "", 0
#         if len(_cmd) == 1:
#             command = _cmd
#         else:
#             command, x = _cmd.split(" ")
#             x = int(x)

#         # u x : 현재 선택된 행에서 x 칸 위에 있는 행 선택
#         if command == 'U':
#             current_row -= x

#         # d x : 현재 선택된 행에서 x 칸 아래에 있는 행 선택
#         elif command == 'D':
#             current_row  += x

#          # c : 현재 행 삭제 -> 다음 행 선택 / 마지막 행인 경우 -> 바로 윗 행 선택
#         elif command == 'C':
#             deleted.append(current_row)
#             table_size -= 1
#             if current_row == table_size:
#                 current_row -= 1

#         # z : 최근 삭제된 행을 복구 (현재 선택된 행 바꾸지 X)
#         else:
#             recent = deleted.pop()
#             if recent <= current_row:
#                 current_row += 1
#             table_size += 1

#     ans_arr = ['O'] * table_size
#     while len(deleted) > 0:
#         ans_arr.insert(deleted.pop(), "X")

#     answer = "".join(ans_arr)
#     return answer


''' 3트 => Linked List 사용
'''
def solution(n, k, cmd):
    deleted = []
    current_row = k

    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]

    answer = ['O'] * n

    for _cmd in cmd:
        command, x = "", 0
        if len(_cmd) == 1:
            command = _cmd
        else:
            command, x = _cmd.split(" ")
            x = int(x)

        # u x : 현재 선택된 행에서 x 칸 위에 있는 행 선택
        if command == 'U':
            for _ in range(x):
                current_row = table[current_row][0]

        # d x : 현재 선택된 행에서 x 칸 아래에 있는 행 선택
        elif command == 'D':
            for _ in range(x):
                current_row = table[current_row][1]

        # c : 현재 행 삭제 -> 다음 행 선택 / 마지막 행인 경우 -> 바로 윗 행 선택
        elif command == 'C':
            answer[current_row] = 'X'
            _prev, _next = table[current_row]
            deleted.append([_prev, current_row, _next])

            if _next == None:  # 마지막 행인 경우 -> 바로 윗 행 선택
                current_row = _prev
            else:  # 마지막 행이 아닌 경우 -> 다음 행 선택
                current_row = _next

            # 링크드 리스트 연결 처리
            if _prev == None:  # 제일 윗 행 삭제인 경우
                table[_next][0] = None
            elif _next == None:  # 제일 마지막 행 삭제인 경우
                table[_prev][1] = None
            else:
                table[_prev][1] = _next
                table[_next][0] = _prev

        # z : 최근 삭제된 행을 복구 (현재 선택된 행 바꾸지 X)
        else:
            _prev, _cur, _next = deleted.pop()
            answer[_cur] = 'O'
            if _prev == None:  # 제일 윗 행 복구인 경우
                table[_next][0] = _cur
            elif _next == None:  # 제일 아래 행 복구인 경우
                table[_prev][1] = _cur
            else:
                table[_next][0] = _cur
                table[_prev][1] = _cur

    return ''.join(answer)