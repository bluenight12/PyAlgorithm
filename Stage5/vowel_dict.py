# 모음 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

import sys

sys.setrecursionlimit(100000)

v = ['A', 'E', 'I', 'O', 'U']


# 문제가 원하는 답의 갯수가 적을 때는 직접 만드는 것도 나쁘지 않다.
def find(data, p, step):
    if step == 6:
        return
    if p != '': data.append(p)
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([p, c]), step + 1)


def vowel(i, st):
    flag = 1
    for j in range(0, min(len(st), len(ans))):
        if st[j] != ans[j]:
            flag = 0
    if flag == 1 and len(st) == len(ans):
        return i
    if len(st) != 5:
        st.append(0)
        return vowel(i + 1, st)
    else:
        return vowel(i + 1, plus(4, st))


def plus(i, st):
    st[i] += 1
    if st[i] == 5:
        st.pop()
        plus(i - 1, st)
    return st


def solution(word):
    answer = 0
    st = [0]
    global ans
    ans = [v.index(i) for i in word]

    return vowel(1, st)


print(solution('U'))
