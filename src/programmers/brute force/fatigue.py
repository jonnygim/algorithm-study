from itertools import permutations

def solution(k, dungeons):
    # 통과한 던전 수
    clear = 0
    # 현재 피로도
    now = k
    # 클리어 수 리스트
    a = []

    for i in permutations(dungeons, len(dungeons)):
        for fatigue in i:
            if fatigue[0] <= now:
                now -= fatigue[1]
                clear += 1
            else:
                break
        now = k # 피로도 리셋
        a.append(clear)  # 통과한 던전 수 리스트에 넣기
        clear = 0  # 통과한 던전 수 리셋

    return max(a)