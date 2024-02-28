# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):

    s = list(s)

    answer = len(s)
    # a a b b a c c c
    # for x in range(1, len(s) // 2 + 1):
    #     comp_len = 0
    #     comp = ''
    #     cnt = 1
    #     for i in range(0, len(s) + 1 , x):
    #         tmp = s[i:i+x]
    #         if comp == tmp: cnt += 1
    #         else:
    #             comp_len += len(tmp)
    #             if cnt > 1: comp_len += len(str(cnt))
    #             cnt = 1
    #             comp = tmp

    #     answer = min(answer, comp_len)

    for i in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = s[0:i]
        comp_len += i
        cnt = 1
        for j in range(i, len(s) + 1, i):
            temp = s[j:j+i]
            if temp == comp: cnt += 1
            else:
                if len(temp) == i:
                    comp_len += i
                else:
                    comp_len += len(temp)
                if cnt > 1: comp_len += len(str(cnt))
                cnt = 1
                comp = temp

        if cnt > 1: comp_len += len(str(cnt))
        answer = min(answer, comp_len)
    return answer


s = 'abcabcdede'
print(solution(s))
