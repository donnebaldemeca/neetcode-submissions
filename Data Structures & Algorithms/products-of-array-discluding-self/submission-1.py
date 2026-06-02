class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make a prefix list
        # make suffix list
        # multiply each list to get result

        prefix = []
        suffix = []

        for i in range(len(nums)):
            pref = 1
            suff = 1
            for j in range(0,i):
                pref = pref * nums[j]
            prefix.append(pref)
            for k in range(i+1,len(nums)):
                suff = suff * nums[k]
            suffix.append(suff)
        
        result = []
        
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result