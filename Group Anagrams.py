#URL: https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list) #initializes dict with empty list, it is in collections class

        for word in strs:
            count_of_alphabets = [0]*26
            for alphabet in word:
                count_of_alphabets[ord("a")-ord(alphabet)] += 1

            hashmap[tuple(count_of_alphabets)].append(word) #using tuple because list is mutable and not allowed as a key in dict
        return list(hashmap.values())