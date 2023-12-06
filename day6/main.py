# funny dumb
input = """Time:        57     72     69     92
Distance:   291   1172   1176   2026""".strip().splitlines()
input = list(map(lambda s : s.split(":")[1].split(), input))
input = list(map(lambda a : list(map(int,a)), input))

sum = []

for i in range(len(input[0])):
    t = input[0][i]
    d = input[1][i]
    print(t,d)
    m = 0
    for i in range(t):
        if i * (t-i) > d:
            m = i
            break
    for i in range(m,t):
        print(f"{(i, t-i)} -> {i * (t-i)}")
        if i * (t-i) <= d:
            m = i-m
            break

    sum.append(m)

from functools import reduce

print(sum)
print(reduce(lambda x, y: x*y, sum))