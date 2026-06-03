class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # base case, if the lowest number is positive
                break

            if i > 0 and a == nums[i - 1]: # move iterator over duplicates
                continue

            l, r = i + 1, len(nums) - 1 # set left pointer 1 after the iterator, and right pointer at the end of list
            while l < r: # 2 pointer
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # move left pointer over duplicates
                        l += 1

        return res