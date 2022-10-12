def solution(d, budget):
    answer = 0
    a = 0
    d.sort()

    for i in range(len(d)):
        if a + d[i] <= budget:
            a += d[i]
            answer += 1

    return answer