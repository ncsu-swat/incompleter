class dictObj(object):

    def __init__(self):
        self.y = 'Yellow'
        self.z = 'Green'

    def do_nothing(self):
        pass
test = dictObj()
print(test.__dict__)