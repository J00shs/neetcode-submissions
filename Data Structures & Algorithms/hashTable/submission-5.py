class Node:
    def __init__(self,key , val):
        self.key = key
        self.value = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Initial size of hashtable
        self.size = 0
        # The hashtable will be an array of LinkedList Nodes
        self.table = [None] * capacity
    

    # Remember, we have to get the sum of all the ASCII values of the key
    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        # We need to get the head and 
        # check if there is already a node at the index
        head = self.table[index]
        # If there is NOT a prexisting node
        if not head:
            self.table[index] = Node(key,value)
            self.size += 1
        else:
            prev = None
            while head:
                # Check if the key already exists...
                if head.key == key:
                    # If so, we'll update the value
                    head.value = value
                    return 
                prev = head
                head = head.next 
            prev.next = Node(key,value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()
        


    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.table[index]
        
        while head:
            if head.key == key:
                return head.value
            # shift pointer by one
            head = head.next
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.table[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next

                else:
                    self.table[index] = head.next

                self.size -= 1
                return True
            prev = head
            head = head.next
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity

        for node in old_table:
            while node:
                self.insert(node.key, node.value)
                node = node.next