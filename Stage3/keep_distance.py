# 프로그래머스 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

def solution(places):
    answer = []
    # 본인의 위쪽과 왼쪽은 확인을 하지 않아도 됨 (왼쪽위부터 하나씩 차례대로 할시)
    # 왼쪽 밑은 해줘야함
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dx2 = [1, 1, -1, -1]
    dy2 = [-1, 1, 1, -1]
    for place in places:
        result = 1
        #enumerate를 이용하면 list 안의 값과 index를 동시에 얻을 수 있다
        # for idx_row, row in enumerate(place):
        #   for idx_col, cell in enumerate(row):
        for y in range(0, 5):
            if result == 0 : break
            for x in range(0, 5):
                if result == 0 : break
                if place[y][x] != 'P': continue
                #다른 함수로 불러와서 조건에 부합했을 때 return을 하는게 훨씬 효율적이다
                for n in range(0, 4):
                    if not (0 <= x + dx[n] < 5 and 0 <=y + dy[n] <5): continue
                    if place[y+dy[n]][x+dx[n]] == 'P': result = 0
                for n in range(0, 4):
                    if not (0 <= x + dx[n]*2 < 5 and 0 <=y + dy[n]*2 <5): continue
                    if place[y+dy[n]*2][x+dx[n]*2] == 'P' and place[y+dy[n]][x+dx[n]] != 'X': result = 0
                for n in range(0, 4):
                    if not (0 <= x + dx2[n] < 5 and 0 <=y + dy2[n] <5): continue
                    if place[y+dy2[n]][x+dx2[n]] == 'P' and (place[y][x+dx2[n]] != 'X' or place[y+dy2[n]][x] != 'X'): result = 0
        answer.append(result)            
                    
            
                
        
    return answer


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))