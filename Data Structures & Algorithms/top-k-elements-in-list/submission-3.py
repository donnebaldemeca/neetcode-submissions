class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        answer = heapq.nlargest(k, hashmap, key=hashmap.get)
        
        return answer