def solution(a, b):
    answer = 0
    temp = 0
    if a > b :
        temp = a 
        a = b
        b = temp 
        
    for num in range(a,b+1):
        answer += num
        
    return answer