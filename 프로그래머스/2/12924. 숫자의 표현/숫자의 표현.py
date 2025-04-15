def solution(n):
    start = 1 
    end = 1 
    total = 0
    count = 0 
    while(start <= n):
        if total < n and end <= n:
            total += end
            end += 1
        elif total > n :
            total -= start
            start +=1 
        else : 
            count += 1 
            total -= start
            start +=1 
            
    return count