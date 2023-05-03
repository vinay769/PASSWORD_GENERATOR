import random
import string


def pass_gen(letter=True, number=True, symbol=True):

    letter = string.ascii_letters
    number = string.digits
    symbol = string.punctuation

    # print(letter,number,symbol)
    n = int(input("enter the number of password : "))
    for i in range(n):

        x = random.choice(letter)
        y = random.choice(number)
        z = random.choice(symbol)

        res = x+y+z
        print(res, end="")


pass_gen()
