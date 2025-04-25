def solution(X, Y):
    answer = ''
    for char in set(X):
        num = min(X.count(char) , Y.count(char))
            
        answer += (char * num)
    
    if not answer:
        return '-1'    
    
    answer =  ''.join(sorted(answer,reverse=True))

    if answer[0] == '0':
        return '0'
    
    return answer 