# 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948

import re
def solution(s):
    return re.sub('\d(?=\d{4})','*',s)
    
print(solution('01002030102'))