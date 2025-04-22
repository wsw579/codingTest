def solution(arr):
    if len(arr) > 1 :
        minNum = min(arr)
        arr.remove(minNum)
        return arr
    else :
        return [-1]