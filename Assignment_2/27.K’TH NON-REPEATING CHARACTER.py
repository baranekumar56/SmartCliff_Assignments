

s = input()

k = int(input())

dict = {}

for i in range(0, len(s)):
    if s[i] in dict:
        dict[s[i]] = -1
    else:
        dict[s[i]] = i

l = []

for i in dict:
    if dict[i] != -1:
        l.append([i, dict[i]])

sorted(l, key=lambda x: x[1])

if len(l) < k:
    print("Not enough k non repeating values")
else:
    print(l[k-1][0])