def solution(n):
    sort_n = sorted(str(n),reverse=True)
    return int("".join(sort_n))