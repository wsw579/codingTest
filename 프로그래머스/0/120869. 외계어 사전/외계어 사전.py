def solution(spell, dic):
    answer = 2
    s = set(spell)
    for d in dic:
        if s == set(d):
            answer = 1
    return answer