import sys
import math

def calc_dia(tri):
    ss = tri.split(' ')
    # print '-------------->', len(ss)
    # a, b, c = tri.split(' ')[:2]
    a = int(ss[0])
    b = int(ss[1])
    c = int(ss[2])
    # print '===', a, b, c
    p = 0.5 * (a + b + c)
    d = (p - a) * (p - b) * (p - c)
    d = math.sqrt(d / p)
    return d

def calc(lines):
    total = int(lines[0])
    dias = {} # diameter to count
    for tri in lines[1:]:
        tri = tri.rstrip()
        d = calc_dia(tri)
        cnt = dias.get(d) or 0
        dias[d] = cnt + 1
    return max(dias.values())


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    # for s in lines:
    #     s = s.rstrip()
    print calc(lines)
