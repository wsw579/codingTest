def solution(dots):
    answer = 0
    x_value = [x for x,y in dots]
    y_value = [y for x,y in dots] 
    
    width = max(x_value) - min(x_value)
    weight = max(y_value) - min(y_value)
    
    return width*weight