class Solution:
    def trap(self, height: List[int]) -> int:
        trap = 0
        maxLeft, maxRight = [0] * len(height), [0] * len(height)

        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        
        maxRight[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        for i in range(len(height)):
            calc = min(maxRight[i], maxLeft[i]) - height[i]
            trap += calc if calc > 0 else 0
        
        return trap





            
            