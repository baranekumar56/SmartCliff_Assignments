
s1 = input()
s2 = input()

i = 0
j = len(s2) - 1

res = ""

while i < len(s1) and j >= 0:
    res += s1[i]
    res += s2[j]

    i += 1
    j -= 1

if i == len(s1):
    if j != 0:
        res += s2[0:j+1]
else:
    res += s1[i:]

print(res)