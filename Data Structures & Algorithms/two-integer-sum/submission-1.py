class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in my_dict:
                j = my_dict[compliment]
                return [j, i]
            my_dict[num] = i