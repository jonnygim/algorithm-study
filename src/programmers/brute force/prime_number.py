from itertools import permutations

def solution(numbers):
    answer = []
    nums = [i for i in numbers]

    a = []
    for i in range(1, len(nums) + 1):
        a += list(permutations(nums, i))
    new_nums = [int(("").join(j)) for j in a]

    for n in set(new_nums):
        if n < 2:
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):  # 제곱근
            if n % i == 0:
                check = False
                break

        if check:
            answer.append(n)

    return len(answer)