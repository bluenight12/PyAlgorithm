def solution(line):
    answer, lists = [], []
    n = len(line)
    min_x = min_y = int(1e15)
    max_x = max_y = -int(1e15)
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1, n):
            c,d,f = line[j]
            if a*d == b*c: continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            #is_integer
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                lists.append([x,y])
            
                if x > max_x :
                    max_x = x
                if x < min_x :
                    min_x = x
                if y > max_y :
                    max_y = y
                if y < min_y :
                    min_y = y
            
        
    x_len = max_x - min_x + 1
    y_len = max_y - min_y + 1

    #Study list comprehension 
    coord = [['.'] * x_len for _ in range(y_len)]
    
    for star_x, star_y in lists:
        nx = star_x - min_x
        ny = max_y - star_y
        coord[ny][nx] = '*'
        
        
    return ["".join(result) for result in coord]