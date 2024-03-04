# 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918

import re
def solution(s):
    answer = False
    if (len(s) == 4 or len(s) == 6) and re.search('^[0-9]*$', s): answer = True
    return answer