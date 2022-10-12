def solution(s, n):
    answer = ''
    tmp = 0

    for i in s:
        if i.isupper():
            if ord(i) + n >= 91:
                tmp = ord(i) + n - 91
                answer += chr(65 + tmp)
            else:
                answer += chr(ord(i) + n)
        elif i.islower():
            if ord(i) + n >= 123:
                tmp = ord(i) + n - 123
                answer += chr(97 + tmp)
            else:
                answer += chr(ord(i) + n)
        else:
            answer += i

    return answer