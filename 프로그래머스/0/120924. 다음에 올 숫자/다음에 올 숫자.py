def solution(common):
    answer = 0
    for i in range(1,len(common)-1):
        if (common[i] - common[i-1]) == (common[i+1] - common[i]):
            n = common[i] - common[i-1]
            answer = common[len(common)-1] + n
        else:
            n = common[i] // common[i-1]
            answer = common[len(common)-1] * n
    return answer