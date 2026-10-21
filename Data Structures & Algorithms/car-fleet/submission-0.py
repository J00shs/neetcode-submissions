class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)] #list comprehension, array of pairs, zip puts multiple iterators in one iterator
        stack = []
        for p, s in sorted(pair)[::-1]:#reverse sorted
            stack.append((target - p) / s) #distance formula, target - position / speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() #decreasing the number of car fleets
        return len(stack)
        