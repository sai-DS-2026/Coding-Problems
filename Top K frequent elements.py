#URL: https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        return sorted(count,key = count.get,reverse = True)[:k]
