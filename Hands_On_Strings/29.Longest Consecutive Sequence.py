
n = int(input())

nums = list(map(int, input().split()))

nums.sort()

max_len = 0
curr_len = 0

for i in range(n):
    for j in range(i, n):
        if j + 1 < n and nums[j] + 1 == nums[j + 1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
            break

print(max_len + 1)