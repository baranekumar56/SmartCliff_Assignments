
s = []

with open("input.txt", "r+") as f:
    buff = f.readline()

    while buff != "":
        s.append(buff.strip('\n')[::-1])
        buff = f.readline()

    f.close()

s = s[::-1]

with open("input.txt", "w") as f:
    for i in s:
        f.write(i + '\n')

    f.close()

print("File content have been reversed successfully")

