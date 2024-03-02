#3진법 뒤집기
#https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    base = []
    while n != 0:
        #div와 mod를 따로 나누지 않아도 됨
        n, div = divmod(n, 3)
        base.append(div)
        #base.insert(0, div)

    """
    for i in range(0, len(base)):
        answer += base[i] * (3**i)
    """
    #int(string, x진법에 해당하는 x)를 넣으면 알아서 숫자로 변환해줌
    return int(''.join(map(str, base)), 3)


print(solution(45))
