#3진법 뒤집기
#https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    base = []
    while n != 0:
        div = n % 3
        n = n // 3
        base.insert(0, div)
    print(base)
    for i in range(0, len(base)):
        answer += base[i] * (3**i)
    return answer


print(solution(45))
