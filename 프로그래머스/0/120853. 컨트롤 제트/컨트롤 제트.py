def solution(s):
    answer = []
    tokens = s.strip().split()
    
    for token in tokens:
        if token == "Z":
            if answer:
                answer.pop()
        else:
            answer.append(int(token))
        
    return sum(answer)