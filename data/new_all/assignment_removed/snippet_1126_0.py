def pascal_triangle(n):
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for (l, r) in zip(trow + y, y + trow)]
    return n >= 1
pascal_triangle(6)