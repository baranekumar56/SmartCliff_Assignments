
s = input()

#in this question we maintain two variables, namely small and big
# all the lower case letters that we encounter will be stored inside small and vice versa for big


small = ""
big = ""

for i in s:
    if i.isupper():
        big += i
    else:
        small += i

print(small + big)