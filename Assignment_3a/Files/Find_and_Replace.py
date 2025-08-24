

def find_and_replace(file_name, old_text, new_text):
    s = ""
    with open(file_name, 'r+') as f:
        s = f.read()
    f.close()

    res = ""

    # we can use a sliding windows based technique in which we select a window of old string size
    # check it with old text, if it matches, then we would replace it with the new text

    buff = ""
    sl = len(s)

    i = 0

    while i < sl and i < len(old_text):
        buff += old_text[i]
        i += 1

    if old_text == buff:
        #replace it with new string
        #for this the starting point would be 0th index

        res = new_text
        buff = ""
    else :
        res = s[0]

    # from this we can move our window

    while i < sl :

        ns = buff[1:] + s[i]

        i += 1

