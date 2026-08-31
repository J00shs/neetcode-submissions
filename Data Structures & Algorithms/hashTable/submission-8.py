class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Hashtable size
        self.table = [None] * capacity

    def hash_function(self, key):
        # Determines which index to store the key in
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        # 1. Get the index to store the key at
        index = self.hash_function(key)
        # 2. Store the index in a variable.
        # We will need to check to see if there is already a node
        head = self.table[index]
        
        # If NULL, meaning there isn't a node there
        if not head:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # If NOT NULL, meaning there is a node there.
            # Check for key to update or append to end
            prev = None
            curr = head
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                prev, curr = curr, curr.next
            prev.next = Node(key, value)
            self.size += 1
            
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.table[index]

        while head:
            if head.key == key:
                return head.value
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
            prev, head = head, head.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # 1. Make copy of old table
        old_table = self.table
        # 2. Double original capacity
        self.capacity *= 2
        # 3. Create new table with new capacity size
        self.table = [None] * self.capacity
        self.size = 0

        for head in old_table:
            while head:
                self.insert(head.key, head.value)
                head = head.next