
lines = {}

with open('dat_files/data.txt', 'r+') as f:

    buff = f.readline()

    while buff != "":
        t = buff.strip('\n').lower()
        if t not in lines:
            lines[t] = buff

        buff = f.readline()

f.close()

with open('dat_files/cleaned.txt', 'w') as f:

    for line in lines.values():
        f.write(line)


