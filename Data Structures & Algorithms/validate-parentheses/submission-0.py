class Solution:
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
        

        