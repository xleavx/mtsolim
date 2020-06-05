import sys

def isDivOn3(s):
    if s is None:
        return False
    s = str(s)
    if s == '':
        return False
    nn = [int(ch) for ch in s]
    sumNN = sum(nn)
    if sumNN > 100000:
        return isDivOn3(str(sumNN))
    return sumNN % 3 == 0

def checkNumber(s):
    #checkeds = []
    numbs = [s]
    while numbs:
        x = numbs.pop(0)
        # print 'check: ', x
        if isDivOn3(x):
            return x
        #checkeds.append(x)
        lx = len(x)
        if lx > 1:
            removedChars = []
            for i in range(lx):
                remCh = x[lx-i-1]
                if remCh in removedChars:
                    continue
                removedChars.append(remCh)
                #
                subx = x[:lx-i-1] + x[lx - i:]
                if subx.startswith('0'):
                    subx = subx.lstrip('0')
                    if subx == '':
                        subx = '0'
                if subx != '' and subx not in numbs:# and subx not in checkeds:
                    numbs.append(subx)
    return '-1'

    #
    # if :
    #     return s
    # ls = len(s)
    # if ls > 1:
    #     for i in range(ls):
    #         subNumber = s[:ls-i-1] + s[ls - i:]
    #         if checkNumber(subNumber):
    #             return subNumber
    # return '-1'

def calc(line):
    n = line.rstrip()
    nn = list(n)
    nn.sort(reverse=True)
    curr_n = ''.join(nn)
    return checkNumber(curr_n)
    # while len(curr_n) > 0:
    #     if isDivOn3(curr_n):
    #         return curr_n
    #     curr_n = curr_n[:-1]
    #
    # return '-1'

if __name__ == '__main__':
    line = sys.stdin.readline()
    print calc(line)
