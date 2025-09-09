
text = input().split()

print("Default Order:", "".join(text))
print("Positional order :{1} {2} {0}".format(text[0], text[1], text[2]))
print("Keyword : {2} {0} {1}".format(text[0], text[1], text[2]))