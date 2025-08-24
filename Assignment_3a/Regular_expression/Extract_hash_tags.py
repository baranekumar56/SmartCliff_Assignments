
import re

s = input()

res = re.findall("(#[A-Za-z0-9].*)|(@[A-Za-z0-9].*)", s)
print(res)