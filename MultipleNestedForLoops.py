from itertools import product
import re

compiled_regex = re.compile("\[(\d)*\.\.(\d)*\]")

line = "hello[0..2][0..3].world[0..4]"

iterable = re.finditer(compiled_regex, line)

a = []
b = []

for el in list(iterable):
    a.append(range(int(el[1]), int(el[2]) + 1))
    b.append([el.start(), el.end()])


for pos in product(*a):
    dummy = line
    pos = pos[::-1]
    for idx, i in enumerate(b[::-1]):
        dummy = "{}[{}]{}".format(dummy[:i[0]], pos[idx], dummy[i[1]:])
    print(dummy)
