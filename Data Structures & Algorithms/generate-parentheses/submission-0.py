class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        if openP < n: add (
        if closedP < openP: add )
        valid additions when openP == closedP == n
        """
        res, stack = [], []

        def backtrack(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()
            if openP > closedP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()
        
        backtrack(0, 0)

        return res

