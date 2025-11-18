def solution(citations):
    citations.sort(reverse=True)
    
    for index,c in enumerate(citations):
        if c < index + 1:
            return index
                        
    return len(citations)