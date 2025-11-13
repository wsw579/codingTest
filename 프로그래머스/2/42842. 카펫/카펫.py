def solution(brown, yellow):
    answer = []
    y_w, y_h = 0,0 
    
    # 제곱근까지 
    n = int((yellow)**0.5)
    for y_h in range (1,n+1):
        if yellow % y_h == 0: 
            y_w = yellow // y_h
            W,H = y_w+2, y_h+2
            if brown == (y_w + 2) * (y_h + 2) - yellow:
                answer+= [W,H]
            
    return answer