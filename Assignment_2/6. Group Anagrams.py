
n = int(input())

groups = {}

for i in range(1, n + 1):
    w = input()
    h = tuple(sorted(w))

    if h in groups:
        groups[h].append(w)
    else:
        groups[h] = [w]

for k, v in groups.items():
    print(v)