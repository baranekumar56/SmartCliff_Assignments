
lines = []

with open('dat_files/bigfile.txt', 'r') as f:
    lines = f.readlines()

f.close()

N = int(input())

part_no = 1

for i in range(0, len(lines), N):
    l = lines[i:i + N]
    with open('part_{}.txt'.format(part_no), 'w') as f:
        f.writelines(l)
    f.close()
    part_no += 1

print("Big File content has been chunked into smaller sizes")