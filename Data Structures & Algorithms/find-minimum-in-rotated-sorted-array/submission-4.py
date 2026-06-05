class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        res = float("infinity")
        while low < high:
            # if nums[low] < nums[high]:
            #     res = min(res, nums[low])
            #     break

            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
            
        return nums[high]

                