def solution(n, lost, reserve):

    # 여분의 체육복을 가져온 학생이 체육복을 도난 당했을 수 있음
    new_lost = [i for i in lost if i not in reserve]
    new_reserve = [i for i in reserve if i not in lost]

    # 정렬이 되어 있을 것이란 보장이 없음 -> 정렬
    new_lost.sort()
    new_reserve.sort()

    # 빌린 사람 수
    cnt = 0

    for i in new_lost:
        if i - 1 in new_reserve:
            cnt += 1
            new_reserve.remove(i - 1)
        elif i + 1 in new_reserve:
            cnt +=1
            new_reserve.remove(i + 1)

    return n - len(new_lost) + cnt