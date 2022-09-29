# 9까지 숫자 일부 정수 배열. 없는 수 찾아서 모두 더한 거 반환
def solution(numbers):
    cnt = 0

    for i in range(0, 10):
        if i in numbers:
            continue
        else:
            cnt += i

    return cnt
