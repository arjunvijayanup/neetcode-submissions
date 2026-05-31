class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens == []: return 0

        res = []

        for num in tokens:

            if num == "+":
                res.append(res.pop() + res.pop())
            elif num == "-":
                a, b = res.pop(), res.pop() # initializing pop values in the right order
                res.append(b - a)
            elif num == "*":
                res.append(res.pop() * res.pop())
            elif num == "/":
                a, b = res.pop(), res.pop()
                res.append(int(b / a))
            else:
                res.append(int(num))
        
        return res[0]
            

