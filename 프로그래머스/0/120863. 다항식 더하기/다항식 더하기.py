def solution(polynomial):
    answer = 0
    num = 0
    poly = polynomial.split('+')
    for p in poly:
        p = p.strip() 
        if 'x' in p:
            if p == 'x':
                answer += 1
            else:
                answer += int(p.replace('x', ''))
        else:
            num += int(p)
            
    if answer and num:
        return f"{answer}x + {num}" if answer != 1 else f"x + {num}"
    elif answer:
        return f"{answer}x" if answer != 1 else "x"
    else:
        return str(num)