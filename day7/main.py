kaboom = open('input.txt').readlines()
part2 = True

# thx random person on reddit for making me realize j already exists in the array...
# https://paste.ofcode.org/68NuRaXeejw87nTB48WbUX
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] if not part2 else ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

order.reverse()
order = { a: i for i, a in enumerate(order) }
ranks = []

class Hand:
    def __init__(self, t, bid) -> None:
        self.t = t
        self.bid = bid
        pass

    def recursive(self, other, idx):
        if self.t[1][idx] == other.t[1][idx]:
            return self.recursive(other, idx+1)
        else:
            return order.get(self.t[1][idx]) < order.get(other.t[1][idx])

    def __lt__(self, other):
        if self.t[0] == other.t[0]:
            return self.recursive(other, 0)
        return self.t[0] < other.t[0]
    def __str__(self) -> str:
        return f"Hand({self.t} | {self.bid})"
    def __repr__(self) -> str:
        return self.__str__()

for hand in kaboom:
    cards, bid, *idc = hand.strip().split()
    m = {}
    
    for type in cards:
        if m.get(type) is None:
            m[type] = 1
        else:
            m[type] = m[type] + 1
    
    if part2 and 'J' in cards:
        from operator import itemgetter
        to = sorted([ (k, v) for k,v in m.items() ], key=itemgetter(1), reverse=True)
        cards_mod = cards.replace("J", to[0][0])
        if to[0][0] == 'J' and len(to) != 1:
            cards_mod = cards.replace("J", to[1][0])

        m={}
        for type in cards_mod:
            if m.get(type) is None:
                m[type] = 1
            else:
                m[type] = m[type] + 1

    t = 0

    for k in m.keys():
        if m[k] == 5:
            t = 6
            break
        if m[k] == 4:
            t = 5
            break
        if m[k] == 3 and len(m.keys()) == 2:
            t = 4
            break
        if m[k] == 3 and len(m.keys()) == 3:
            t = 3 
            break
        if m[k] == 2 and len(m.keys()) == 3:
            t = 2
            break
        if m[k] == 2 and len(m.keys()) == 4:
            t = 1
            break
    ranks.append(Hand((t, cards), int(bid)))
from functools import reduce

sorted_rank = [ (h, r+1) for r,h in enumerate(sorted(ranks)) ]
# print(sorted_rank)
e = reduce(lambda x,y : x + y[0].bid * y[1], sorted_rank, 0)
print(e)