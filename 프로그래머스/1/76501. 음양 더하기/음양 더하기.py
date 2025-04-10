def solution(absolutes, signs):
    answer = 0
    for i, num in enumerate(absolutes) :
            if signs[i] == True:
                answer += num
            else :
                answer -= num
    return answer