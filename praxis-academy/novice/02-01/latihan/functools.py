import functools

total = functools.reduce(lambda a, b: (0, a[1] + b[1]), items)[1]

def combine(a, b):
    return 0, a[1] + b[1]

total = functools.reduce(combine, items)[1]

total = 0
for a, b in items:
    total += b

total = sum(b for a, b in items)