import re

def get_words_that_start_and_end_with_same_letter(s):

    pat = r'\b(?i)([a-z])\w*\1\b'

    return re.findall(pat, s, flags=re.IGNORECASE)

s = input()
print(get_words_that_start_and_end_with_same_letter(s))