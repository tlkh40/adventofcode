import copy

AROUND_DIGIT = [
    # above
    (0,-1),
    # below
    (0,1),
    # above
    (-1,0),
    # below
    (1,0),
    # diag up right
    (1,1),
    # diag down right
    (1,-1),
    # diag up left
    (-1,1),
    # diag down left
    (-1,-1)
]

f = open('input.txt', mode="r")

matrix = f.readlines()

char = 0
sum = 0
sum2 = 0
maybe_gear = {}

for line_index, line in enumerate(matrix):
    while True:
        if len(line) == char:
            char = 0
            break
        if line[char].isdigit():
            start = copy.copy(char)
            num = ""

            # read whole number
            while True:
                if char == len(line):
                    char = char - 1
                    break
                if not line[char].isdigit():
                    break
                num += line[char]
                char += 1

            # Check if digit should be added
            counted = False
            for digit in range(start, char):
                for direction in AROUND_DIGIT:
                    x = direction[0]
                    y = direction[1]
                    pos_x = digit + x
                    pos_y = line_index + y
                    if (
                        pos_y >= 0 and len(matrix) - 1 - pos_y >= 0
                        and pos_x >= 0 and len(matrix[pos_y]) - 1 - pos_x >= 0
                    ):
                        c = matrix[pos_y][pos_x]
                        if not c.isdigit() and c != ".":
                            counted = True

                            # Check if it's a gear (pt2)
                            if c == "*":
                                coords = (pos_x, pos_y)
                                cord_hash = f"{line_index}_{start}_{char}"
                                if maybe_gear.get(coords) is None:
                                    maybe_gear[coords] = { 
                                        "hash": cord_hash,
                                        "val": int(num),
                                        "added": False
                                    }
                                else:
                                    if (
                                        maybe_gear[coords]["hash"] != cord_hash
                                        and not maybe_gear[coords]["added"]
                                    ):
                                        maybe_gear[coords]["added"] = True
                                        sum2 += maybe_gear[coords]["val"] * int(num)
                                        
                            break
            if counted:
                sum += int(num)
        char += 1
        
print(f"sum: {sum} sum2: {sum2}")