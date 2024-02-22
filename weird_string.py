# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = list(s)
    idx = 0
    for i in range(len(answer)):
        if answer[i] == ' ': idx = 0; continue
        answer[i] = answer[i].upper() if idx % 2 == 0 else answer[i].lower()
        idx += 1
            
    return ''.join(answer)