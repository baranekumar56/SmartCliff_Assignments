
import re

s = input()

hashtags = re.findall(r"(#\w+)", s)
mentions = re.findall(r"(@\w+)", s)
print(hashtags)
print(mentions)