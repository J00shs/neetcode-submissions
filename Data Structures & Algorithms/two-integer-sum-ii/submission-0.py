class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0 #start of array
        R = len(numbers) - 1 #end of array
        current_sum = 0 

        while L < R:
            current_sum = numbers[L] + numbers[R]
            if current_sum < target:
                L += 1
                continue
            elif current_sum > target:
                R -= 1
                continue
            if current_sum == target:
                return [L + 1, R + 1]
            



        