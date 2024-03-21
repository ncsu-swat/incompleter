from timeit import default_timer

def timer(n):
    for row in range(0, n):
        print(row)
    print(default_timer() - start)
timer(5)
timer(15)