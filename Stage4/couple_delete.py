# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    
    l = ['',s[0]]
    for i in s[1:]:
        if l[-1] != i:
            l.append(i)
        else:
            l.pop()
    answer = 1 if len(l) == 1 else 0
    return answer
    
    '''
    answer = -1
    s = list(s)
    n = 0
    start, end = 0, 1
    tmp = []
    # 0 1 2 3 4 5 
    while end < len(s):
        if start < 0 or s[start] == ' ':
            start = end
            end += 1
        if end >= len(s):
            break
        if s[start] == s[end]:
            n += 2
            s[start] = ' '
            s[end] = ' '
            start -= 1
            if tmp:
                start = tmp[-1]
                tmp.pop(-1)
            end += 1
        else:
            tmp.append(start)
            start = end
            end += 1
        
            
    answer = 1 if n == len(s) else 0
    return answer
    '''


stn = 'azzbxxccddsszzvvaawweerrabccbaba'
print(solution(stn))