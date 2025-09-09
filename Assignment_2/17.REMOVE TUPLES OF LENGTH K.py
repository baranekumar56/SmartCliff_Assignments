
# for this problem, lets consider the user provides , no of tuples
# and on each input line they specify the tuples

n = int(input())

tuples = []

for i in range(n):
    tuples.append(tuple(map(int, input().split())))


#length of the tuple to be removed

k = int(input())

res = []

for j in tuples:

    if len(j) != k:
        res.append(j)

print(res)