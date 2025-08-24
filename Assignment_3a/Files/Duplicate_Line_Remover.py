
lines = {}

with open('data.txt', 'r+') as f:

    buff = f.readline()

    while buff != "":
        t = buff.strip('\n').lower()
        if t not in lines:
            lines[t] = buff

        buff = f.readline()

f.close()

with open('cleaned.txt', 'w') as f:

    for line in lines.values():
        f.write(line)


