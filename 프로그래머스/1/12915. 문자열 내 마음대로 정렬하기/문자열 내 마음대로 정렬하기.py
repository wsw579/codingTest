def solution(strings, n):
    answer = []
    
    answer = sorted(strings, key=lambda s: (s[n], s))

    return answer