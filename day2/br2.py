import re
aaaa = re.compile(r"(\d+ \w+)+")

gr = {"red": 12, "green": 13, "blue": 14}

def parse_line(s: str):
    id = int(s.strip().removeprefix("Game ").split(":")[0])
    m = aaaa.findall(s)
    t = {}
    for group in m:
        l = group.split(" ")
        qty = int(l[0])
        color = l[1]
        highest = t.get(color) 
        if highest is None:
            t[color] = qty
            continue
        if highest < qty:
            t[color] = qty
    result = 1
    for k in t.keys():
        result = result * t[k]
    return result

c = 0

for line in open("input.txt", "r"):
    c += parse_line(line)
print(c)