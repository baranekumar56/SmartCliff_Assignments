
s1 = input().split(' ')
s2 = input().split(' ')

uncommon = []

for i in s1:
    if s1.count(i) == 1 and i not in s2:
        uncommon.append(i)

for i in s2:
    if s2.count(i) == 1 and i not in s1:
        uncommon.append(i)

print(uncommon)