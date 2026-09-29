class Solution:
    # Imagine a dungeon with multiple rooms. Each room has different types of doors.
    # You have a torch holder. When you enter the room, you must light a torch and place it on your holder. Newest torch sits on top
    # When you reach an exit, you must leave the torch that was lit most recently. The room will only allow you to exit if the exit torch matches the gate. 
    # If you have no torches, or the top torch doesn't match the exit gate, you'll die!
    
    # Types of Gates; ( = torch, ) = exit gate
    # Wooden - ( )
    # Stone - []
    # Golden - { }
    def isValid(self, s: str) -> bool:
        # Time complexity and Memory - O(n)

        # 1. Create an empty stack and hashmap of closed -> open characters
        stack = []
        closeToOpen = {"}":"{"
                      ,")":"("
                      ,"]":"[" }

        # Check if character is a open or closed bracket
        for c in s:
            # If this is a closing character
            if c in closeToOpen:
                # Check if stack is not empty and value at top of stack is the matching opening character 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # If the stack is empty or characters dont match
                else:
                    return False
            else:
                stack.append(c)
        # Return true if the stack is not empty
        return True if not stack else False
        

        