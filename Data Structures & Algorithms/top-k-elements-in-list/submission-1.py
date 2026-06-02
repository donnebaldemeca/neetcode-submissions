class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        output = []

        while len(output) < k:
            val = max(count, key=count.get)
            output.append(val)
            count.pop(val)
        
        return output
