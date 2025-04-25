from collections import Counter

def solution(X, Y):
    counter_X = Counter(X)
    counter_Y = Counter(Y)
    
    answer = []
    
    for digit in counter_X:
        if digit in counter_Y: 
            count = min(counter_X[digit] , counter_Y[digit])
            answer.extend(count * digit)
            
    if not answer:
        return '-1'
    
    if answer[0] == '0':
        return '0'
    
    answer.sort(reverse=True)
    
    return ''.join(answer)