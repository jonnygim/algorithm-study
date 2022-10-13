# 0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들
#수 있는 큰 수
def solution(numbers):
    answer = ''
    n = 0

    print(sorted(numbers, key=str, reverse=True))
    a = sorted(numbers, key=str, reverse=True)

    for i in range(0, len(a)):
        if len(str(a[-2])) == 2 and len(str(a[-1])) == 1:
            print(str(a[-2])[1])
            n = a[-2]
            a[-2] = a[-1]
            a[-1] = n

        answer += str(a[i])

    print(answer)
    return str(answer)


solution([3, 30, 34, 32, 5, 9])
solution([34, 3444, 32, 3222])
# 하면 344434323222