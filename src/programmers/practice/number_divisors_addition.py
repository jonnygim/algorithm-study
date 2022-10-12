# 두 정수 left, right
# left ~ right 중
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀
# answer
def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
        cnt = 0

    return answer