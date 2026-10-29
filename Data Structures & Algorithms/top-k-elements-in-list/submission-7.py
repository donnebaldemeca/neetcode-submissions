class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        
        my_heap = []

        for num in my_dict.keys():
            heapq.heappush(my_heap, (my_dict[num], num))

            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        return [heapq.heappop(my_heap)[1] for i in range(k)]