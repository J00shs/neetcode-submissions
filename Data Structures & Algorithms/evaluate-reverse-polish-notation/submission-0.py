class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                # Perform math
                if t == operators[0]:
                    res = left + right
                elif t == operators[1]:
                    res = left - right
                elif t == operators[2]:
                    res = right * left
                else:
                    res = int(left / right)
                stack.append(res)
        return stack[-1]