from collections import deque

def solution(numbers, target):
    answer = 0
    dq = deque([(0, 0)]) # sum, level
    while dq:
        print('dq -----', dq)
        s, l = dq.popleft()
        print(f'pop -- s: {s}, l: {l}')
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
            print('lever == len(numbers) and sum == target')
            print('ans : ', answer)
        dq.append((s+numbers[l-1], l+1)) # out of index 방지 [l-1]
        dq.append((s-numbers[l-1], l+1))

    print(answer)
    return answer


solution([4, 1, 2, 1], 2)