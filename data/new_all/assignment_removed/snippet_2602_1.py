class print1:

    def __init__(self):

    def get(self):
        self.string = input('Enter string: ')

    def put(self):
        print('String is:')
        print(self.string)
obj = print1()
obj.get()
obj.put()