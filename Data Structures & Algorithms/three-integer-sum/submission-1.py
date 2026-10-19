class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort() #1. sort input array
        for i, a in enumerate(nums): # [(0, -4), (1, -1).....,
            if i > 0 and a == nums[i -1]: # we don't want to reuse the same value
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

            


        