def solution(s):
    answer = []
    #s = list(s)
    n = [0, 0]
    cnt = 0
    while s != '1':
        cnt = s.count('1')
        # 이 작업을 하는게 list로 바꾸지 말고 count 쓰기
        '''
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
        '''
        n[0] += 1
        n[1] += len(s) - cnt
        s = bin(cnt)[2:]

    return n

print(solution('1111111'))