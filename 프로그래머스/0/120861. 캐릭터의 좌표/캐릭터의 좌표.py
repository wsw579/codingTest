def solution(keyinput, board):
    answer = [0,0]
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    for key in keyinput:
        if key == "left":
            if answer[0] > -x_limit:
                answer[0]-= 1 
        elif key == "right":
            if answer[0] < x_limit:
                answer[0]+= 1
        elif key == "up":
            if answer[1] < y_limit:
                answer[1]+= 1
        elif key == "down":
            if answer[1] > -y_limit:
                answer[1]-= 1
        
    return answer