import regex as re
f = open("input.txt").read().strip().splitlines()
symbols = {(x, y) for x, line in enumerate(f) for y, e in enumerate(line) if not e.isdigit() and e != "."}
print(sum((part_number := int(m[0])) for x, line in enumerate(f) for m in re.finditer(r"\d+", line) if any((x + dx, y + dy) in symbols for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] for y in range(m.start(), m.end()))))



