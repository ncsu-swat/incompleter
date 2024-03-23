class geeks:
    counter = 0

    def __init__(self):
        geeks.counter += 1
g1 = geeks()
g2 = geeks()
print(geeks.counter)