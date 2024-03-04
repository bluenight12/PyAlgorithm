# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def hanoi(n, start, mid, to, answer):
    if n == 1:
        return answer.append([start, to])
    # 먼저 n-1개의 탑을 경유지에 놔두고
    hanoi(n-1, start, to, mid, answer)
    answer.append([start, to])
    # 경유지에 있던 탑을 원래 가려고 했던 곳으로 놔둔다
    hanoi(n-1, mid, start, to, answer)
def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer


print(solution(3))
