def solution(brown, yellow):
    h = (brown - 4) // 4
    
    while True:
        if yellow % h == 0:
            w = yellow // h
            if (h + 2) * (w + 2) == brown + yellow:
                break
        h += 1
    
    answer = [w + 2, h + 2]
    answer.sort(reverse = True)
    
    return answer
