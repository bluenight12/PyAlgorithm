def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for idx_row, row in enumerate(arr1):
        value = 0
        for mul in range(len(arr2[0])):
            for idx_col, col in enumerate(row):
                value += col * arr2[idx_col][mul]
            answer[idx_row].append(value)
            value = 0

    return answer


if __name__ == '__main__':
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [3, 3]]
    print(solution(arr1, arr2))
