import sys
import math
import decimal

def is_elementary(tri):
    ss = tri.split(' ')
    # print '-------------->', len(ss)
    # a, b, c = tri.split(' ')[:2]
    a = decimal.Decimal(ss[0])
    b = decimal.Decimal(ss[1])
    c = decimal.Decimal(ss[2])
    # print '===', a, b, c
    x = ((c - b) / a)
    # return x == int(x)
    return x == x.quantize(decimal.Decimal('0'), rounding=decimal.ROUND_DOWN)

def calc(lines):
    total = int(lines[0])
    cnt = 0
    for tri in lines[1:]:
        tri = tri.rstrip()
        if is_elementary(tri):
            cnt += 1
    return str(cnt)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    # for s in lines:
    #     s = s.rstrip()
    print calc(lines)
