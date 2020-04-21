import sys
import string

def isrlud(char):
    return char in 'rlud'

def opposite(char):
    orig = 'rlud'
    oppo = 'lrdu'
    i = orig.index(char)
    return oppo[i]

def check_b1(s):
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if not isrlud(ch):
            return "No"
        oo = opposite(ch)
        if stack and stack[-1] == oo:
            stack.pop(-1)
        else:
            stack.append(ch)
    return len(stack) == 0 and "Yes" or "No"

def check_b(s):
    ud = 0
    lr = 0
    for ch in s:
        if not isrlud(ch):
            return "No"
        ud += (ch == 'd' and 1) or (ch == 'u' and -1) or 0
        lr += (ch == 'r' and 1) or (ch == 'l' and -1) or 0
    return (ud == lr == 0) and "Yes" or "No"


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    for s in lines:
        #s = sys.stdin.readline()
        s = s.rstrip()
        print check_b1(s)
