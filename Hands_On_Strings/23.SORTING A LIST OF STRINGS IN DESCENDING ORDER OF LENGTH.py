
strings = input().split(' ')

dic = {}

# we store each string with their length and count in to dictionary
# then we sort that dictionary based on string length


for i in strings:
    if i in dic:
        dic[i][1] += 1
    else:
        dic[i] = (len(i), 1)

sorted_strings = []

for string, val in dic.items():

    if len(sorted_strings) == 0:
        sorted_strings.append((string, val[0], val[1]))

    else:
        j = len(sorted_strings) - 1

        while (j >= 0):

            if val[0] <= sorted_strings[j][1]:
                sorted_strings.insert(j+1, (string, val[0], val[1]))
                break

            j -= 1

        if j < 0:
            sorted_strings.insert(0, (string, val[0], val[1]))


res = []

for i in sorted_strings:
    for j in range(0, i[2]):
        res.append(i[0])

print(res)