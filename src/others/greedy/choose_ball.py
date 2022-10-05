n, m = map(int, input().split())
balls_w = list(map(int, input().split()))

array = [0] * 11

for x in balls_w:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)