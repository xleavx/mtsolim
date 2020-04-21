import sys
import string

def is_digit(char):
    return char in string.digits

def cmp_digits(dig1, dig2):
    if dig1 == dig2:
        return 0
    elif dig1 == '':
        return -1
    elif dig2 == '':
        return 1
    n1 = int(dig1)
    n2 = int(dig2)
    if n1 == n2:
        return -1 * cmp(len(dig1), len(dig2))
    else:
        return cmp(n1, n2)

def next_item(s, i):
    # char or digits
    digs = ''
    if i >= len(s):
        return ''

    while i < len(s):
        char = s[i]
        if not is_digit(char) :
            return digs == '' and char or digs
        else:
            digs = digs + char
    return digs


def cmp_func_internal(s1, s2):
    result = 0
    i1 = i2 = 0
    len1 = len(s1)
    len2 = len(s2)
    while i1 < len1 and i2 < len2:
        item1 = next_item(s1, i1)
        item2 = next_item(s2, i2)
        result = cmp_items(item1, item2)
        if result <> 0:
            return result
        i1 = i1 + len(item1)
        i2 = i2 + len(item2)
    return result

def cmp_func(s1, s2):
    result = cmp_func_internal(s1, s2)
    print 'cmp %d:%s - %s' % (result, s1, s2,)

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    # for s in lines:
    #     s = s.rstrip()
    lines = [s.rstrip() for s in lines[1:]]
    lines.sort(cmp_func)
    for line in lines:
        print line
