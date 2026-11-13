#URL: https://leetcode.com/problems/contains-duplicate/
#neet code solution video ref:https://youtu.be/3OamzN90kPg

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False