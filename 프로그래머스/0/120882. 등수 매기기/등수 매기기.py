from statistics import mean
def solution(score):
    answer = []
    averages = []
    for s in score :
        averages.append(mean(s))
        
    sorted_avg = sorted(averages, reverse=True)
    for a in averages:
        answer.append(sorted_avg.index(a)+1)
    return answer