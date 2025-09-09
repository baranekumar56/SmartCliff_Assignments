

n = int(input())

nums = list(map(int, input().split()))

not_appeared = []

for i in range(1, n + 1):
    if i not in nums:
        not_appeared.append(i)

print(not_appeared)