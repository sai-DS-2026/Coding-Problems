#URL: https://leetcode.com/problems/valid-anagram/
#neet code solution video ref: https://youtu.be/9UtInBqnCgA
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        return "".join(sorted(s)) == "".join(sorted(t))