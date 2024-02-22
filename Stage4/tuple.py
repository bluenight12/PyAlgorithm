# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    # dictionary 에 가장 많이 들어간 값(제일 처음으로 들어간 값) 을 기준으로 내림차순 정렬하면 tuple이 나온 순서대로 return 가능
    answer = {}
    data = s[2:-2].split('},{')
    for i in data:
        i = i.split(',')
        for val in i:
            val = int(val)
            answer[val] = 1 if val not in answer else answer[val] + 1
    answer = dict(sorted(answer.items(), key = lambda x : x[1], reverse= True))
    return list(answer)

    '''
    data = s[2:-2].split('},{')
    
    # 글자 개수로 sorted
    data = sorted(data, key=lambda x : len(x))
    
    for item in data:
        
        item = item.split(',')
            
        for value in item:
            value = int(value)
            if value not in answer:
                answer[value] = 1
    # dictionary를 list로 추출 하면 key값만 나옴
    return list(answer)
    # 양옆 중괄호를 2개씩 삭제한뒤에 },{를 삭제하면 숫자만 남음
    # list의 탐색 시간은 n 이므로 O(n^2) 급이 되어버림
    # dictionary의 탐색 시간은 1이고 넣어야 할 키는 하나기 때문에 괜찮음
    '''
    '''
    data = s[2:-2].split('},{')
    
    # 글자 개수로 sorted
    data = sorted(data, key=lambda x : len(x))
    
    for item in data:
        #map(자료형, 나열 할 자료)
        item = list(map(int, item.split(',')))
        # 밑의 작업을 위에 한문장으로 가능
        #item = item.split(',')
        #for i in range(0, len(item)):
        #    item[i] = int(item[i])
            
        print(item)
        for value in item:
            if value not in answer:
                answer.append(value)
    return answer
    '''
    # s = list(s)
    # s.pop(0)
    # s.pop(-1)
    # idx = 0
    # tmp = []
    # for i in s:
    #     if i == '{': answer.append([])
    #     elif i == '}': 
    #         answer[idx].append(int(''.join(tmp)))
    #         tmp = []
    #         idx += 1
    #     elif i == ',':
    #         if tmp == []: continue 
    #         answer[idx].append(int(''.join(tmp)))
    #         tmp = []
    #     else: tmp.append(i)
    # # answer[idx].append(i)
    # answer.sort(key = len)
    # idx = 0
    # result = []
    # result.append(answer[idx][0])
    # for i in range(1, len(answer)):
    #     for j in range(0, i):
    #         answer[i].remove(answer[j][0])
            
    #     result.append(answer[i][0])    
    # return result

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)