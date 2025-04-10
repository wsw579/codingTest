def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    if answer not in numbers : 
        for char in numbers : 
            answer.remove(char)
    return sum(answer)