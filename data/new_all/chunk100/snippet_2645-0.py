class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def count(self, key):
        current = self.head
        count = 0
        while current:
            if current.data == key:
                count = count + 1
            current = current.next
        return count
for data in [5, 1, 3, 5, 5, 15, 4, 9, 2]:
    a_llist.append(data)
print('The linked list: ', end='')
a_llist.display()
print()
key = int(input('Enter data item: '))
count = a_llist.count(key)
print('{0} occurs {1} time(s) in the list.'.format(key, count))