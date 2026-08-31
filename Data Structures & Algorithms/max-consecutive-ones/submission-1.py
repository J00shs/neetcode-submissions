class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Iterate through array
        # Add to streak if 1, reset if 0 
        # I have to capture the current streak and compare it with any new streaks
        longest_streak = 0
        current_streak = 0

        for i in nums:
            if i == 1:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0

        return longest_streak