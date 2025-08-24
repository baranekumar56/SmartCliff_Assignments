
s = input()

lower_case_letters = 0
upper_case_letters = 0
special_case_letters = 0

for i in s:
    if i.isupper():
        upper_case_letters += 1
    elif i.islower():
        lower_case_letters += 1
    else:
        special_case_letters += 1

print("Uppercase letters: ", upper_case_letters)
print("Lowercase letters: ", lower_case_letters)
print("Special case letters: ", special_case_letters)