
a = "abcdefghijklmnopqrstuvwxyz"
b = sorted(a, reverse=True)

mirror = {}

for i in range(0, 26):
    mirror[a[i]] = b[i]

k = int(input())

in_s = list(input())

for i in range(k-1, len(in_s)):
    in_s[i] = mirror[in_s[i]]

print("".join(in_s))

