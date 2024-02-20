from functools import reduce
from itertools import chain
def solution(n):
    answer = []
    x1, x2, y1, y2 = 1, n - 1, 0, n - 1
    answer = [[0] * i for i in range(1, n+1)]
    # for j in range(0, n):
    #     answer.append([0] * (j + 1))
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    t = 0
    x, y = 0, 0
    # 나누기를 int로 변환하려면 
    # n * (n + 1) // 2, len(snail)과 동일
    for i in range(1, int((n * (n+1))/2 + 1)):
        answer[x][y] = i
        x += dx[t]
        y += dy[t]
        if t == 0 and x == x2:
            t = 1
            x2 -= 1
        elif t == 1 and y == y2: 
            t = 2
            y2 -= 2
        elif t == 2 and x == x1: 
            t = 0
            x1 += 2
            
        # ny와 nx로 미리 이동한 후에 틀리다면 다시 이동하는 식으로 해도 됨
        # nx = x + dx[t]
        # ny = y + dy[t]
        # if 0 <= nx < n and 0 <= ny <= nx and answer[nx][ny] == 0:
        # 굳이 끝 번호를 이용하지 않고 다음 위치에 숫자가 이미 들어가 있다면 넘어가는 식으로 하는게 x1 x2 y2를 쓰지 않고 할 수 있음
        
        # 다른 풀이로는 도는 순서는 결국 n 값에서 angle이 바뀔 때 마다 -1이 되므로
        # 4를 넣었을 때 아래 -> 오른쪽 -> 위 순으로 4 -> 3 -> 2 -> 1을 하면 완성이 된다
    
    
    # *는 unpacking 함수로써 2차원배열인 answer의 값을 각각 풀어줌
    #return list(chain(*answer))
    
    #return list(reduce(lambda x, y:x + y, answer))
    
    #return [i for j in answer for i in j]



if __name__ == "__main__":
    print(solution(7))