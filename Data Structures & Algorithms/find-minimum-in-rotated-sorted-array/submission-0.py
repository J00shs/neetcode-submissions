class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search b/c of the O(log n), sorted array, minimum kth element

        # // means floor division

        res = nums[0] 

        L, R = 0, len(nums) - 1
        
        while L <= R:
            if nums[L] < nums[R]:
                # in the situation where the array is sorted. we break out out the while loop
                res = min(res, nums[L])
                break 
            m = (L + R) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[L]:
                L = m + 1
            else:
                R = m - 1
        return res


