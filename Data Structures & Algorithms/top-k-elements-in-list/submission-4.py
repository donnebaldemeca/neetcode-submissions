class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sort_arr = []

        for num, cnt in count.items():
            sort_arr.append([cnt, num])
        sort_arr.sort()

        res = []

        while len(res) < k:
            res.append(sort_arr.pop()[1])

        return res