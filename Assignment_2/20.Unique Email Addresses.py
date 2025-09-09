
n = int(input())

emails = []

for i in range(n):
    emails.append(input())

count_of_unique_emails = 0

names = {}

for email in emails:

    localname = email.split('@')[0]
    name = localname.split('+')[0]

    u_name = ""
    for i in name:
        if i != '.':
            u_name += i

    if u_name not in names:
        count_of_unique_emails += 1
        names[u_name] = 1
    else :
        names[u_name] += 1

print(count_of_unique_emails)

