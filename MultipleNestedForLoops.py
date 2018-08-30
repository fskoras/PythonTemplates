from itertools import product
import re

compiled_regex = re.compile("\[(\d)*\.\.(\d)*\]")

line = "siema[0..2][0..3].ziom[0..4]"

iterable = re.finditer(compiled_regex, line)

a = []
b = []

for el in list(iterable)[::-1]:
    a.append(range(int(el[1]), int(el[2]) + 1))
    b.append([el.start(), el.end()])

for pos in product(*a):
    dummy = line
    for idx, i in enumerate(b):
        dummy = "{}[{}]{}".format(dummy[:i[0]], pos[idx], dummy[i[1]:])
    print(dummy)
