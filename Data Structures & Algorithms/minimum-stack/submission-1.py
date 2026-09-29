class MinStack:
    # For this problem, think of a resturant with a set of plates.
    # A manager wants to know what the lightest plate is on the stack of plates
    # Everytime he adds a new plate, he keeps track of which one is the lighest up until this point on a seperate piece of paper

    def __init__(self):
        self.stack = []
        # A minimum stack ton keep track of the min value added so far
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self-minStack[-1]- the manager sees the lightest plate so far
        # He'll then compare the new plate with the previous minium and record which ever is        lighter.
        # If this is the first plate, compare the plate with itself
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        # 

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        



        
        
