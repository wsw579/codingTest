def solution(quiz):
    answer = []
    
    for q in quiz:
        expression, res = q.split("=")
        if eval(expression.strip()) == int(res.strip()):
            answer.append("O")
        else:
            answer.append("X")
    return answer