class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list=[]
        for i in range(len(nums)*2):
            new_list.append(nums[i%len(nums)])
        return new_list