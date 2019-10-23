lala = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lala)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)