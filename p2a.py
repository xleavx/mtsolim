import sys
import string


def isalpha(char):
    return char in string.ascii_letters


def calc(string):
    number = int(string)
    if number % 2 != 0:
        return string
    nn = [number + 1, number - 1]
    minLength = None
    minValue = None
    for n in nn:
        l = len(str(n))
        if minLength is None or l < minLength:
            minLength = l
            minValue = n
        elif l == minLength and n < minValue:
            minValue = n
    return str(minValue)


if __name__ == '__main__':
    s = raw_input()
    print calc(s),
