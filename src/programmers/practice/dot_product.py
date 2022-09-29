def solution(a, b):
    s_num = 0

    for i in range(0, len(a)):
        s_num = s_num + a[i] * b[i]

    return s_num