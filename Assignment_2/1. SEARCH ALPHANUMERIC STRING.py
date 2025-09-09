
sentence = input().split(" ")

# for this problem we split the input string by spaces , then
# for each word in the sentence we check whether it have a number and a letter in it

for word in sentence:
    contains_number = False
    contains_letter = False
    contains_symbol = False

    for i in word:
        if i.isdigit():
            contains_number = True
        elif i.isalpha():
            contains_letter = True
        else:
            contains_symbol = True

    if not contains_symbol and contains_number and contains_letter:
        print(word)
