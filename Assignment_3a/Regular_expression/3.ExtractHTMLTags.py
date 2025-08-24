import re


def extract_tags(html):

    pat = r'</?([a-zA-Z][a-zA-Z0-9]*)[^>]*>'

    return re.findall(pat, html)

s = input()
print(extract_tags(s))