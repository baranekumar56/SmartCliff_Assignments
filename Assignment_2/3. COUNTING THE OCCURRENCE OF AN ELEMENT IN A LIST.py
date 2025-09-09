
N = int(input())
element_to_count = input()

elements = []

for i in range(N):
    elements.append(input())

count = 0

for i in elements:
    if i == element_to_count:
        count += 1

print(count)


