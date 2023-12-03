import re
aaaa = re.compile(r"(\d+ \w+)+")

gr = {"red": 12, "green": 13, "blue": 14}

def parse_line(s: str):
    id = int(s.strip().removeprefix("Game ").split(":")[0])
    m = aaaa.findall(s)
    for group in m:
        l = group.split(" ")
        qty = int(l[0])
        color = l[1]
        if gr.get(color) < qty:
            print(f"not possible id:{id} color:{color} qty:{qty}")
            id = 0
            break
    return id

c = 0

for line in open("input.txt", "r"):
    c += parse_line(line)
print(c)