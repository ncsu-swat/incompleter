def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res
if __name__ == '__main__':
    test_list = [1, 3, 4, 6, 5, 1]
    item = 1
    print('The original list is : ' + str(test_list))
    print('The list after performing the remove operation is : ' + str(res))