
class Node:

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

#l = Node(3)


# Find Head of the List

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert data into linked list

    '''
    Simplest Method (Insert new node by placing it at the head of the list and point new node at the old head 
    (Note: Sort of pushing the other node down the line, As for Time Complexity, this implementation of insert is constant O(1)
    This is because the insert method, no matter what, will always take the same amount of time: it can only take one data point,
    it can only ever create one node, and the new node doesn’t need to interact with all the other nodes in the list, the inserted
    node will only ever interact with the head.)
    '''
    '''
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    '''
# Insert node in the list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next_node):
                current = current.next_node
            current.next_node = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # Search

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    # Delete

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())








