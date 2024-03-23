def split_string(string):
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string
if __name__ == '__main__':
    string = 'Geeks for Geeks'
    list_string = split_string(string)
    print(list_string)
    new_string = join_string(list_string)
    print(new_string)