def solution(n, words):
    used = set()
    used.add(words[0])
    for i in range(1,len(words)):
        current_word = words[i]
        pre_word = words[i-1]
        if current_word[0] != pre_word[-1] or current_word in used :
            return [(i % n) + 1 , (i//n) + 1]
        elif current_word[0] == pre_word[-1] and current_word not in used :
            used.add(current_word)
            
    return [0,0]