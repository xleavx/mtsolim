import sys
import datetime

def isDateByMask(s, mask):
    try:
        byMask1 = datetime.datetime.strptime(s, mask)
        return True
    except:
        return False

def calc(s):
    s = s.rstrip()
    #nn = string.split()
    # result = 1 <= int(nn[0]) <= 12 and 1 <= int(nn[1]) <= 31
    # result = result and
    # return str(int( not result ))
    return str(int(isDateByMask(s, '%m %d %Y') != isDateByMask(s, '%d %m %Y')))


if __name__ == '__main__':
    line = sys.stdin.readline()
    print calc(line)
