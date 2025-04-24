def solution(array, n):
    minNum = [100,0] 
    for num in array:
        temp = abs(n - num) 
        if minNum[0] > temp or (temp == minNum[0] and num < minNum[1]):
            minNum[0] = temp
            minNum[1] = num
            
    return minNum[1]