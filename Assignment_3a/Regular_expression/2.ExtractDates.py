import re


def extract_dates(s):
    pat = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}\.\d{2}\.\d{2})\b'

    return re.findall(pat, s)

s = input()

print(extract_dates(s))