
n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

element_to_check = int(input())

try:
    nums.index(element_to_check)
    print("True")
except ValueError:
    print("False")
