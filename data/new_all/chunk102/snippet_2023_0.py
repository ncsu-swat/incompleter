def Rearrange(arr):
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0]
if __name__ == '__main__':
    print(Rearrange(arr))