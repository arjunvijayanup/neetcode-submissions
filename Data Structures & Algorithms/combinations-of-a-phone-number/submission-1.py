class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, comb = [], []
        dMap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        def bt(i, curStr):
            if len(digits) == len(curStr):
                res.append(curStr)
                return
            for c in dMap[digits[i]]:
                bt(i+1 , curStr + c)
            
        if digits:
            bt(0, "")
            
        return res
