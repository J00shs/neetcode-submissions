class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Set an arr with default values of 1
        res = [1] * (len(nums))

        # 1a. Set the default prefix to 1
        prefix = 1
        # 2. Calculate the prefixes and store in arr
        for i in range(len(nums)):
            # 2a. ith val * prefix = new_prefix
            # 2b. store new_prefix at in new arr
            res[i] = prefix
            prefix *= nums[i]

    # 3. Set the default postfix to 1
        postfix = 1
        # 4. Calculate the postfixes and override values in arr
        for i in range(len(nums) -1, -1, -1):
                                #start stop(before -1) step(move backwards by one)
            res[i] *= postfix
            postfix *= nums[i]
        return res



