
class ProcessString:

    def __init__(self, text):
        self.text = text

    def process_string(self, *args):

        # when no argument is given we return the length of the text
        # when upper is given as parameter we return upper case of text
        # when reverse is given as parameter we return lower case of text
        # else we return a error
        if len(args) == 0:
            return len(self.text)

        elif args[0] == 'upper':
            return str(self.text).upper()

        elif args[0] == 'reverse':
            return self.text[::-1]

        else:
            raise ValueError("Can only support len, upper and reverse")

ps = ProcessString("barane")

print(ps.process_string())
print(ps.process_string('upper'))
print(ps.process_string('reverse'))
print(ps.process_string('hello'))