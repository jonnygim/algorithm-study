# 놀이기구 이용료 price
# but N 번째 이용한다면 price 의 N배를 받기로 함
# 100, 200, 300
# count 번 타게 되면 가진 돈에서 얼마나 모자르나
# 부족하지 않으면 0
def solution(price, money, count):
    answer = -1

    for i in range(1, count + 1):
        money -= price * i

    if money < 0:
        answer = abs(money)
    elif money >= 0:
        answer = 0

    return answer