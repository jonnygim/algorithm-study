# 0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들
#수 있는 큰 수
def solution(numbers):
    answer = ''
    sum_ = 0
    tmp = []
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse=True)

    for (c, length) in tmp:
        sum_ += int(c)

        if sum_ == 0:
            return '0'
        answer += c[:length]

    return answer

# solution2([3, 30, 34, 32, 5, 9])
solution2([3, 30, 34, 5, 9])
# solution2([34, 3444, 32, 3222])
# 하면 344434323222