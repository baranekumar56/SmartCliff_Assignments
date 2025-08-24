
from num2words import num2words

def num_to_word(n):
    return num2words(n)

n = int(input())

print(num_to_word(n))