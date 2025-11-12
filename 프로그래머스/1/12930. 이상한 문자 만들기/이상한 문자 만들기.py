def solution(s): 
    temp = []
    temp += s.split(' ')
    answerTemp = []
    for wordList in temp:
        answer = ''
        for index,word in enumerate(wordList):
            if index % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
                
        answerTemp.append(answer)
                
    
    return " ".join(answerTemp)