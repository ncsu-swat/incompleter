def avgfun(*n):
    for t in n:
        sums = sums + t
    avg = sums / len(n)
    return avg
result1 = avgfun(1, 2, 3)
result2 = avgfun(2, 6, 4, 8)
print(round(result1, 2))
print(round(result2, 2))