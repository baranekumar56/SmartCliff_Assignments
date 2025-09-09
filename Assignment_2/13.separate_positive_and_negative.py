
nums = list(map(int, input().split()))

positive_nums = []
negative_nums = []

for i in nums:
    if i <= 0:
        negative_nums.append(i)
    else:
        positive_nums.append(i)

print("Original list:", nums)
print("Positive list:", positive_nums)
print("Negative list:", negative_nums)