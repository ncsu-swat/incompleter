def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))
li1 = [10, 15, 20, 25, 30, 35, 40]
print(Diff(li1, li2))