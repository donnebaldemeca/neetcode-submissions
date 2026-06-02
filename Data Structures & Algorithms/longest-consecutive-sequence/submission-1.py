class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: # base case
            return 0
        res = 0
        nums.sort() # sort

        predicted_value = nums[0] # pointer to compare
        streak = 0
        i = 0

        while i < len(nums):
            if nums[i] != predicted_value: # reset pointer and streak
                predicted_value = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == predicted_value: # iterate
                i += 1
            streak += 1 # update
            predicted_value += 1
            res = max(res, streak)
        
        return res