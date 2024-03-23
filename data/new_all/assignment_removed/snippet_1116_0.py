class dictObj(object):

    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'

    def do_nothing(self):
        pass
test = dictObj()
print(test.__dict__)