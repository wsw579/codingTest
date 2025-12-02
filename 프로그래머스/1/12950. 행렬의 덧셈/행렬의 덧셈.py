def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        new_arr = []
        new_arr = [x+y for x,y in zip(a,b)]
        answer.append(new_arr)
        
    return answer