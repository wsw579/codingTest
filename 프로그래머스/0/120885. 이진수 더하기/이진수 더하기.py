def solution(bin1, bin2):
    sum_bin = int(bin1,2) + int(bin2,2)
    
    return bin(sum_bin)[2:]