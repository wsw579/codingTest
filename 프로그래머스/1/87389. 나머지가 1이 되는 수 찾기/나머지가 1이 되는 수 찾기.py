def solution(n):
    for num in range(1,n+1):
        if n % num == 1:
            return num  # 1부터 시작하니까 굳이 추가조건 넣지 않아도 결과가 가장 작은 자연수 
        