class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        closemap = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in closemap:
                if stack and stack[-1]==closemap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack