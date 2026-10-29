class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1
        
        my_list = []

        for i in range(k):
            most_freq = max(my_dict, key=my_dict.get)
            my_list.append(most_freq)
            my_dict.pop(most_freq)
        return my_list