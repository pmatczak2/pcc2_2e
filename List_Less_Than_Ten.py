# Take a list, say for example this one:
# and write a program that prints out all the elements of the list that are less than 5.

b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 6:
        b.append(i)
print(b)

