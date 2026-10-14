class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures): # get the index and temperature value at the same time
            while stack and t > stack[-1][0]: #top of stack, tempature value of our pair
                stackT, stackInd = stack.pop() # put temp and index in variables
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


        