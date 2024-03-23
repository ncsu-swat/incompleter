unflat_json = {'user': {'Rachel': {'UserID': 1717171717, 'Email': 'rachel1999@gmail.com', 'friends': ['John', 'Jeremy', 'Emily']}}}

def flatten_json(y):

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
print(flatten_json(unflat_json))