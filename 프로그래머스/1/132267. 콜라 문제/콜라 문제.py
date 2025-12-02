def solution(a, b, n):
    answer = 0
    while n >= a:
        new_get = (n // a) * b
        answer += new_get
        n = new_get + (n % a) 
    
    
    return answer