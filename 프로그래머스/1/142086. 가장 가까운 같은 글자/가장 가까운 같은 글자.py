def solution(s):
    answer = []
    dict = {} # 가장 마지막 인덱스 
    
    for current_index, word in enumerate(s):
        if word not in dict:   # 인덱스가 등록안됨 
            answer.append(-1)  
        else:
            previous_index = dict[word]
            distance = current_index - previous_index
            answer.append(distance)
        
        dict[word] = current_index
    
    
    return answer