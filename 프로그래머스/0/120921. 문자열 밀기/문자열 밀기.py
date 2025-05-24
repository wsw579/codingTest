def solution(A, B):
    answer = 0
    
    while(answer < len(A)):
        if A == B:
            return answer 
        else:
            A = A[-1] + A[:-1]
            answer +=1 
    
    if A != B:
        answer = -1
    return answer