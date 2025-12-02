def solution(s):
    answer = ""
    number_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    }
    
    start_index = 0 
    
    for end_index in range(len(s)):
        if s[end_index].isdigit():
            answer += str(s[end_index])
            start_index = end_index+1
            
        if s[start_index:end_index+1] in number_map:
            answer += str(number_map.get(s[start_index:end_index+1]))
            start_index = end_index+1
        
         
    
    return int(answer)