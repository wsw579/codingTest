def solution(s):
    answer = True
    s = s.lower()
    if s.count('p') == s.count('y'):
        return answer
    elif s.count('p') != s.count('y'):
        return False
    else :
        return answer