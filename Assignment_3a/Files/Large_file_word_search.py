
lines = None

line_nos = []

with open("document.txt", 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].lower()

keyword = input("Enter Keyword:")

for i in range(0, len(lines)):
    if keyword in lines[i].split():
        line_nos.append(i+1)

print("Keyword appearing lines:")
print(line_nos)

