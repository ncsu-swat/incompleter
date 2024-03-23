class geeks:
    counter = 0

    def __init__(self):
        geeks.counter += 1
g2 = geeks()
g3 = geeks()
print(geeks.counter)