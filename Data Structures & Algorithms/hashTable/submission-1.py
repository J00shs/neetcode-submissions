# Creation of LinkedList Nodes
# Linkedlist nodes are important in the case that we have collisions
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # What is this variable?
        self.next = None



class HashTable:
    # Our Hashtable will be an array of linkedlist nodes
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # What is self.table responsible for? Is this the table itself? 
        self.table = [None] * capacity

    # When we hash something, it's the length of the key mod the capacity of the current array
    def hash_function(self, key):
        return key % self.capacity



    def insert(self, key: int, value: int) -> None:
        # 1st - fetch the index. Use the key, call the hash function, and generate an index
        index = self.hash_function(key)
        # 2nd - Fetch what is at the current index. This is important.
        node = self.table[index]
        # 3rd - Use the head we fetch to see if it's null. Null means no key-value is there.
        # We'll create a node and insert at the given index 
        if not node:
            self.table[index] = Node(key, value)
    
        # If there is a value there(non-null), we'll traverse the linked-list
        else:
            prev = None
            while node:
                # If the key already exists, replace the value
                if node.key == key:
                    node.value = value
                    return
                prev , node = node, node.next
            prev.next = Node(key,value)
        self.size += 1
        # Check to see if array is half full. If so, resize. 
        if self.size / self.capacity >= 0.5:
            self.resize()
    # Does the insert() function perform chaining if a index is already taken?
    # Yes, it's performing chaining. Hence, the LinkedList nodes. 
    # If an existing key is already at the index, it's value will be updated


    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        # Return the value based on the provided key in the get
        # If the provided key matches a node key, we return the value of the node
        # If the provided key does not match the key of the node, it'll return -1.
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1
        


    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        prev = None

        # While the node is non-null
        while node:
            if node.key == key:
                # If previous is non-null, aka, deleting a node that's not first
                if prev:
                    prev.next = node.next
                # If it's null, aka, the first node 
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            # Shift our pointer to the next node
            # We also capture the previous node
            prev, node = node, node.next
        # If we don't find the key
        return False


             


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        # Creation of new table with more capacity
        new_table = [None] * self.capacity

        # Now we need to move the nodes into the new table
        for node in self.table:
            while node:
                index = node.key % self.capacity
                # If it's an empty linked list at the index, we just create a new node
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                            new_node = new.node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next
        self.table = new_table



