def solution(s):
    a = sorted(s)
    a.sort(reverse=True)

    return ''.join(a)