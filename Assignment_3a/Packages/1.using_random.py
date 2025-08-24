
import random

rand_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#@$%^&*()"

def get_random_password(length):

    password = ""

    for i in range(0, length):
        password += rand_str[random.randint(0, len(rand_str)-1)]

    return password

print(get_random_password(8))