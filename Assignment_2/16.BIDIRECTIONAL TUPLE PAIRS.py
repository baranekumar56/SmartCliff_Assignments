
s = input().split(" ")

tlist = []

for j in range(0, len(s), 2):

    tlist.append((int(s[j]), int(s[j+1])))

count = 0

for i in tlist:
    count += tlist.count((i[1], i[0]))

print(count // 2)
