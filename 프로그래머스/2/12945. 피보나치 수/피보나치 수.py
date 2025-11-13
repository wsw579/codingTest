def solution(n):    
    if n == 0:
        return 0
    if n == 1:
        return 1 
    
    a, b = 0,1
    for n in range(2,n+1):
        temp = (a + b) % 1234567 
        a = b
        b = temp 
    
    return b