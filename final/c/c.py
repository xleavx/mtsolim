import sys

def calc(string):
    NOMINALS = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    cards = []
    card = ''
    for i in range(len(string)):
        card += string[i]
        if card not in NOMINALS:
            continue
        cards.append(card)
        card = ''
    def cmpfunc(c1, c2, NOMINALS=NOMINALS):
        return cmp(NOMINALS.index(c1), NOMINALS.index(c2))
    cards.sort(cmpfunc)
    return ''.join(cards)

if __name__ == '__main__':
    line = sys.stdin.readline()
    print calc(line)
