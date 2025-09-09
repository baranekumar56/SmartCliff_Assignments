from collections import Counter

def find_valid_words(dictionary, charset):
    char_count = Counter(charset)
    valid_words = []

    for word in dictionary:
        word_count = Counter(word)
        if all(word_count[c] <= char_count.get(c, 0) for c in word_count):
            valid_words.append(word)

    print(", ".join(valid_words))

strs = input().split()
charset = input().split()

find_valid_words(strs, charset)
