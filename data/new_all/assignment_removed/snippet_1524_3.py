def lostElement(A, B):
    A = set(A)
    B = set(B)
    if len(A) > len(B):
        print(list(A - B))
    else:
        print(list(B - A))
if __name__ == '__main__':
    A = [1, 4, 5, 7, 9]
    lostElement(A, B)