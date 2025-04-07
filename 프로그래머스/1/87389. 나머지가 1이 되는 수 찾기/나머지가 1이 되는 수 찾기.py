def solution(n):
    answer = 0
    for num in range(1,n+1):
        if n % num == 1:
            if answer != 0:
                if answer > num:
                    answer = num
            else :
                answer = num
            
    return answer