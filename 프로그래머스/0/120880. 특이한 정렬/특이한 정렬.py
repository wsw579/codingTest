def solution(numlist, n):
    answer = []
    temp = []
    for num in numlist:
        distance = abs(n - num)
        temp.append((distance, num)) 

    temp.sort(key=lambda x : (x[0],-x[1]))
    
    for t in temp:
        answer.append(t[1])
        
    return answer