def solution(x):
    num = 0 
    o_x = x 
    while x > 0 :
        num += x % 10
        x //= 10
        
    if num > 0 and (o_x % num == 0) :
        return True
    
    return False 