def solution(rows, columns, queries):
    answer = []
    i = 1
    matrix = []
    for j in range(0, rows):
        mat = [i for i in range(i, columns + i)]
        i += columns
        matrix.append(mat)
    # matrix = [ [i * columns + (j + 1) for j in range(0, columns)] for i in range(0, rows)]        
    # 한줄로 변환 가능
    for i in queries:
        x1, y1, x2, y2 = i
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        # x1, y1, x2, y2 = i[0] - 1, i[1] -1, i[2] - 1, i[3] - 1
        min = matrix[x1][y1]
        mem = min
        tmp = min
        # 가로 list는 x1 부터 x2-1까지 잘라서 x1 + 1부터 x2 까지 갖다 붙이기
        # 전 값을 받으면 tmp와 mem 없이 할 수 있음
        for j in range(y1, y2):
            tmp = matrix[x1][j+1]
            if(tmp < min) : min = tmp
            matrix[x1][j+1] = mem
            mem = tmp
        for j in range(x1, x2):
            tmp = matrix[j+1][y2]
            if(tmp < min) : min = tmp
            matrix[j+1][y2] = mem
            mem = tmp
        for j in range(y2, y1, -1):
            tmp = matrix[x2][j-1]
            if(tmp < min) : min = tmp
            matrix[x2][j-1] = mem
            mem = tmp            
        for j in range(x2, x1, -1):
            tmp = matrix[j-1][y1]
            if(tmp < min) : min = tmp
            matrix[j-1][y1] = mem
            mem = tmp
            
        answer.append(min)
        
    return answer

if __name__ == "__main__":
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))