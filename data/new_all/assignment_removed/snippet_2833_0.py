def gnome_sort(alist):
    for pos in range(1, len(alist)):
        while pos != 0 and alist[pos] < alist[pos - 1]:
            (alist[pos], alist[pos - 1]) = (alist[pos - 1], alist[pos])
            pos = pos - 1
alist = input('Enter the list of numbers: ').split()
gnome_sort(alist)
print('Sorted list: ', end='')
print(alist)