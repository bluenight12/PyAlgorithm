def solution(n):
    answer = []
    i = 1
    x1, x2, y1, y2 = 1, n - 1, 0, n - 1
    for j in range(0, n):
        answer.append([0] * (j + 1))
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    t = 0
    x, y = 0, 0
    for i in range(1, int((n * (n+1))/2 + 1)):
        answer[x][y] = i
        x += dx[t]
        y += dy[t]
        if t == 0 and x == x2:
            t = 1
            x2 -= 1
        elif t == 1 and y == y2: 
            t = 2
            y2 -= 1
        elif t == 2 and x == x1: 
            t = 0
            x1 += 1
        
            

    return list(map(''.join, answer))

if __name__ == "__main__":
    print(solution(5))