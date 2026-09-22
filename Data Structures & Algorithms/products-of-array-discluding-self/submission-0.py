class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result arr. Each position will have an intial value of 1
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            # Put the prefix into that position
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



