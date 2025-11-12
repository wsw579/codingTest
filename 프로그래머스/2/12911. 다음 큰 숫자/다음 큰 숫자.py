def solution(n):
    n_count = bin(n).count('1')
    check_num = n + 1
    
    while True:
        check_num_one_count = bin(check_num).count('1')
        
        if check_num_one_count == n_count:
            return check_num
        
        check_num += 1

