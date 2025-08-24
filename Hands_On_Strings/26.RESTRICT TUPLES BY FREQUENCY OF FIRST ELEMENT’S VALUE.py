from numba.cpython.new_tupleobj import tuple_eq

#lets consider the input tuple is given in a space separated manner

k = int(input())

list_of_tuples = []

tuples = input().split(" ")

for i in range(0, len(tuples), 2):
    list_of_tuples.append((tuples[i], tuples[i+1]))

freq = {}

res = []

for i in list_of_tuples:
    if i[0] in freq:
        if freq[i[0]] < k:

            res.append(i)
            freq[i[0]] += 1
    else :
        res.append(i)
        freq[i[0]] = 1

print(res)