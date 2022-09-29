def solution(absolutes, signs):
    answer = 123456789
    a = []

    for i in range(len(signs)):
        if signs[i]:
            a.append(absolutes[i])
        else:
            a.append(-absolutes[i])

    print(sum(a))

    return answer