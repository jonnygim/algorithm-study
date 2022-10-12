# s 한 개 이상의 단어로 구성된 문자열
# 각 단어는 하나 이상의 공백 문자
# 각 단어의 짝수번째 알파벳은 대문자로
# 홀수번째 알파벳은 소문자로 바꾼 문자열 리턴
#-- 공백 기준으로 인덱스를 확인해야 함 / 0은 짝수로 처리
def solution(s):
    answer = ""

    for word in s.split(" "):
        for idx, j in enumerate(word):
            if idx == 0 or idx % 2 == 0:
                answer += j.upper()
            else:
                answer += j.lower()
        answer += " "

    return answer[:-1]