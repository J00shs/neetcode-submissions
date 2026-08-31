class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I need a for-loop to subtract the target with the number at the current index. How  
        # I need a for-loop to subtract the target with the number at the current index. How?
        # Use enumerate to loop through a sequence to get the index and value

            values = {}
            for i, num in enumerate(nums):
                difference = target - num
                if difference in values:
                    return [values[difference], i]
                values[num] = i
                # How do I add to the hashmapsimply?
            return

        