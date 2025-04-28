def solution(n):
    answer = ''
    num = n//2 +1
    for _ in range(num):
        answer += '수박'
        
    return answer[:n]