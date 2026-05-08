class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # Reverse the iteration
        # new max = max(old max, arr[i])
        n = len(arr)
        oldMax = -1
        for i in range(n-1, -1, -1):
            newMax = max(oldMax, arr[i])
            arr[i] = oldMax
            oldMax = newMax
        
        return arr

            
