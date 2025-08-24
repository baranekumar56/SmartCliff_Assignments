import re


def extract_phone_numbers(text):
    pat = r'\b(?:\+91-\d{10}|91\d{10}|[6-9]\d{9})\b'

    return re.findall(pat, text)

text = input()
print(extract_phone_numbers(text))
