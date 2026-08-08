class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1)
        intSec = set()

        for num in nums2:
            if num in nums:
                intSec.add(num)

        return list(intSec)