l = open("input.txt", "r").readlines()

def exclude_whitespace(o):
    return list(filter(lambda a : a != '', o))

copies = {}
sum = 0

for idx, line in enumerate(l):
    parts = line.replace("Card ", "").split(":")
    game = parts[0]
    numbers = parts[1].strip().split("|")
    winning = exclude_whitespace(numbers[0].split(" "))
    hand = exclude_whitespace(numbers[1].split(" "))

    counter = 0
    for n in winning:
        if n in hand:
            counter += 1

    sum += 0 if counter == 0 else 2 ** (counter - 1)

    if copies.get(idx) is None:
        copies[idx] = 1

    for i in range(counter):
        how_many = copies.get(idx, 1)
        val = copies.get(idx + i + 1)
        if val is None:
            copies[idx + i + 1] = how_many + 1
        else:
            copies[idx + i + 1] = how_many + val

sum2 = 0

for k in copies.keys():
    sum2 += copies[k]

print(f"1:{sum} 2:{sum2}")