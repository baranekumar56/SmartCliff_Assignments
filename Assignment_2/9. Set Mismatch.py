from collections import Counter

n = int(input())

nums = list(map(int, input().split()))

res = []

for i in nums:
    if nums.count(i) > 1:
        res.append(i)
        break

for i in range(1, n + 1):
    if i not in nums:
        res.append(i)
        break

print(res)
