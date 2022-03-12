a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = {}
for key in a:
    if c.get(key, 0) == 0:
        c[key] = 1
    else:
        c[key] += 1
for key in b:
    if c.get(key, 0) == 0:
        c[key] = 1
    else:
        c[key] += 1
print([k for k, v in c.items() if v > 1])