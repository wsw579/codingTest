def solution(sides):
    answer = 0
    # max(sides)가 가장 긴 변 
    for num in range(max(sides) - min(sides)+1, max(sides)+1):
        answer += 1 
        
    #나머지 한 변이 제일 긴 변 
    for num in range(max(sides)+1, sum(sides)):
        answer +=1 
            
    return answer