def main(num):
    a = 0
    b = 1

    if num == a:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, num):
        x = a
        y = b
        c = a + b
        a = b
        b = c
        print(c)
        x, y = y, x + y
        assert (x, y) == (a, b)
main(10)
