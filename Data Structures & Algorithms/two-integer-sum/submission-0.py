class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_map = {}

        for n in range(len(nums)):
            compliment = target - nums[n]
            if compliment in compliment_map:
                return [compliment_map[compliment], n]
            else:
                compliment_map[nums[n]] = n
        return None