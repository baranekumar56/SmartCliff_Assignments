from collections import Counter

s = input()

n_words = int(input())

words = []

for i in range(n_words):
    words.append(input())

word_len = len(words[0])

# each word in the words list is of same size and the given input string's lenght is a multiple of the word len
# so we split the input string into size of word len slices and then manually brute force search the list
# to find the appearance of words

appearances = []

s_slices = []

for i in range(0, len(s), word_len):
    s_slices.append(s[i:i + word_len])

word_set = Counter(words)

for i in range(0, len(s_slices) - word_len + 1):

    # check for the length of the total words given
    l = Counter(s_slices[i:i + n_words])

    found = True

    for j in word_set.keys():
        if l[j] != word_set[j]:
            found = False
            break
    if found:
        appearances.append(i*word_len)

print(appearances)