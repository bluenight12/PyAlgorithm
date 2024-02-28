# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def compress(s, length):

    # length 1 부터 len의1/2 + 1 까지
    words = [s[i:i + length] for i in range(0, len(s), length)]
    # 단어 갯수와 나온 횟수를 파악할 List
    res = []
    # 첫 비교 word ( 처음에 짰던 방식과 유사 )
    cur_word = words[0]
    # 처음에 단어를 가지고 비교하기 때문에 초기값 1
    cur_cnt = 1
    for pattern, compare in zip(words, words[1:] + ['']):
        if pattern == compare: cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = compare
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(s):
    if len(s) == 1: return 1
    else : return min(compress(s, length) for length in list(range(1, len(s) // 2 + 1)))
    #s = list(s)

    #answer = len(s)
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
    '''
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
    '''


s = 'abcabcdede'
print(solution(s))
