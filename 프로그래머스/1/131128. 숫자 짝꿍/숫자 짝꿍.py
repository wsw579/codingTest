from collections import Counter

def solution(X, Y):
    common = Counter(X) & Counter(Y)
    
    if not common:
        return '-1'

    answer = sorted(common.elements(), reverse=True)

    if answer[0] == '0':
        return '0'

    return ''.join(answer)
