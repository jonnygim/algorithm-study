def solution(x):
    answer = True
    a = []
    num = x
    s_num = 0

    while num > 0:
        if num // 10000 != 0:
            a.append(num // 10000)
            num = num % 10000
        elif num // 1000 != 0:
            a.append(num // 1000)
            num = num % 1000
        elif num // 100 != 0:
            a.append(num // 100)
            num = num % 100
        elif num // 10 != 0:
            a.append(num // 10)
            num = num % 10
        else:
            a.append(num)
            break

    for i in a:
        s_num += i

    if x % s_num != 0:
        answer = False

    return answer