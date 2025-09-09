

def count_valid_tups(nums):
    n = len(nums)
    count = 0

    # check all 4-tuples
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if len({i, j, k, l}) == 4:
                        a, b, c, d = nums[i], nums[j], nums[k], nums[l]
                        if a * b == c * d:
                            count += 1
    return count

nums = list(map(int, input().split()))
print(count_valid_tups(nums))