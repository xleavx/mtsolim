import sys

def calc(lines):
    nConstellation = int(lines[0].split()[0])
    nStars         = int(lines[0].split()[1])
    starsInConstellation = [int(sn) for sn in lines[1].split()]
    nTotal = sum(starsInConstellation)
    return str(cmp(nTotal, nStars))

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    print calc(lines)
