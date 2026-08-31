class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        # Remember, dummy head
        self.head = ListNode(-1)
        # Point the dummy head to itself
        self.tail = self.head


    
    def get(self, index: int) -> int:
        # We need to iterate through each node until we land at the index we want.
        # Since the first node is a dummy node, we need to  call the .next pointer 
        curr = self.head.next
        i = 0
        # While non-null, run this loop
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            # If list was empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
         i = 0
         curr = self.head
         while i < index and curr:
            # Move curr to node before target node
            i += 1
            curr = curr.next
        # Confirm if previous and target node exists
         if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
         return False

        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
