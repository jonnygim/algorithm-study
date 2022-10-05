# 이코테 - 그리디
# 01. 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)



