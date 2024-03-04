# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def collatz(n, i):
    if n == 1: return i
    if i == 501: return -1
    if n % 2 == 0:
        return collatz(n // 2, i + 1)
    else:
        return collatz(n * 3 + 1, i + 1)


def solution(num):
    print(collatz(num, 0))


solution(626331)
