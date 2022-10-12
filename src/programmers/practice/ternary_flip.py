# 자연수 n
# 3진법 상에서 앞뒤로 뒤집고 다시 10진법으로 바꿔서 리턴
def solution(n):
    answer = 0
    a = ""
    while n:
        a += f'{n % 3}'
        n = n // 3

    for idx, i in enumerate(a[::-1]):
        i = int(i)
        answer += 3 ** idx * i

    return answer


solution(45)
