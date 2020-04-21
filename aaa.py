import sys
import string


def isalpha(char):
    return char in string.ascii_letters


def check_a(s):
    distance = -1
    for i in range(len(s)):
        if isalpha(s[i]):
            if -1 < distance < 2:
                return 'unsafe'
            distance = 0
        elif ' ' == s[i]:
            distance += 1
    return 'safe'


if __name__ == '__main__':
    s = raw_input()
    #s = sys.stdin.readline()
    print check_a(s),
